from resources import CardStatus, ScienceTokens
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
    [(cklad_kamnei, CardStatus.CAN_BE_TAKEN), (cklad_glini, CardStatus.CAN_BE_TAKEN), (cklad_drevesini, CardStatus.CAN_BE_TAKEN),
                    (lesopoval, CardStatus.CAN_BE_TAKEN), (konushna, CardStatus.CAN_BE_TAKEN), (taverna, CardStatus.CAN_BE_TAKEN)],
        
        [(stekl_masterskaia, CardStatus.LOCKED), (masterskaia, CardStatus.LOCKED), (None, CardStatus.LOCKED), (None, CardStatus.LOCKED), (None, CardStatus.LOCKED)],
            [(apteka, CardStatus.LOCKED), (bani, CardStatus.LOCKED), (altar, CardStatus.LOCKED), (glin_carier, CardStatus.LOCKED)],
                  [(None, CardStatus.LOCKED), (None, CardStatus.LOCKED), (None, CardStatus.LOCKED)],
                        [(carier, CardStatus.LOCKED), (lesopozagatovka, CardStatus.LOCKED)],
])

def single_game():
    good_player = Player(
        current_money=7,
        available_wonders=[
            visachie_sadi,
            bolshoi_sphinks,
            artemis_hram,
            pirei,
        ],
        built_wonders=[
        ],
        science_tokens=[],
        cards=[
        ]
    )
    opponent = Player(
        current_money=7,
        available_wonders=[
            koloss_rodosski,
            zeus_statue,
            bolshoi_zirk,
            alexandriskaia_bibl,
        ],
        built_wonders=[
        ],
        science_tokens=[],
        cards=[
        ]
    )

    good_player.set_opponent(opponent)
    opponent.set_opponent(good_player)

    first_table = deepcopy(first_table_original)

    sess = Session(good_player, opponent, first_table, [
        ScienceTokens.ARCHITECTURE, ScienceTokens.AGRICULTURE, ScienceTokens.ECONOMY, ScienceTokens.LAW, ScienceTokens.MASONRY
    ], war_status=0)

    turn_friendly = True
    cur_player = good_player
    while not sess.check_age_end():
        is_extra_turn = sess.make_turn(cur_player) 
        while is_extra_turn and not sess.check_age_end():
            is_extra_turn = sess.make_turn(cur_player) 
        
        if sess.check_war_victory(cur_player):
            return (cur_player is good_player, sess.first_action)
        if sess.check_science_victory(cur_player):
            return (cur_player is good_player, sess.first_action)

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
            return (cur_player is good_player, sess.first_action)
        if sess.check_science_victory(cur_player):
            return (cur_player is good_player, sess.first_action)

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
            return (cur_player is good_player, sess.first_action)
        if sess.check_science_victory(cur_player):
            return (cur_player is good_player, sess.first_action)

        turn_friendly = not turn_friendly
        if turn_friendly: cur_player = good_player
        else: cur_player = opponent
    
    return (sess.calculate_win_points(good_player) > sess.calculate_win_points(opponent), sess.first_action)


sessions_count = 15_000
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
