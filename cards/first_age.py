from card import Card
from resources import CardColor, Resource, ScienceSymbol

lesopoval = Card(
    title='Лесоповал', color=CardColor.BROWN,
    resources_generated=[Resource.WOOD]
)

lesopozagatovka = Card(
    title='Лесозаготовка', color=CardColor.BROWN, money_cost=1,
    resources_generated=[Resource.WOOD],
)

glin_carier = Card(
    title='Глиняный карьер', color=CardColor.BROWN,
    resources_generated=[Resource.CLAY],
)

carier = Card(
    title='Карьер', color=CardColor.BROWN, money_cost=1,
    resources_generated=[Resource.CLAY],
)

kamenolomna = Card(
    title='Каменоломня', color=CardColor.BROWN,
    resources_generated=[Resource.STONE],
)

kamen_barrier = Card(
    title='Каменный карьер', color=CardColor.BROWN, money_cost=1, 
    resources_generated=[Resource.STONE],
)

stekl_masterskaia = Card(
    title='Стекольная мастерская', color=CardColor.GREY, money_cost=1,
    resources_generated=[Resource.GLASS],
)

papir_masterskaia = Card(
    title='Папирусная мастерская', color=CardColor.GREY, money_cost=1,
    resources_generated=[Resource.PAPYRUS],
)

stroz_vishka = Card(
    title='Сторожевая вышка', color=CardColor.RED, attack_power=1,
)

masterskaia = Card(
    title='Мастерская', color=CardColor.GREEN, culture_points=1,
    science_symbol=ScienceSymbol.MAIATNIK,
    resources_cost=[Resource.PAPYRUS], 
)

apteka = Card(
    title='Аптека', color=CardColor.GREEN, culture_points=1,
    science_symbol=ScienceSymbol.WHEEL,
    resources_cost=[Resource.GLASS], 
)

cklad_kamnei = Card(
    title='Склад камней', color=CardColor.YELLOW, money_cost=3,
    resources_reduced_cost=[Resource.STONE],
)

cklad_glini = Card(
    title='Склад глины', color=CardColor.YELLOW, money_cost=3,
    resources_reduced_cost=[Resource.CLAY],
)

cklad_drevesini = Card(
    title='Склад древесины', color=CardColor.YELLOW, money_cost=3,
    resources_reduced_cost=[Resource.WOOD],
)

konushna = Card(
    title='Конюшня', color=CardColor.RED, attack_power=1,
    resources_cost=[Resource.WOOD], 
)

garnizon = Card(
    title='Гарнизон', color=CardColor.RED, attack_power=1,
    resources_cost=[Resource.CLAY], 
)

chastocol = Card(
    title='Частокол', color=CardColor.RED, money_cost=2, attack_power=1,
)

skriptori = Card(
    title='Скрипторий', color=CardColor.GREEN, money_cost=2,
    science_symbol=ScienceSymbol.INK,
)

lavka_travnika = Card(
    title='Лавка травника', color=CardColor.GREEN, money_cost=2,
    science_symbol=ScienceSymbol.STUPKA,
)

teatr = Card(
    title='Театр', color=CardColor.BLUE, culture_points=3,
)

altar = Card(
    title='Алтарь', color=CardColor.BLUE, culture_points=3,
)

bani = Card(
    title='Бани', color=CardColor.BLUE, culture_points=3, 
    resources_cost=[Resource.STONE], 
)

taverna = Card(
    title='Таверна', color=CardColor.YELLOW, culture_points=3,
    resources_cost=[Resource.STONE], 
    money_gives=4,
)


first_age_cards = [
    lesopoval,
    lesopozagatovka,
    glin_carier,
    carier,
    kamenolomna,
    kamen_barrier,
    stekl_masterskaia,
    papir_masterskaia,
    stroz_vishka,
    masterskaia,
    apteka,
    cklad_kamnei,
    cklad_glini,
    cklad_drevesini,
    konushna,
    garnizon,
    chastocol,
    skriptori,
    lavka_travnika,
    teatr,
    altar,
    bani,
    taverna
]

