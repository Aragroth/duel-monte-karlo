import random
from cards.first_age import first_age_cards
from resources import CardStatus, CardColor, CardStateKnown, Resource, ScienceSymbol, ScienceTokens
from card import Card
import enum

from wonder import Wonder
import itertools


class CardTable:
    def __init__(self, card: Card | None, status: CardStatus) -> None:
        self.card = card
        self.status = status

    def __str__(self) -> str:
        return f"{self.card} - {self.status.name}"

    def __repr__(self) -> str:
        return str(self)


class Table:
    def __init__(self, age: int, age_cards, used_cards=None) -> None:
        self.layout: list[list[CardTable]] = []
        self.age_cards = age_cards
        self.age = age
        self.used_cards = [] if used_cards is None else used_cards

    def open_other_cards(self):
        pass
    
    def has_age_ended(self) -> bool:
        pass

    def select_card(self) -> Card:
        available_cards = [card for row in self.layout for card in row if card.status is CardStatus.CAN_BE_TAKEN]
        if len(available_cards) == 0:
            return None
        
        selected: CardTable = random.choice(available_cards)
        selected.status = CardStatus.TAKEN
        return selected.card

    def generate_new_card(self):
        new_card = random.choice(list(set(self.age_cards).difference(set(self.used_cards))))
        self.used_cards.append(new_card)
        return new_card
    
    def has_age_ended(self) -> bool:
        not_played_cards = len([card for row in self.layout for card in row if card.status is not CardStatus.TAKEN])
        return not_played_cards == 0 
                    
class FirstAgeTable(Table):
    def __init__(self, age: int, age_cards, used_cards=None) -> None:
        super().__init__(age, age_cards, used_cards)

    def start_layout(self):
        self.layout = [] 
        counter = 0 
        age_cards = random.sample(self.age_cards, 20)
        for sides in [6, 5, 4, 3, 2]:
            side = []
            for _ in range(sides):
                if sides % 2 == 0:
                    side.append(
                        CardTable(age_cards[counter], CardStatus.LOCKED)
                    )
                    self.used_cards.append(age_cards[counter])
                else:
                    side.append(
                        CardTable(None, CardStatus.LOCKED)
                    )
                counter += 1
            self.layout.append(side)
        
        for i in range(6):
            self.layout[0][i].status = CardStatus.CAN_BE_TAKEN


    def fixed_layout(self):
        self.layout = [] 
        counter = 0 
        age_cards = random.sample(self.age_cards, 20)
        for sides in [6, 5, 4, 3, 2]:
            side = []
            for _ in range(sides):
                if sides % 2 == 0:
                    side.append(
                        CardTable(age_cards[counter], CardStatus.LOCKED)
                    )
                    self.used_cards.append(age_cards[counter])
                else:
                    side.append(
                        CardTable(age_cards[counter], CardStatus.LOCKED)
                    )
                counter += 1
            self.layout.append(side)
        
        for i in range(6):
            self.layout[0][i].status = CardStatus.CAN_BE_TAKEN
    
    def set_layout(self, layout):
        self.layout = [] 
        sides = [6, 5, 4, 3, 2]
        for sides_ind in range(len(sides)):
            side = []
            for i in range(len(layout[sides_ind])):
                if sides[sides_ind] % 2 == 0:
                    side.append(
                        CardTable(layout[sides_ind][i], CardStatus.LOCKED)
                    )
                    self.used_cards.append(layout[sides_ind][i])
                else:
                    side.append(
                        CardTable(layout[sides_ind][i], CardStatus.LOCKED)
                    )
            self.layout.append(side)

        for i in range(6):
            self.layout[0][i].status = CardStatus.CAN_BE_TAKEN

    def open_other_cards(self):
        for row_ind in range(1, len(self.layout)):
            row = self.layout[row_ind]
            for card_ind in range(len(row)):
                is_left_taken = self.layout[row_ind - 1][card_ind].status is CardStatus.TAKEN 
                is_right_taken = self.layout[row_ind - 1][card_ind + 1].status is CardStatus.TAKEN 
                is_current_taken = self.layout[row_ind][card_ind].status is CardStatus.TAKEN 

                if is_left_taken and is_right_taken and not is_current_taken:
                    if self.layout[row_ind][card_ind].card is None:
                        self.layout[row_ind][card_ind].card = self.generate_new_card()
                    self.layout[row_ind][card_ind].status = CardStatus.CAN_BE_TAKEN

    def __str__(self) -> str:
        combined = ''
        for row_ind in range(len(self.layout)):
            combined += '\t' * row_ind + f"{self.layout[row_ind]}" + '\n'                    
        return combined


class SecondAgeTable(Table):
    def __init__(self, age: int, age_cards, used_cards=None) -> None:
        super().__init__(age, age_cards, used_cards)

    def start_layout(self):
        counter = 0 
        age_cards = random.sample(self.age_cards, 20)
        for sides in [2, 3, 4, 5, 6]:
            side = []
            for _ in range(sides):
                if sides % 2 == 0:
                    side.append(
                        CardTable(age_cards[counter], CardStatus.LOCKED)
                    )
                    self.used_cards.append(age_cards[counter])
                else:
                    side.append(
                        CardTable(None, CardStatus.LOCKED)
                    )
                counter += 1
            self.layout.append(side)
        
        for i in range(2):
            self.layout[0][i].status = CardStatus.CAN_BE_TAKEN
    
    def open_other_cards(self):
        for row_ind in range(1, len(self.layout)):
            row = self.layout[row_ind]
            for card_ind in range(len(row)):
                if card_ind == 0:
                    is_right_taken = self.layout[row_ind - 1][card_ind].status is CardStatus.TAKEN
                    is_left_taken = True
                elif card_ind == (len(row) - 1):
                    is_right_taken = True
                    is_left_taken = self.layout[row_ind - 1][card_ind - 1].status is CardStatus.TAKEN
                else:
                    is_left_taken = self.layout[row_ind - 1][card_ind].status is CardStatus.TAKEN
                    is_right_taken = self.layout[row_ind - 1][card_ind - 1].status is CardStatus.TAKEN 
                
                is_current_taken = self.layout[row_ind][card_ind].status is CardStatus.TAKEN

                if is_left_taken and is_right_taken and not is_current_taken:
                    if self.layout[row_ind][card_ind].card is None:
                        self.layout[row_ind][card_ind].card = self.generate_new_card()
                    self.layout[row_ind][card_ind].status = CardStatus.CAN_BE_TAKEN
    
    def __str__(self) -> str:
        combined = ''
        for row_ind in range(len(self.layout)):
            combined += '\t' * (len(self.layout) - row_ind) + f"{self.layout[row_ind]}" + '\n'                
        return combined
    

