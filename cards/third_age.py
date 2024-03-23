from card import Card
from resources import CardColor, Resource, ScienceSymbol

from cards.first_age import chastocol, taverna
from cards.second_age import strelbishe, ploshad, shcola, laboratoria, statua, chram, tribuna, pivovarna


def wonder_preaction(player):
    player.current_money += len(player.built_wonders) * 2

def grey_preaction(player):
    player.current_money += len([card for card in player.cards if card.color is CardColor.GREY]) * 3

def brown_preaction(player):
    player.current_money += len([card for card in player.cards if card.color is CardColor.BROWN]) * 2

def yellow_preaction(player):
    player.current_money += len([card for card in player.cards if card.color is CardColor.YELLOW]) * 1

def red_preaction(player):
    player.current_money += len([card for card in player.cards if card.color is CardColor.RED]) * 1

def gild_science_preaction(player):
    green_player = len([card for card in player.cards if card.color is CardColor.GREEN])
    green_opponent = len([card for card in player.opponent.cards if card.color is CardColor.GREEN])

    player.current_money += max(green_player, green_opponent) * 1

def gild_sailors_preaction(player):
    cards_player = len([card for card in player.cards if card.color in [CardColor.BROWN, CardColor.GREY]])
    cards_opponent = len([card for card in player.opponent.cards if card.color  in [CardColor.BROWN, CardColor.GREY]])

    player.current_money += max(cards_player, cards_opponent) * 1

def gild_shoppers_preaction(player):
    yellow_player = len([card for card in player.cards if card.color is CardColor.YELLOW])
    yellow_opponent = len([card for card in player.opponent.cards if card.color is CardColor.YELLOW])

    player.current_money += max(yellow_player, yellow_opponent) * 1

def gild_cort_preaction(player):
    blue_player = len([card for card in player.cards if card.color is CardColor.BLUE])
    blue_opponent = len([card for card in player.opponent.cards if card.color is CardColor.BLUE])

    player.current_money += max(blue_player, blue_opponent) * 1

def gild_tactics_preaction(player):
    red_player = len([card for card in player.cards if card.color is CardColor.RED])
    red_opponent = len([card for card in player.opponent.cards if card.color is CardColor.RED])

    player.current_money += max(red_player, red_opponent) * 1


def gild_builders_endgame(player):
    first = len(player.built_wonders)
    second = len(player.opponent.built_wonders)
    return max(first, second) * 2

def gild_money_endgame(player):
    first = player.current_money
    second = player.opponent.current_money
    return max(first, second) * 1

def gild_science_endgame(player):
    green_player = len([card for card in player.cards if card.color is CardColor.GREEN])
    green_opponent = len([card for card in player.opponent.cards if card.color is CardColor.GREEN])

    return max(green_player, green_opponent) * 2

def gild_sailors_endgame(player):
    cards_player = len([card for card in player.cards if card.color in [CardColor.BROWN, CardColor.GREY]])
    cards_opponent = len([card for card in player.opponent.cards if card.color  in [CardColor.BROWN, CardColor.GREY]])

    return max(cards_player, cards_opponent) * 1

def gild_shoppers_endgame(player):
    yellow_player = len([card for card in player.cards if card.color is CardColor.YELLOW])
    yellow_opponent = len([card for card in player.opponent.cards if card.color is CardColor.YELLOW])

    return max(yellow_player, yellow_opponent) * 1

def gild_cort_endgame(player):
    blue_player = len([card for card in player.cards if card.color is CardColor.BLUE])
    blue_opponent = len([card for card in player.opponent.cards if card.color is CardColor.BLUE])

    return max(blue_player, blue_opponent) * 1

def gild_tactics_endgame(player):
    red_player = len([card for card in player.cards if card.color is CardColor.RED])
    red_opponent = len([card for card in player.opponent.cards if card.color is CardColor.RED])

    return max(red_player, red_opponent) * 1



arsenal = Card(
    title='Арсенал', color=CardColor.RED, attack_power=3,
    resources_cost=[Resource.CLAY, Resource.CLAY, Resource.CLAY, Resource.WOOD, Resource.WOOD],
)

shtab = Card(
    title='Штаб', color=CardColor.RED, attack_power=3, money_cost=8
)

akademia = Card(
    title='Академия', color=CardColor.GREEN, culture_points=3, science_symbol=ScienceSymbol.CLOCK,
    resources_cost=[Resource.STONE, Resource.WOOD, Resource.GLASS, Resource.GLASS],
)

studia = Card(
    title='Студия', color=CardColor.GREEN, culture_points=3, science_symbol=ScienceSymbol.CLOCK,
    resources_cost=[Resource.WOOD, Resource.WOOD, Resource.GLASS, Resource.PAPYRUS],
)

torgovaia_palata = Card(
    title='Торговая палата', color=CardColor.YELLOW, culture_points=3,
    resources_cost=[Resource.PAPYRUS, Resource.PAPYRUS], preaction=grey_preaction
)

port = Card(
    title='Порт', color=CardColor.YELLOW, culture_points=3,
    resources_cost=[Resource.WOOD, Resource.GLASS, Resource.PAPYRUS], preaction=brown_preaction
)

orusinaia = Card(
    title='Оружейная', color=CardColor.YELLOW, culture_points=3,
    resources_cost=[Resource.STONE, Resource.STONE, Resource.GLASS], preaction=red_preaction
)

dvorez = Card(
    title='Дворец', color=CardColor.BLUE, culture_points=7,
    resources_cost=[Resource.CLAY, Resource.STONE, Resource.WOOD, Resource.GLASS, Resource.GLASS],
)

