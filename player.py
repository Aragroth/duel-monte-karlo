import random
from cards.first_age import first_age_cards
from resources import CardStatus, CardColor, CardStateKnown, Resource, ScienceSymbol, ScienceTokens
from card import Card
import enum

from wonder import Wonder
import itertools

class Player:
    def __init__(self, current_money=7, available_wonders=None, built_wonders=None, science_tokens=None, cards=None) -> None:
        self.science_tokens: list[ScienceTokens] = [] if science_tokens is None else science_tokens

        self.built_wonders: list[Wonder] = [] if built_wonders is None else built_wonders
        self.available_wonders = [] if available_wonders is None else available_wonders
        self.cards: list[Card] = [] if cards is None else cards
        self.current_money = current_money

        self.was_first_war_mark = False
        self.was_second_war_mark = False
        
        self.science_symbols = [card.science_symbol for card in self.cards if card.science_symbol is not None]
        if ScienceTokens.LAW in self.science_tokens:
            self.science_symbols.append(ScienceSymbol.VESI)

        self.collected_science_symbols_pairs = [symb for symb in self.science_symbols if self.science_symbols.count(symb) >= 2]
        self.opponent = None

    def set_opponent(self, opponent):
        self.opponent: Player = opponent
    
    def resource_cost(self, needed_resource: Resource) -> int:
        for card in self.cards:
            if needed_resource in card.resources_reduced_cost:
                return 1

        count = 2 # default cost for every player
        for card in self.opponent.cards:
            if card.color in [CardColor.BROWN, CardColor.GREY]:
                for res in card.resources_generated:
                    if type(res) is list and needed_resource in res:
                        count += 1
                    elif needed_resource is res:
                        count += 1
        return count

    def sell_card(self) -> None:
        yellow_cards_number = len([
            card for card in self.cards if card.color is CardColor.YELLOW
        ])

        total_gain = 2 + yellow_cards_number
        self.current_money += total_gain
    
    def minimal_cost(self, need_resources: list[Resource]) -> int:
        need_resources = need_resources.copy()
        
        resource_options = []
        for card in self.cards:
            for generated_res in card.resources_generated:
                if type(generated_res) is list:
                    resource_options.append(generated_res)
                elif generated_res in need_resources:
                    need_resources.remove(generated_res)
        
        for wonder in self.built_wonders:
            if len(wonder.can_give_resource) != 0:
                resource_options.append(wonder.can_give_resource)
        
        minimal_cost = float("+inf")
        for option in itertools.product(*resource_options):
            needed_res_left = need_resources.copy()
            
            for elem in option:
                if elem in needed_res_left:
                    needed_res_left.remove(elem)
            
            total_cost = 0
            for need in needed_res_left:
                total_cost += self.resource_cost(need)
            
            if total_cost < minimal_cost:
                minimal_cost = total_cost
            
            if minimal_cost == 0:
                return 0
            
        return minimal_cost

    def try_build_card(self, card: Card, force_free_build=False) -> bool:
        if card.prev_card in self.cards or force_free_build:
            if ScienceTokens.URBANISM in self.science_tokens and card.prev_card in self.cards:
                self.current_money += 4
            # TODO  maybe fix it somehow for all to be at end
            if card.science_symbol is not None:
                self.science_symbols.append(card.science_symbol)

            self.cards.append(card)
            return True
        
        total_cost = card.money_cost
        
        if ScienceTokens.MASONRY in self.science_tokens and card.color is CardColor.BLUE:
            resource_price = float('+inf')
            if len(card.resources_cost) <= 2:
                resource_price = 0
            else:
                for combination in itertools.combinations(card.resources_cost, 2):
                    shallow_res = card.resources_cost.copy()
                    for resource in combination:
                        shallow_res.remove(resource)
                    new_cost = self.minimal_cost(shallow_res)
                    if new_cost < resource_price:
                        resource_price = new_cost
        else:    
            resource_price = self.minimal_cost(card.resources_cost)
        
        total_cost += resource_price
        
        if self.current_money < total_cost:
            return False

        if ScienceTokens.ECONOMY in self.opponent.science_tokens:
            self.opponent.current_money += resource_price
        
        if card.science_symbol is not None:
            self.science_symbols.append(card.science_symbol)

        self.current_money -= total_cost
        if card.preaction is not None:
            card.preaction(self)

        self.cards.append(card)
        return True

    def try_build_wonder(self, wonder: Wonder) -> bool:
        if not self.is_allowed_build_wonder():
            return False

        if ScienceTokens.ARCHITECTURE in self.science_tokens:
            total_cost = float('+inf')
            for combination in itertools.combinations(wonder.resources_cost, 2):
                shallow_res = wonder.resources_cost.copy()
                for resource in combination:
                    shallow_res.remove(resource)
                new_cost = self.minimal_cost(shallow_res)
                if new_cost < total_cost:
                    total_cost = new_cost
        else:    
            total_cost = self.minimal_cost(wonder.resources_cost)

        if self.current_money < total_cost:
            return False
    
        self.current_money -= total_cost
        self.built_wonders.append(wonder)
        self.available_wonders.remove(wonder)

        return True

    def is_allowed_build_wonder(self) -> bool:
        is_max_wonder = (len(self.built_wonders) + len(self.opponent.built_wonders)) == 7
        has_wonders =  len(self.available_wonders) > 0
        return not is_max_wonder and has_wonders
    
    def select_wonder(self) -> Wonder:
        return random.choice(self.available_wonders)

    def destory_card(self, card):
        if card in self.cards:
            self.cards.remove(card)
        
    def has_new_science_symbol_pair(self):
        for card in self.cards:
            if card.science_symbol is not None:
                symb = card.science_symbol
                for new_card in self.cards:
                    are_equal = symb is new_card.science_symbol 
                    if new_card is not card and are_equal and symb not in self.collected_science_symbols_pairs:
                        self.collected_science_symbols_pairs.append(symb)
                        return True
        return False

