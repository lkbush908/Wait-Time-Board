class Park:
    def __init__(self, name, liveURL, numID):
        self.name = name
        self.liveURL = liveURL
        self.numID = numID
        
    def __str__(self):
        return self.name


class Resort:
    def __init__(self, name, parks, numID):
        self.name = name
        self.parks = parks
        self.numID = numID
    def __str__(self):
        return self.name


Disneyland = Park("Disneyland Park", 'https://api.themeparks.wiki/v1/entity/7340550b-c14d-4def-80bb-acdb51d49a66/live', 1)
CaliAdventure = Park("Disney Calfornia Adventure", 'https://api.themeparks.wiki/v1/entity/832fcd51-ea19-4e77-85c7-75d5843b127c/live', 2)

DLRParks = [Disneyland, CaliAdventure]


MagicKingdom = Park("Magic Kingdom", 'https://api.themeparks.wiki/v1/entity/75ea578a-adc8-4116-a54d-dccb60765ef9/live', 1)
Epcot = Park("Epcot", 'https://api.themeparks.wiki/v1/entity/47f90d2c-e191-4239-a466-5892ef59a88b/live', 2)
HollyStudios = Park("Hollywood Studios", 'https://api.themeparks.wiki/v1/entity/288747d1-8b4f-4a64-867e-ea7c9b27bad8/live', 3)
AnimalKingdom = Park("Animal Kingdom", 'https://api.themeparks.wiki/v1/entity/1c84a229-8862-4648-9c71-378ddd2c7693/live', 4)

WDWParks = [MagicKingdom, Epcot, HollyStudios, AnimalKingdom]


DLR = Resort("Disneyland Resort", DLRParks, 1)
WDW = Resort("Walt Disney World", WDWParks, 2)


ResortOptions = [DLR, WDW]