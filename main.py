from resources import ScienceTokens
from player import Player
from session import Session
from table import FirstAgeTable, SecondAgeTable, ThirdAgeTable

from wonder import *
from cards.first_age import first_age_cards
from cards.second_age import second_age_cards
from cards.third_age import third_age_cards, third_age_gilds

import random
from time import time


def single_game():
    best_wonders = [
        artemis_hram,
        pirei,
        visachie_sadi,
        bolshoi_sphinks
    ]
    worst_wonders = [
        koloss_rodosski,
        zeus_statue,
        bolshoi_zirk,
        mausalei
    ]
    good_player = Player(available_wonders=worst_wonders)
    opponent = Player(available_wonders=best_wonders)

    good_player.set_opponent(opponent)
    opponent.set_opponent(good_player)

    first_table = FirstAgeTable(1, first_age_cards)

    sess = Session(good_player, opponent, first_table, [
        ScienceTokens.ARCHITECTURE, ScienceTokens.AGRICULTURE, ScienceTokens.ECONOMY, ScienceTokens.LAW, ScienceTokens.MASONRY
    ])

    turn_friendly = True
    cur_player = good_player
    while not sess.check_age_end():
        is_extra_turn = sess.make_turn(cur_player) 
        while is_extra_turn and not sess.check_age_end():
            is_extra_turn = sess.make_turn(cur_player) 
        
        if sess.check_war_victory(cur_player):
            return 1
        if sess.check_science_victory(cur_player):
            return 2

        turn_friendly = not turn_friendly
        if turn_friendly: cur_player = good_player
        else: cur_player = opponent
    
    # not possible to win in first age
    second_table = SecondAgeTable(2, second_age_cards)
    second_table.start_layout()

    old_cards_not_in_box = [card.card for row in first_table.layout for card in row]
    second_table.used_cards.extend(old_cards_not_in_box) # all dropped cards
    sess.update_age(second_table)

    if sess.war_status != 0:
        turn_friendly = random.choice([True, False])
        if turn_friendly:
            cur_player = good_player
        else:
            cur_player = opponent

    while not sess.check_age_end():
        is_extra_turn = sess.make_turn(cur_player) 
        while is_extra_turn and not sess.check_age_end():
            is_extra_turn = sess.make_turn(cur_player) 
        
        if sess.check_war_victory(cur_player):
            return 1
        if sess.check_science_victory(cur_player):
            return 2
        
        turn_friendly = not turn_friendly
        if turn_friendly: cur_player = good_player
        else: cur_player = opponent

        

    
    third_table = ThirdAgeTable(3, third_age_cards, third_age_gilds)
    third_table.start_layout()
    
    old_cards_not_in_box = [card.card for row in first_table.layout for card in row]
    old_cards_not_in_box.extend([card.card for row in second_table.layout for card in row])
    third_table.used_cards.extend(old_cards_not_in_box) # all dropped cards
    sess.update_age(third_table)
    
    if sess.war_status != 0:
        turn_friendly = random.choice([True, False])
        if turn_friendly:
            cur_player = good_player
        else:
            cur_player = opponent

    while not sess.check_age_end():
        is_extra_turn = sess.make_turn(cur_player) 
        while is_extra_turn and not sess.check_age_end():
            is_extra_turn = sess.make_turn(cur_player) 
        
        if sess.check_war_victory(cur_player):
            return 1
        if sess.check_science_victory(cur_player):
            return 2
        
        turn_friendly = not turn_friendly
        if turn_friendly: cur_player = good_player
        else: cur_player = opponent

    return 3


sessions_count = 100_000
sum = 0
start = time()
results = {1: 0, 2: 0, 3: 0}
for i in range(sessions_count):
    results[single_game()] += 1 


print(results[1] / sessions_count, results[2] / sessions_count, results[3] / sessions_count)
print( results[2])
print(time() - start)
