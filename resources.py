import enum

class Resource(enum.Enum):
    CLAY = 1
    WOOD = 2
    STONE = 3
    GLASS = 4
    PAPYRUS = 5

    def __str__(self):
        return self.name


class CardStatus(enum.Enum):
    LOCKED = 1
    CAN_BE_TAKEN = 2
    TAKEN = 3

    def __str__(self):
        return self.name


class CardStateKnown(enum.Enum):
    KNOWN = 1
    UNKNOWN = 2

    def __str__(self):
        return self.name


class CardColor(enum.Enum):
    GREY = 1
    BROWN = 2
    YELLOW = 3
    RED = 4
    GREEN = 5
    PURPLE = 6
    BLUE = 7

    def __str__(self):
        return self.name


class ScienceSymbol(enum.Enum):
    GLOBUS = 1
    VESI = 2
    CLOCK = 3
    STUPKA = 4
    MAIATNIK = 5
    INK = 6
    WHEEL = 7

    def __str__(self):
        return self.name


class ScienceTokens(enum.Enum):
    AGRICULTURE = 1
    ARCHITECTURE = 2
    ECONOMY = 3
    LAW = 4
    MASONRY = 5
    MATHEMATICS = 6
    PHILOSOPHY = 7
    STRATEGY = 8
    THEOLOGY = 9
    URBANISM = 10

    def __str__(self):
        return self.name