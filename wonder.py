from resources import Resource, CardColor


class Wonder:
    def __init__(self, title: str, resources_cost=None, can_give_resource=None, culture_points=0,
                 extra_turn=False, money_gives=0, destroy_card_color=None, removes_money_opponent=0,
                 attack_points=0, get_science_token=False, build_deleted_card=False) -> None:
        self.title: str = title
        self.resources_cost: list[Resource] = [] if resources_cost is None else resources_cost
        self.can_give_resource: list[Resource] = [] if can_give_resource is None else can_give_resource
        self.culture_points: int = culture_points
        self.extra_turn: bool = extra_turn
        self.money_gives: int = money_gives
        self.destroy_card_color: CardColor | None = destroy_card_color
        self.removes_money_opponent = removes_money_opponent
        self.attack_points = attack_points
        self.get_science_token = get_science_token
        self.build_deleted_card = build_deleted_card

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return str(self)
    

appieva_doroga = Wonder(
    title='Аппиева дорога',
    money_gives=3, removes_money_opponent=3, extra_turn=True, culture_points=3,
    resources_cost=[Resource.PAPYRUS, Resource.CLAY, Resource.CLAY, Resource.STONE, Resource.STONE] 
)

bolshoi_zirk = Wonder(
    title="Большой цирк", culture_points=3, attack_points=1, destroy_card_color=CardColor.GREY,
    resources_cost=[Resource.GLASS, Resource.WOOD, Resource.STONE, Resource.STONE] 
)

koloss_rodosski = Wonder(
    title='Колосс родосский',
    attack_points=2, culture_points=3,
    resources_cost=[Resource.GLASS, Resource.CLAY, Resource.CLAY, Resource.CLAY] 
)

alexandriskaia_bibl = Wonder(
    title='Александрийская библиотека',
     culture_points=4, get_science_token=True,
    resources_cost=[Resource.PAPYRUS, Resource.GLASS, Resource.WOOD, Resource.WOOD, Resource.WOOD] 
)

aleksandr_maiak = Wonder(
    title="Александрийский маяк", culture_points=4,
    can_give_resource=[Resource.WOOD, Resource.STONE, Resource.CLAY],
    resources_cost=[Resource.PAPYRUS, Resource.PAPYRUS, Resource.STONE, Resource.WOOD] 
)

visachie_sadi = Wonder(
    title="Висячие сады семирамиды", culture_points=3, extra_turn=True, money_gives=6,
    resources_cost=[Resource.PAPYRUS, Resource.GLASS, Resource.WOOD, Resource.WOOD] 
)

mausalei = Wonder(
    title="Мавзолей в Галикарнасе", culture_points=2, build_deleted_card=True,
    resources_cost=[Resource.PAPYRUS, Resource.GLASS, Resource.GLASS, Resource.CLAY, Resource.CLAY] 
)

pirei = Wonder(
    title="Пирей", culture_points=2, extra_turn=True,
    can_give_resource=[Resource.PAPYRUS, Resource.GLASS],
    resources_cost=[Resource.CLAY, Resource.STONE, Resource.WOOD, Resource.WOOD] 
)

piramid_heopsa = Wonder(
    title="Пирамида хеопса", culture_points=9,
    resources_cost=[Resource.PAPYRUS, Resource.STONE, Resource.STONE, Resource.STONE] 
)

bolshoi_sphinks = Wonder(
    title="Большой сфинкс", culture_points=6, extra_turn=True,
    resources_cost=[Resource.GLASS, Resource.GLASS, Resource.CLAY, Resource.STONE] 
)

zeus_statue = Wonder(
    title="Статуя Зевса", destroy_card_color=CardColor.BROWN, attack_points=1, culture_points=3,
    resources_cost=[Resource.PAPYRUS, Resource.PAPYRUS, Resource.CLAY, Resource.WOOD, Resource.STONE] 
)

artemis_hram = Wonder(
    title="Храм артемиды", money_gives=12, extra_turn=True,
    resources_cost=[Resource.PAPYRUS, Resource.GLASS, Resource.STONE, Resource.WOOD] 
)

all_wonders = [
    appieva_doroga,
    bolshoi_zirk,
    koloss_rodosski,
    alexandriskaia_bibl,
    aleksandr_maiak,
    visachie_sadi,
    mausalei,
    pirei,
    piramid_heopsa,
    bolshoi_sphinks,
    zeus_statue,
    artemis_hram,
]