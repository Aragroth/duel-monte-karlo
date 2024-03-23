from table import Table
import random
from cards.first_age import first_age_cards
from player import Player
from resources import CardStatus, CardColor, CardStateKnown, Resource, ScienceSymbol, ScienceTokens
from card import Card
import enum

from wonder import Wonder
import itertools

class Session:
    class Actions(enum.Enum):
        BUILD_WONDER = 1
        BUILD_CARD = 2
        SELL_CARD = 3

    def __init__(self, good_player, opponent, table: Table, available_science_tokens, war_status=0, ) -> None:
        self.good_player: Player = good_player
        self.opponent: Player = opponent

        self.available_science_tokens: list[ScienceTokens] = available_science_tokens

        self.age = table.age
        self.table: Table = table
        self.war_status = war_status

        self.first_action = None
    
    def update_war(self, player: Player, power: int):
        if player is self.good_player:
            self.war_status += power
        else:
            self.war_status -= power

        # TODO check minus balance
        if self.war_status >= 2:
            if not self.opponent.was_first_war_mark:
                self.opponent.current_money -= 2
                self.opponent.was_first_war_mark = True
        
        if self.war_status >= 5:
            if not self.opponent.was_second_war_mark:
                self.opponent.current_money -= 5
                self.opponent.was_second_war_mark = True

        if self.war_status <= -2:
            if not self.good_player.was_first_war_mark:
                self.good_player.current_money -= 2
                self.good_player.was_first_war_mark = True
        
        if self.war_status <= -5:
            if not self.good_player.was_second_war_mark:
                self.good_player.current_money -= 5
                self.good_player.was_second_war_mark = True

    def check_progress_token(self, player: Player) -> bool:
        if player.has_new_science_symbol_pair() and len(self.available_science_tokens) > 0:
            new_token = random.choice(self.available_science_tokens)
            self.available_science_tokens.remove(new_token)
            player.science_tokens.append(new_token)

            if new_token is ScienceTokens.AGRICULTURE or new_token is ScienceTokens.URBANISM:
                player.current_money += 6
            return True
        
        return False

    def check_war_victory(self, player: Player):
        return self.war_status * (-1) ** (player is self.opponent) >= 9 

    def check_science_victory(self, player: Player):
        return len(set(player.science_symbols)) >= 6
    
    def calculate_win_points(self, player: Player):
        total_points = 0
        total_points += sum([card.culture_points for card in player.cards])
        total_points += sum([card.endgame_action(player) for card in player.cards if card.endgame_action is not None])
        total_points += sum([wonder.culture_points for wonder in player.built_wonders])
        total_points += player.current_money // 3

        if ScienceTokens.AGRICULTURE in player.science_tokens:
            total_points += 4
        if ScienceTokens.MATHEMATICS in player.science_tokens:
            total_points += 3 * len(player.science_tokens)
        if ScienceTokens.PHILOSOPHY in player.science_tokens:
            total_points += 7

        player_related_war_points = self.war_status * (-1) ** (player is self.opponent)
        if player_related_war_points >= 6:
            total_points += 10
        elif player_related_war_points >= 3:
            total_points += 5
        elif player_related_war_points >= 1:
            total_points += 2
        
        return total_points
        
    def check_age_end(self):
        return self.table.has_age_ended()
    
    def update_age(self, new_table: Table):
        self.age = new_table.age
        self.table = new_table

    def dropped_cards(self):
        result = []
        old_cards = [card for card in self.table.used_cards if card not in self.table.age_cards]
        for card_check in old_cards:
            if card_check not in self.good_player.cards and card_check not in self.opponent.cards:
                result.append(card_check)

        for card_check in self.table.age_cards:
            for row in self.table.layout:
                for table_card in row:
                    if card_check is table_card.card and table_card.status is CardStatus.TAKEN:
                        if card_check not in self.good_player.cards and card_check not in self.opponent.cards:
                            result.append(card_check)
        return result

    def make_turn(self, player: Player):
        next_extra_turn = False

        available_green_cards = [
            card.card for row in self.table.layout for card in row
            if card.status is CardStatus.CAN_BE_TAKEN and card.card.color is CardColor.GREEN
        ]

        # if opponent is aggressive in science victory
        if player is self.opponent and len(available_green_cards) > 0 and random.choice([True, False]):
            sel_card = random.choice(available_green_cards)
            selected_action = self.Actions.BUILD_CARD

        else:
            sel_card: Card = self.table.select_card()
            # TODO add less probablity to action of just selling, becuase wonders often just sold 
            available_actions = [self.Actions.BUILD_CARD, self.Actions.SELL_CARD]
            if player.is_allowed_build_wonder():
                available_actions.append(self.Actions.BUILD_WONDER)
            selected_action = random.choice(available_actions)

        if selected_action is self.Actions.BUILD_CARD:
            has_built = player.try_build_card(sel_card)
            
            if has_built:
                attacking_power = sel_card.attack_power
                if ScienceTokens.STRATEGY in player.science_tokens and sel_card.color is CardColor.RED:
                    attacking_power += 1
                self.update_war(player, attacking_power)

                # TODO fix
                if self.first_action is None:
                    self.first_action = (selected_action, sel_card)
            else:
                # TODO fix
                if self.first_action is None:
                    self.first_action = (self.Actions.SELL_CARD, sel_card)
                player.sell_card()

        elif selected_action is self.Actions.SELL_CARD:
            if self.first_action is None:
                    self.first_action = (selected_action, sel_card)
            player.sell_card()

        elif selected_action is self.Actions.BUILD_WONDER:
            has_built = False
            is_allowed = player.is_allowed_build_wonder()
            if is_allowed:
                sel_wonder = player.select_wonder()
                has_built = player.try_build_wonder(sel_wonder)
            
            if has_built:
                if self.first_action is None:
                    self.first_action = (selected_action, f"({sel_card.title}) - {sel_wonder.title}")

                next_extra_turn = sel_wonder.extra_turn or ScienceTokens.THEOLOGY in player.science_tokens
                self.update_war(player, sel_wonder.attack_points)
                if sel_wonder.destroy_card_color is not None:
                    opponent_color_cards = [card for card in player.opponent.cards if card.color == sel_wonder.destroy_card_color]
                    if len(opponent_color_cards) != 0:
                        player.opponent.destory_card(random.choice(opponent_color_cards))
                if sel_wonder.get_science_token:
                    dropped_tokens = [ token for token in list(ScienceTokens)
                        if  token not in self.available_science_tokens and
                            token not in player.science_tokens and
                            token not in player.opponent.science_tokens
                    ]
                    player.science_tokens.append(random.choice(dropped_tokens))
                if sel_wonder.build_deleted_card:
                    dropped_cards = self.dropped_cards()
                    if len(dropped_cards) != 0:
                        player.try_build_card(random.choice(dropped_cards), force_free_build=True)
            else:
                if self.first_action is None:
                    self.first_action = (self.Actions.SELL_CARD, sel_card)
                    
                player.sell_card()
        
        self.table.open_other_cards()
        
        self.check_progress_token(player)

        # self.state_printer(player)

        return next_extra_turn

    def state_printer(self, player):
        print('\n---------------------------------------------------------')
        print('good turn' if player is self.good_player else 'bad turn')
        print('war: ', self.war_status)
        print(self.table)
   
        print('good player: ')
        print(self.good_player.cards)
        print(self.good_player.built_wonders)
        print(self.good_player.science_symbols)
        print(self.good_player.science_tokens)
        print(self.good_player.collected_science_symbols_pairs)
        print(self.good_player.current_money)

        print('opponent: ')
        print(self.opponent.cards)
        print(self.opponent.built_wonders)
        print(self.opponent.science_symbols)
        print(self.opponent.science_tokens)
        print(self.opponent.collected_science_symbols_pairs)
        print(self.opponent.current_money)

    def __str__(self) -> str:
        return f"{self.war_status}"
    
    def __repr__(self) -> str:
        return str(self)
    