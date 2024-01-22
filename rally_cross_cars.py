from strenum import StrEnum

class RallyClasses(StrEnum):
    CROSSKARTS      = "Crosskarts",
    SUPER_1600      = "Super 1600",
    LITES           = "Lites",
    GROUP_B         = "Group B",
    SUPERCARS       = "Supercars",
    SUPERCARS_2019  = "Supercars 2019"

RALLY_CLASSES = [
    RallyClasses.CROSSKARTS,
    RallyClasses.SUPER_1600,
    RallyClasses.LITES,
    RallyClasses.GROUP_B,
    RallyClasses.SUPERCARS,
    RallyClasses.SUPERCARS_2019
]

RALLY_CLASSES_CARS = {
    RallyClasses.CROSSKARTS: [
        "Speedcar Xtrem"
    ],

    RallyClasses.SUPER_1600: [
        "Opel Corsa Super 1600",
        "Renault Clio RS S1600",
        "Volkswagen Polo S1600"
    ],

    RallyClasses.LITES: [
        "Ford Fiesta OMSE SuperCar Lites"
    ],

    RallyClasses.GROUP_B: [
        "Lancia Delta S4 Rallycross",
        "Ford RS200 Evolution",
        "Peugeot 205 T16 Rallycross",
        "MG Metro 6R4 Rallycross"
    ],

    RallyClasses.SUPERCARS: [
        "Audi S1 EKS RX quattro",
        "Ford Fiesta Rallycross (Mk7)",
        "Ford Fiesta Rallycross (Mk8)",
        "Peugeot 208 WRX",
        "Renault Megane RS RX",
        "SUBARU WRX STI Rallycross",
        "Volkswagen Polo R Supercar"
    ],

    RallyClasses.SUPERCARS_2019: [
        "Renault Clio RS RX",
        "Renault Megane RS RX",
        "Ford Fiesta Rallycross (Mk8)",
        "Mini Cooper SX1",
        "Peugeot 208 WRX",
        "Ford Fiesta Rallycross (STARD)",
        "Ford Fiesta RXS Evo 5",
        "Audi S1 EKS RX quattro",
        "Seat Ibiza RX"
    ]
}