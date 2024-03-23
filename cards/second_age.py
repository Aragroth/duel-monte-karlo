from card import Card
from resources import CardColor, Resource, ScienceSymbol

from cards.first_age import konushna, garnizon, skriptori, lavka_travnika, teatr, altar, bani


lesopilka = Card(
    title='Лесопилка', color=CardColor.BROWN, money_cost=2,
    resources_generated=[Resource.WOOD, Resource.WOOD],
)

kirpichnoe_proizv = Card(
    title='Кирпичное производство', color=CardColor.BROWN, money_cost=2,
    resources_generated=[Resource.CLAY, Resource.CLAY],
)

dobicha_kamna = Card(
    title='Добича камня', color=CardColor.BROWN, money_cost=2,
    resources_generated=[Resource.STONE, Resource.STONE],
)

masterskaia_stekloduva = Card(
    title='Мастерская стеклодува', color=CardColor.GREY,
    resources_generated=[Resource.GLASS],
)

suhilnaia_komnata = Card(
    title='Сушильная комната', color=CardColor.GREY,
    resources_generated=[Resource.PAPYRUS],
)

steni = Card(
    title='Сторожевая вышка', color=CardColor.RED, attack_power=2,
    resources_cost=[Resource.STONE, Resource.STONE]
)

forum = Card(
    title='Форум', color=CardColor.YELLOW, money_cost=3,
    resources_generated=[[Resource.GLASS, Resource.PAPYRUS]],
    resources_cost=[Resource.CLAY], 
)

karavan_sarai = Card(
    title='Караван-сарай', color=CardColor.YELLOW, money_cost=2,
    resources_cost=[Resource.GLASS, Resource.PAPYRUS],
    resources_generated=[[Resource.WOOD, Resource.CLAY, Resource.STONE]] 
)

tamosna = Card(
    title='Таможня', color=CardColor.YELLOW, money_cost=4,
    resources_reduced_cost=[Resource.PAPYRUS, Resource.GLASS],
)

sud = Card(
    title='Суд', color=CardColor.BLUE, culture_points=5,
    resources_cost=[Resource.WOOD, Resource.WOOD, Resource.GLASS],
)

konevodstvo = Card(
    title='Коневодство', color=CardColor.RED, attack_power=1,
    resources_cost=[Resource.CLAY, Resource.WOOD], prev_card=konushna
)

kazarmi = Card(
    title='Казармы', color=CardColor.RED, attack_power=1, money_cost=3,
    prev_card=garnizon
)

strelbishe = Card(
    title='Стрельбище', color=CardColor.RED, attack_power=2,
    resources_cost=[Resource.STONE, Resource.WOOD, Resource.PAPYRUS], 
)

ploshad = Card(
    title='Площадь', color=CardColor.RED, attack_power=2,
    resources_cost=[Resource.CLAY, Resource.CLAY, Resource.GLASS], 
)

biblioteka = Card(
    title='Библиотека', color=CardColor.GREEN, culture_points=2,
    resources_cost=[Resource.STONE, Resource.WOOD, Resource.GLASS],
    science_symbol=ScienceSymbol.INK, prev_card=skriptori
)

lazaret = Card(
    title='Лазарет', color=CardColor.GREEN, culture_points=2,
    resources_cost=[Resource.CLAY, Resource.CLAY, Resource.STONE],
    science_symbol=ScienceSymbol.STUPKA, prev_card=lavka_travnika
)

shcola = Card(
    title='Школа', color=CardColor.GREEN, culture_points=1,
    resources_cost=[Resource.WOOD, Resource.PAPYRUS, Resource.PAPYRUS],
    science_symbol=ScienceSymbol.WHEEL,
)

laboratoria = Card(
    title='Лаборатория', color=CardColor.GREEN, culture_points=1,
    resources_cost=[Resource.WOOD, Resource.GLASS, Resource.GLASS],
    science_symbol=ScienceSymbol.MAIATNIK,
)

statua = Card(
    title='Статуя', color=CardColor.BLUE, culture_points=4,
    resources_cost=[Resource.CLAY, Resource.CLAY], prev_card=teatr
)

chram = Card(
    title='Храм', color=CardColor.BLUE, culture_points=4,
    resources_cost=[Resource.WOOD, Resource.PAPYRUS], prev_card=altar
)

akveduk = Card(
    title='Акведук', color=CardColor.BLUE, culture_points=5,
    resources_cost=[Resource.STONE, Resource.STONE, Resource.STONE],  prev_card=bani
)

tribuna = Card(
    title='Трибуна', color=CardColor.BLUE, culture_points=4,
    resources_cost=[Resource.STONE, Resource.WOOD]
)

pivovarna = Card(
    title='Пивоварня', color=CardColor.YELLOW, money_gives=6
)

second_age_cards = [
    lesopilka,
    kirpichnoe_proizv,
    dobicha_kamna,
    masterskaia_stekloduva,
    suhilnaia_komnata,
    steni,
    forum,
    karavan_sarai,
    tamosna,
    sud,
    konevodstvo,
    kazarmi,
    strelbishe,
    ploshad,
    biblioteka,
    lazaret,
    shcola,
    laboratoria,
    statua,
    chram,
    akveduk,
    tribuna,
    pivovarna
]