class ThirdAgeTable(Table):
    def __init__(self, age: int, age_cards, gildia_cards, used_cards=None) -> None:
        super().__init__(age, age_cards, used_cards)
        self.gildia_cards = gildia_cards

    def start_layout(self):
        counter = 0 
        # TODO rewrite all tables to do this at init to be known
        self.age_cards = random.sample(self.age_cards, 17) + random.sample(self.gildia_cards, 3)
        age_cards = self.age_cards

        side_ind = 0
        for sides in [2, 3, 4, 2, 4, 3, 2]:
            side = []
            for _ in range(sides):
                if sides % 2 == 0 and side_ind != 3:
                    side.append(
                        CardTable(age_cards[counter], CardStatus.LOCKED)
                    )
                    self.used_cards.append(age_cards[counter])
                else:
                    side.append(
                        CardTable(None, CardStatus.LOCKED)
                    )
                counter += 1
            side_ind += 1
            self.layout.append(side)
        
        for i in range(2):
            self.layout[0][i].status = CardStatus.CAN_BE_TAKEN
    
    def open_other_cards(self):
        for row_ind in range(1, len(self.layout)):
            row = self.layout[row_ind]
            for card_ind in range(len(row)):
                # TODO rewrite
                if row_ind <= 2:
                    if card_ind == 0:
                        is_right_taken = self.layout[row_ind - 1][card_ind].status is CardStatus.TAKEN
                        is_left_taken = True
                    elif card_ind == (len(row) - 1):
                        is_right_taken = True
                        is_left_taken = self.layout[row_ind - 1][card_ind - 1].status is CardStatus.TAKEN
                    else:
                        is_left_taken = self.layout[row_ind - 1][card_ind].status is CardStatus.TAKEN
                        is_right_taken = self.layout[row_ind - 1][card_ind - 1].status is CardStatus.TAKEN 
                    
                    is_current_taken = self.layout[row_ind][card_ind].status is CardStatus.TAKEN

                    if is_left_taken and is_right_taken and not is_current_taken:
                        if self.layout[row_ind][card_ind].card is None:
                            self.layout[row_ind][card_ind].card = self.generate_new_card()
                        self.layout[row_ind][card_ind].status = CardStatus.CAN_BE_TAKEN
                
                elif row_ind == 3:
                    if card_ind == 0:
                        is_right_taken = self.layout[row_ind - 1][0].status is CardStatus.TAKEN
                        is_left_taken = self.layout[row_ind - 1][1].status is CardStatus.TAKEN
                    if card_ind == 1:
                        is_right_taken = self.layout[row_ind - 1][2].status is CardStatus.TAKEN
                        is_left_taken = self.layout[row_ind - 1][3].status is CardStatus.TAKEN
                    
                    is_current_taken = self.layout[row_ind][card_ind].status is CardStatus.TAKEN

                    if is_left_taken and is_right_taken and not is_current_taken:
                        if self.layout[row_ind][card_ind].card is None:
                            self.layout[row_ind][card_ind].card = self.generate_new_card()
                        self.layout[row_ind][card_ind].status = CardStatus.CAN_BE_TAKEN
                elif row_ind == 4:
                    if card_ind <= 1:
                        is_right_taken = self.layout[row_ind - 1][0].status is CardStatus.TAKEN
                        is_left_taken = True
                    else:
                        is_right_taken = self.layout[row_ind - 1][1].status is CardStatus.TAKEN
                        is_left_taken = True
                    
                    is_current_taken = self.layout[row_ind][card_ind].status is CardStatus.TAKEN

                    if is_left_taken and is_right_taken and not is_current_taken:
                        if self.layout[row_ind][card_ind].card is None:
                            self.layout[row_ind][card_ind].card = self.generate_new_card()
                        self.layout[row_ind][card_ind].status = CardStatus.CAN_BE_TAKEN

                elif row_ind > 4:
                    is_left_taken = self.layout[row_ind - 1][card_ind].status is CardStatus.TAKEN 
                    is_right_taken = self.layout[row_ind - 1][card_ind + 1].status is CardStatus.TAKEN 
                    is_current_taken = self.layout[row_ind][card_ind].status is CardStatus.TAKEN 

                    if is_left_taken and is_right_taken and not is_current_taken:
                        if self.layout[row_ind][card_ind].card is None:
                            self.layout[row_ind][card_ind].card = self.generate_new_card()
                        self.layout[row_ind][card_ind].status = CardStatus.CAN_BE_TAKEN

    def __str__(self) -> str:
        combined = ''
        for row_ind in range(len(self.layout)):
            combined += f"{self.layout[row_ind]}" + '\n'                
        return combined