ratusha = Card(
    title='Ратуша', color=CardColor.BLUE, culture_points=7,
    resources_cost=[Resource.STONE, Resource.STONE, Resource.STONE, Resource.WOOD, Resource.WOOD],
)

obelisk = Card(
    title='Обелиск', color=CardColor.BLUE, culture_points=5,
    resources_cost=[Resource.STONE, Resource.STONE, Resource.GLASS],
)

ukreplenia = Card(
    title='Укрепления', color=CardColor.RED, attack_power=2, prev_card=chastocol,
    resources_cost=[Resource.STONE, Resource.STONE, Resource.CLAY, Resource.PAPYRUS],
)

osadnaia_masterskaia = Card(
    title='Осадная мастерская', color=CardColor.RED, attack_power=2, prev_card=strelbishe,
    resources_cost=[Resource.STONE, Resource.STONE, Resource.CLAY, Resource.PAPYRUS],
)

ippodrom = Card(
    title='Ипподром', color=CardColor.RED, attack_power=2, prev_card=ploshad,
    resources_cost=[Resource.CLAY, Resource.CLAY, Resource.STONE, Resource.STONE],
)


universitet = Card(
    title='Университет', color=CardColor.GREEN, culture_points=2,
    resources_cost=[Resource.CLAY, Resource.GLASS, Resource.PAPYRUS],
    science_symbol=ScienceSymbol.GLOBUS, prev_card=shcola
)

observatoria = Card(
    title='Обсерватория', color=CardColor.GREEN, culture_points=2,
    resources_cost=[Resource.STONE, Resource.PAPYRUS, Resource.PAPYRUS],
    science_symbol=ScienceSymbol.GLOBUS, prev_card=laboratoria
)

sadi = Card(
    title='Сады', color=CardColor.BLUE, culture_points=6,
    resources_cost=[Resource.CLAY, Resource.CLAY, Resource.WOOD, Resource.WOOD], prev_card=statua
)

panteon = Card(
    title='Пантеон', color=CardColor.BLUE, culture_points=6,
    resources_cost=[Resource.CLAY, Resource.WOOD, Resource.PAPYRUS, Resource.PAPYRUS], prev_card=chram
)

senat = Card(
    title='Сенат', color=CardColor.BLUE, culture_points=5,
    resources_cost=[Resource.CLAY, Resource.CLAY, Resource.STONE, Resource.PAPYRUS], prev_card=tribuna
)

maiak = Card(
    title='Майак', color=CardColor.YELLOW, culture_points=3, preaction=yellow_preaction,
    resources_cost=[Resource.CLAY, Resource.CLAY, Resource.GLASS], prev_card=taverna
)

arena = Card(
    title='Арена', color=CardColor.YELLOW, culture_points=3, preaction=wonder_preaction,
    resources_cost=[Resource.CLAY, Resource.STONE, Resource.WOOD], prev_card=pivovarna
)

gildia_torgovcev = Card(
    title='Гильдия торговцев', color=CardColor.PURPLE,
    preaction=gild_shoppers_preaction, endgame_action=gild_shoppers_endgame,
    resources_cost=[Resource.CLAY, Resource.WOOD, Resource.GLASS, Resource.PAPYRUS]
)

gildia_sudovladelcev = Card(
    title='Гильдия судовладельцев', color=CardColor.PURPLE,
    preaction=gild_sailors_preaction, endgame_action=gild_sailors_endgame,
    resources_cost=[Resource.CLAY, Resource.STONE, Resource.GLASS, Resource.PAPYRUS]
)

gildia_stroitelei = Card(
    title='Гильдия строителей', color=CardColor.PURPLE,
    endgame_action=gild_builders_endgame,
    resources_cost=[Resource.STONE, Resource.STONE, Resource.CLAY, Resource.WOOD, Resource.GLASS]
)

gildia_sudei = Card(
    title='Гильдия судей', color=CardColor.PURPLE,
    preaction=gild_cort_preaction, endgame_action=gild_cort_endgame,
    resources_cost=[Resource.WOOD, Resource.WOOD, Resource.CLAY, Resource.PAPYRUS]
)

gildia_uchenix = Card(
    title='Гильдия учёных', color=CardColor.PURPLE,
    preaction=gild_science_preaction, endgame_action=gild_science_endgame,
    resources_cost=[Resource.CLAY, Resource.CLAY, Resource.WOOD, Resource.WOOD]
)

gildia_rostovchikov = Card(
    title='Гильдия ростовщиков', color=CardColor.PURPLE,
    endgame_action=gild_money_endgame,
    resources_cost=[Resource.STONE, Resource.STONE, Resource.WOOD, Resource.WOOD]
)

gildia_strategov = Card(
    title='Гильдия стратегов', color=CardColor.PURPLE,
    preaction=gild_tactics_preaction, endgame_action=gild_tactics_endgame,
    resources_cost=[Resource.STONE, Resource.STONE, Resource.CLAY, Resource.PAPYRUS]
)


third_age_cards = [
    arsenal,
    shtab,
    akademia,
    studia,
    torgovaia_palata,
    port,
    orusinaia,
    dvorez,
    ratusha,
    obelisk,
    ukreplenia,
    osadnaia_masterskaia,
    ippodrom,
    universitet,
    observatoria,
    sadi,
    panteon,
    senat,
    maiak,
    arena,
]

third_age_gilds = [
    gildia_torgovcev,
    gildia_sudovladelcev,
    gildia_stroitelei,
    gildia_sudei,
    gildia_uchenix,
    gildia_rostovchikov,
    gildia_strategov,
]