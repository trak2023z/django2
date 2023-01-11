from django_enumfield import enum

class AnnouncementsCategories(enum.Enum):
    BUY = 0
    SELL = 1
    FREE = 2
    EXCHANGE = 3

    __labels__ ={
        BUY: "Kupię",
    SELL: "Sprzedam",
    FREE: "Oddam",
    EXCHANGE: "Wymienię"
    }