class Card:
    def __init__(self, title, color, resources_cost=None, attack_power=0,  culture_points=0, endgame_action=None,
                resources_generated=None, resources_reduced_cost=None, money_cost=0, money_gives=0,  preaction=None,
                prev_card=None, science_symbol=None
        ) -> None:
        self.title = title
        self.color = color

        self.money_gives = money_gives
        self.money_cost = money_cost
        self.resources_cost = [] if resources_cost is None else resources_cost

        self.attack_power = attack_power
        self.culture_points = culture_points
        self.science_symbol = science_symbol

        self.preaction = preaction
        self.endgame_action = endgame_action
        
        self.resources_generated = [] if resources_generated is None else resources_generated
        self.resources_reduced_cost = [] if resources_reduced_cost is None else resources_reduced_cost

        self.prev_card = prev_card  

    def __str__(self) -> str:
        return self.title
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Card):
            return self.title == other.title
        return False
    
    def __hash__(self):
        return hash(self.title)