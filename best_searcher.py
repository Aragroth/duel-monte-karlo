from resources import ScienceTokens
from player import Player
from session import Session
from table import FirstAgeTable, SecondAgeTable, ThirdAgeTable

from wonder import *
from cards.first_age import *
from cards.second_age import second_age_cards
from cards.third_age import third_age_cards, third_age_gilds

import random
from time import time
from copy import deepcopy

first_table_original = FirstAgeTable(1, first_age_cards)
first_table_original.set_layout([
    [cklad_kamnei, cklad_glini, cklad_drevesini, lesopoval, glin_carier, taverna],
        [None, None, None, None, None],
          [apteka, bani, altar, masterskaia],
            [None, None, None],
               [carier, lesopozagatovka],
])

def single_game():
    good_player = Player(available_wonders=[
        koloss_rodosski,
        zeus_statue,
        bolshoi_zirk,
        mausalei
    ])
    opponent = Player(available_wonders=[
        artemis_hram,
        pirei,
        visachie_sadi,
        bolshoi_sphinks
    ])

    good_player.set_opponent(opponent)
    opponent.set_opponent(good_player)

    first_table = deepcopy(first_table_original)

    sess = Session(good_player, opponent, first_table, [
        ScienceTokens.ARCHITECTURE, ScienceTokens.AGRICULTURE, ScienceTokens.ECONOMY, ScienceTokens.LAW, ScienceTokens.MASONRY
    ])

    turn_friendly = True
    cur_player = good_player
    while not sess.check_age_end():
        is_extra_turn = sess.make_turn(cur_player) 
        while is_extra_turn and not sess.check_age_end():
            is_extra_turn = sess.make_turn(cur_player) 
        
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
        
        turn_friendly = not turn_friendly
        if turn_friendly: cur_player = good_player
        else: cur_player = opponent

        if sess.check_war_victory(cur_player):
            return (cur_player is good_player, sess.first_action)
        if sess.check_science_victory(cur_player):
            return (cur_player is good_player, sess.first_action)

    
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
        
        turn_friendly = not turn_friendly
        if turn_friendly: cur_player = good_player
        else: cur_player = opponent

        if sess.check_war_victory(cur_player):
            return (cur_player is good_player, sess.first_action)
        if sess.check_science_victory(cur_player):
            return (cur_player is good_player, sess.first_action)
    
    return (sess.calculate_win_points(good_player) > sess.calculate_win_points(opponent), sess.first_action)


sessions_count = 10_000
sum = 0
result = {}
start = time()
for i in range(sessions_count):
    local_res = single_game()
    if local_res[1] not in result:
        result[local_res[1]] = (local_res[0], 1)  
    else:
        result[local_res[1]] = (result[local_res[1]][0] + local_res[0], result[local_res[1]][1] + 1)  

print(len(result))
res_final = [(key, result[key][0] / result[key][1]) for key in result]
for elem in sorted(res_final, key=lambda x: x[1], reverse=True):
    print(elem[0][0].name, elem[0][1], '-', elem[1])

print(time() - start)
