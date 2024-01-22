from strenum import StrEnum

class RallyLocations(StrEnum):
    ARGENTINA   = "Catamarca Province, Argentina",
    AUSTRALIA   = "Monaro, Australia",
    FINLAND     = "Jämsä, Finland",
    GERMANY     = "Baumholder, Germany",
    GREECE      = "Argolis, Greece",
    MONACO      = "Monte Carlo, Monaco",
    NEW_ZEALAND = "Hawkes Bay, New Zealand",
    POLLAND     = "Łęczna County, Poland",
    SCOTLAND    = "Perth and Kinross, Scotland",
    SPAIN       = "Ribadelles, Spain",
    SWEDEN      = "Värmland, Sweden",
    USA         = "New England, USA",
    WALES       = "Powys, Wales"

RALLY_LOCATIONS = [
    RallyLocations.ARGENTINA,
    RallyLocations.AUSTRALIA,
    RallyLocations.FINLAND,
    RallyLocations.GERMANY,
    RallyLocations.GREECE,
    RallyLocations.MONACO,
    RallyLocations.NEW_ZEALAND,
    RallyLocations.POLLAND,
    RallyLocations.SCOTLAND,
    RallyLocations.SPAIN,
    RallyLocations.SWEDEN,
    RallyLocations.USA,
    RallyLocations.WALES
]

RALLY_SUBLOCATIONS = {
    RallyLocations.ARGENTINA: [
        "Valle de los Puentes",
        "El Rodeo",
        "San Isidro",
        "Camino de Acantilados y Rocas",
        "Miraflores",
        "Huillaprima",
        "Camino a La Puerta",
        "La Merced",
        "Valle de los Puentes a la Inversa",
        "Las Juntas",
        "Camino de Acantilados y Rocas Inverso",
        "Camino a Coneta"
    ],

    RallyLocations.AUSTRALIA: [
        "Yambulla Mountain Descent",
        "Chandlers Creek",
        "Yambulla Mountain Ascent",
        "Noorinbee Ridge Ascent",
        "Rockton Plains",
        "Mount Kaye Pass Reverse",
        "Bondi Forest",
        "Mount Kaye Pass",
        "Rockton Plains Reverse",
        "Chandlers Creek Reverse"
    ],

    RallyLocations.FINLAND: [
        "Pitkäjärvi",
        "Kakaristo",
        "Iso Oksajärvi",
        "Naarajärvi",
        "Hämelahti",
        "Oksala",
        "Paskuri",
        "Järvenkylä",
        "Kotajärvi",
        "Kailajärvi",
        "Jyrkysjärvi",
        "Kontinjärvi"
    ],

    RallyLocations.GERMANY: [
        "Kreuzungsring reverse",
        "Innerer Feld-Sprint",
        "Ruschberg",
        "Oberstein",
        "Hammerstein",
        "Frauenberg",
        "Kreuzungsring",
        "Waldabstieg",
        "Verbundsring reverse",
        "Verbundsring",
        "Waldaufsteig",
        "Innerer Feld Sprint (Umgekehrt)"
    ],

    RallyLocations.GREECE: [
        "Koryfi Dafini",
        "Pomona Ekrixi",
        "Tsiristra Thea",
        "Ypsona tou Dasos",
        "Anodou Farmakas",
        "Ourea Spevsi",
        "Perasma Platani",
        "Ampelonas Ormi",
        "Abies Koilada",
        "Pedines Epidaxi"
        "Fourketa Kourva",
        "Kathodo Leontiou"
    ],

    RallyLocations.MONACO: [
        "Gordolon - Courte Montee",
        "Vallee Descendante",
        "Pra D'Alart",
        "Route de Turini Decente",
        "Route de Turini",
        "Col de Turini - Sprint en montee",
        "Col de Turini - Descente",
        "Col de Turini Depart",
        "Col de Turini - Depart en descente",
        "Col de Turini Sprint en descente",
        "Approache du Col de Turini Montee",
        "Route de Turini Montee"
    ],

    RallyLocations.NEW_ZEALAND: [
        "Waimara Sprint Reverse",
        "Waimara Point Forward",
        "Ocean Beach Sprint Reverse",
        "Te Awanga Sprint Reverse",
        "Elsthorpe Sprint Forward",
        "Eslthorpe Sprint Reverse",
        "Te Awanga Forward",
        "Ocean Beach Sprint",
        "Waimara Point Reverse",
        "Te Awanga Sprint Forward",
        "Waimara Sprint Forward",
        "Ocean Beach"
    ],

    RallyLocations.POLLAND: [
        "Zagorze",
        "Czarny Las",
        "Borysik",
        "Zienki",
        "Zaróbka",
        "Jagodno",
        "Kopina",
        "Józefin",
        "Jezioro Lukie",
        "Jezioro Rotcze",
        "Lejno",
        "Marynka"
    ],

    RallyLocations.SCOTLAND: [
        "South Morningside",
        "South Morningside Reverse",
        "Newhouse Bridge",
        "Newhouse Bridge Reverse",
        "Glencastle Farm",
        "Glencastle Farm Reverse",
        "Old Butterstone Muir",
        "Rosebank Farm Reverse",
        "Rosebank Farm",
        "Annbank Station Reverse",
        "Annbank Station",
        "Old Butterstone Muir Reverse"
    ],

    RallyLocations.SPAIN: [
        "Vinedos dentro del valle Parra",
        "Final en Bellriu",
        "Vinedos Dardenya inversa",
        "Vinedos Dardenya",
        "Comienzo en Bellriu",
        "Descento por carretera",
        "Camino a Centenera",
        "Centenera",
        "Ascenso por valle el Gualet",
        "Ascenso bosque Montevard",
        "Subida por Carretera",
        "Salida desde Montverd"
    ],

    RallyLocations.SWEDEN: [
        "Norraskoga",
        "Ostra Hinnsjon",
        "Lysvik",
        "Stor-Jangen Sprint",
        "Hamra",
        "Skogsrallyt",
        "Elgsjon",
        "Bjorklagen",
        "Älgsjön",
        "Älgsjön Sprint",
        "Ransbysater",
        "Stor-Jangen Sprint Reverse"
    ],

    RallyLocations.USA: [
        "North Fork Pass",
        "North Fork Pass Reverse",
        "Hancock Hill Sprint Reverse",
        "Hancock Creek Burst",
        "Hancock Hill Sprint Forward",
        "Fuller Mountain Descent",
        "Fuller Mountain Ascent",
        "Fury Lake Depart",
        "Beaver Creek Trail Forward",
        "Beaver Creek Trail Reverse",
        "Tolt Valley Sprint Forward",
        "Tolt Valley Sprint Reverse"
    ],

    RallyLocations.WALES: [
        "Geufron Forest",
        "Fferm Wynt Reverse",
        "Dyffryn Afon Reverse",
        "Dyffryn Afon",
        "Bronfelen",
        "Bidno Moorland",
        "Bidno Moorland Reverse",
        "Fferm Wynt",
        "Sweet Lamb",
        "River Severn Valley",
        "Pant Mawr",
        "Pant Mawr Reverse"
    ]
}