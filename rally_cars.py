from strenum import StrEnum

class RallyClasses(StrEnum):
    H1              = "Historic Rally H1 (FWD)",
    H2_FWD          = "Historic Rally H2 (FWD)",
    H2_RWD          = "Historic Rally H2 (RWD)",
    F2_KIT_CAR      = "F2 Kit Car",
    H3              = "Historic Rally H3 (RWD)",
    B_4WD           = "Historic Rally Group B (4WD)",
    B_RWD           = "Historic Rally Group B (RWD)",
    A               = "Modern Rally Group A",
    GT              = "Modern Rally GT",
    R2              = "Modern Rally R2",
    NR4_R4          = "Modern Rally NR4/R4",
    n_2000CC        = "Up to 2000cc (4WD)",
    R5              = "Modern Rally R5"

RALLY_CLASSES = [
    RallyClasses.H1,
    RallyClasses.H2_FWD,
    RallyClasses.H2_RWD,
    RallyClasses.F2_KIT_CAR,
    RallyClasses.H3,
    RallyClasses.B_4WD,
    RallyClasses.B_RWD,
    RallyClasses.A,
    RallyClasses.GT,
    RallyClasses.R2,
    RallyClasses.NR4_R4,
    RallyClasses.n_2000CC,
    RallyClasses.R5
]

RALLY_CLASSES_CARS = {
    RallyClasses.H1: [
        "Citroen DS 21",
        "Lancia Fulvia HF",
        "Mini Cooper S"
    ],

    RallyClasses.H2_FWD: [
 	    "Peugeot 205 GTI",
        "Volkswagen Golf GTI 16V"
    ],

    RallyClasses.H2_RWD: [
        "Fiat 131 Abarth Rally",
        "Ford Escort Mk II",
        "Opel Kadett C GT/E",
        "Alpine Renault A110 1600 S"
    ],

    RallyClasses.F2_KIT_CAR: [
        "Peugeot 306 Maxi Kit Car",
        "Seat Ibiza Kit Car",
        "Volkswagen Golf GTI Mk 4 Kit Car"
    ],

    RallyClasses.H3: [
        "BMW E30 M3 Evo Rally",
        "Datsun 240Z",
        "Ford Sierra Cosworth RS500",
        "Lancia Stratos",
        "Opel Ascona 400",
        "Renault 5 Turbo"
    ],

    RallyClasses.B_4WD: [
        "Audi Sport quattro S1 E2",
        "Ford RS200",
        "Lancia Delta S4",
        "MG Metro 6R4",
        "Peugeot 205 T16 Evo 2"
    ],

    RallyClasses.B_RWD: [
        "BMW M1 Procar Rally",
        "Lancia 037 Evo 2",
        "Opel Manta 400",
        "Porsche 911 SC RS"
    ],

    RallyClasses.A: [
        "Ford Escort RS Cosworth",
        "Lancia Delta HF Integrale",
        "SUBARU Impreza 1995",
        "Mitsubishi Lancer Evolution VI",
        "SUBARU Impreza RS"
    ],

    RallyClasses.GT: [
        "Aston Martin V8 Vantage GT4",
        "BMW M2 Competition",
        "Chevrolet Camaro GT4.R",
        "Ford Mustang GT4",
        "Porsche 911 RGT Rally spec"
    ],

    RallyClasses.R2: [
        "Ford Fiesta R2",
        "Opel Adam R2",
        "Peugeot 208 R2"
    ],

    RallyClasses.NR4_R4: [
        "Mitsubishi Lancer Evolution X",
        "SUBARU WRX STI NR4"
    ],

    RallyClasses.n_2000CC: [
        "Citroen C4 Rally",
        "Ford Focus RS Rally 2001",
        "Ford Focus RS Rally 2007",
        "Peugeot 206 Rally",
        "Skoda Fabia Rally 2005",
        "SUBARU Impreza",
        "SUBARU Impreza 2001",
        "SUBARU Impreza S4 Rally 2008"
    ],

    RallyClasses.R5: [
        "Citroen C3 R5",
        "Ford Fiesta R5",
        "Mitsubishi Space Star R5",
        "Peugeot 208 T16 R5",
        "Skoda Fabia R5",
        "Volkswagen Polo GTI R5"
    ]
}