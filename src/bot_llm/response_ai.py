from openai import OpenAI
from definitions import ROOT_DIR
import yaml
import os
import json
from dotenv import load_dotenv

import requests

load_dotenv() # Load environment variables from .env file
comunas = [
    {
      "idComuna": "44",
      "descripcion": "Algarrobo",
      "abreviacion": "AL"
    },
    {
      "idComuna": "301",
      "descripcion": "Alhue",
      "abreviacion": "AH"
    },
    {
      "idComuna": "347",
      "descripcion": "Alto Biobío",
      "abreviacion": "AB"
    },
    {
      "idComuna": "28",
      "descripcion": "Alto del Carmen",
      "abreviacion": "AC"
    },
    {
      "idComuna": "343",
      "descripcion": "Alto Hospicio",
      "abreviacion": "AH"
    },
    {
      "idComuna": "256",
      "descripcion": "Ancud",
      "abreviacion": "AN"
    },
    {
      "idComuna": "33",
      "descripcion": "Andacollo",
      "abreviacion": "AD"
    },
    {
      "idComuna": "197",
      "descripcion": "Angol",
      "abreviacion": "AG"
    },
    {
      "idComuna": "290",
      "descripcion": "Antártica",
      "abreviacion": "AC"
    },
    {
      "idComuna": "18",
      "descripcion": "Antofagasta",
      "abreviacion": "AN"
    },
    {
      "idComuna": "179",
      "descripcion": "Antuco",
      "abreviacion": "AT"
    },
    {
      "idComuna": "145",
      "descripcion": "Arauco",
      "abreviacion": "AR"
    },
    {
      "idComuna": "3",
      "descripcion": "Arica",
      "abreviacion": "AR"
    },
    {
      "idComuna": "272",
      "descripcion": "Aysén",
      "abreviacion": "AI"
    },
    {
      "idComuna": "309",
      "descripcion": "Buin",
      "abreviacion": "BU"
    },
    {
      "idComuna": "167",
      "descripcion": "Bulnes",
      "abreviacion": "BU"
    },
    {
      "idComuna": "53",
      "descripcion": "Cabildo",
      "abreviacion": "CB"
    },
    {
      "idComuna": "289",
      "descripcion": "Cabo de Hornos",
      "abreviacion": "CB"
    },
    {
      "idComuna": "175",
      "descripcion": "Cabrero",
      "abreviacion": "CE"
    },
    {
      "idComuna": "13",
      "descripcion": "Calama",
      "abreviacion": "CL"
    },
    {
      "idComuna": "255",
      "descripcion": "Calbuco",
      "abreviacion": "CL"
    },
    {
      "idComuna": "22",
      "descripcion": "Caldera",
      "abreviacion": "CD"
    },
    {
      "idComuna": "63",
      "descripcion": "Calera",
      "abreviacion": "CR"
    },
    {
      "idComuna": "307",
      "descripcion": "Calera de Tango",
      "abreviacion": "CT"
    },
    {
      "idComuna": "71",
      "descripcion": "Calle Larga",
      "abreviacion": "CL"
    },
    {
      "idComuna": "4",
      "descripcion": "Camarones",
      "abreviacion": "CM"
    },
    {
      "idComuna": "6",
      "descripcion": "Camiña",
      "abreviacion": "CA"
    },
    {
      "idComuna": "40",
      "descripcion": "Canela",
      "abreviacion": "CN"
    },
    {
      "idComuna": "149",
      "descripcion": "Cañete",
      "abreviacion": "CÑ"
    },
    {
      "idComuna": "210",
      "descripcion": "Carahue",
      "abreviacion": "CF"
    },
    {
      "idComuna": "47",
      "descripcion": "Cartagena",
      "abreviacion": "CG"
    },
    {
      "idComuna": "80",
      "descripcion": "Casablanca",
      "abreviacion": "CS"
    },
    {
      "idComuna": "259",
      "descripcion": "Castro",
      "abreviacion": "CA"
    },
    {
      "idComuna": "57",
      "descripcion": "Catemu",
      "abreviacion": "CT"
    },
    {
      "idComuna": "133",
      "descripcion": "Cauquenes",
      "abreviacion": "CF"
    },
    {
      "idComuna": "321",
      "descripcion": "Cerrillos",
      "abreviacion": "CE"
    },
    {
      "idComuna": "318",
      "descripcion": "Cerro Navia",
      "abreviacion": "CN"
    },
    {
      "idComuna": "267",
      "descripcion": "Chaitén",
      "abreviacion": "HT"
    },
    {
      "idComuna": "20",
      "descripcion": "Chañaral",
      "abreviacion": "CH"
    },
    {
      "idComuna": "132",
      "descripcion": "Chanco",
      "abreviacion": "CH"
    },
    {
      "idComuna": "113",
      "descripcion": "Chépica",
      "abreviacion": "CP"
    },
    {
      "idComuna": "196",
      "descripcion": "Chiguayante",
      "abreviacion": "CY"
    },
    {
      "idComuna": "276",
      "descripcion": "Chile Chico",
      "abreviacion": "CG"
    },
    {
      "idComuna": "161",
      "descripcion": "Chillán",
      "abreviacion": "CH"
    },
    {
      "idComuna": "172",
      "descripcion": "Chillán Viejo",
      "abreviacion": "CW"
    },
    {
      "idComuna": "114",
      "descripcion": "Chimbarongo",
      "abreviacion": "CM"
    },
    {
      "idComuna": "346",
      "descripcion": "Cholchol",
      "abreviacion": "CH"
    },
    {
      "idComuna": "262",
      "descripcion": "Chonchi",
      "abreviacion": "CK"
    },
    {
      "idComuna": "271",
      "descripcion": "Cisnes",
      "abreviacion": "CS"
    },
    {
      "idComuna": "152",
      "descripcion": "Cobquecura",
      "abreviacion": "CQ"
    },
    {
      "idComuna": "253",
      "descripcion": "Cochamó",
      "abreviacion": "MO"
    },
    {
      "idComuna": "277",
      "descripcion": "Cochrane",
      "abreviacion": "CX"
    },
    {
      "idComuna": "84",
      "descripcion": "Codegua",
      "abreviacion": "CD"
    },
    {
      "idComuna": "163",
      "descripcion": "Coelemu",
      "abreviacion": "CM"
    },
    {
      "idComuna": "162",
      "descripcion": "Coihueco",
      "abreviacion": "CC"
    },
    {
      "idComuna": "91",
      "descripcion": "Coinco",
      "abreviacion": "CI"
    },
    {
      "idComuna": "118",
      "descripcion": "Colbún",
      "abreviacion": "CO"
    },
    {
      "idComuna": "7",
      "descripcion": "Colchane",
      "abreviacion": "CE"
    },
    {
      "idComuna": "292",
      "descripcion": "Colina",
      "abreviacion": "CO"
    },
    {
      "idComuna": "199",
      "descripcion": "Collipulli",
      "abreviacion": "CP"
    },
    {
      "idComuna": "88",
      "descripcion": "Coltauco",
      "abreviacion": "CK"
    },
    {
      "idComuna": "39",
      "descripcion": "Combarbalá",
      "abreviacion": "CB"
    },
    {
      "idComuna": "190",
      "descripcion": "Concepción",
      "abreviacion": "CO"
    },
    {
      "idComuna": "326",
      "descripcion": "Conchalí",
      "abreviacion": "CH"
    },
    {
      "idComuna": "81",
      "descripcion": "Concón",
      "abreviacion": "CC"
    },
    {
      "idComuna": "137",
      "descripcion": "Constitución",
      "abreviacion": "CN"
    },
    {
      "idComuna": "150",
      "descripcion": "Contulmo",
      "abreviacion": "CT"
    },
    {
      "idComuna": "23",
      "descripcion": "Copiapó",
      "abreviacion": "CP"
    },
    {
      "idComuna": "32",
      "descripcion": "Coquimbo",
      "abreviacion": "CO"
    },
    {
      "idComuna": "191",
      "descripcion": "Coronel",
      "abreviacion": "CR"
    },
    {
      "idComuna": "234",
      "descripcion": "Corral",
      "abreviacion": "RL"
    },
    {
      "idComuna": "274",
      "descripcion": "Coyhaique",
      "abreviacion": "CI"
    },
    {
      "idComuna": "219",
      "descripcion": "Cunco",
      "abreviacion": "CU"
    },
    {
      "idComuna": "207",
      "descripcion": "Curacautín",
      "abreviacion": "CN"
    },
    {
      "idComuna": "297",
      "descripcion": "Curacaví",
      "abreviacion": "CU"
    },
    {
      "idComuna": "260",
      "descripcion": "Curaco de Vélez",
      "abreviacion": "CV"
    },
    {
      "idComuna": "146",
      "descripcion": "Curanilahue",
      "abreviacion": "CJ"
    },
    {
      "idComuna": "226",
      "descripcion": "Curarrehue",
      "abreviacion": "CD"
    },
    {
      "idComuna": "135",
      "descripcion": "Curepto",
      "abreviacion": "CJ"
    },
    {
      "idComuna": "127",
      "descripcion": "Curicó",
      "abreviacion": "CU"
    },
    {
      "idComuna": "258",
      "descripcion": "Dalcahue",
      "abreviacion": "DH"
    },
    {
      "idComuna": "21",
      "descripcion": "Diego de Almagro",
      "abreviacion": "DA"
    },
    {
      "idComuna": "89",
      "descripcion": "Doñihue",
      "abreviacion": "DÑ"
    },
    {
      "idComuna": "333",
      "descripcion": "El Bosque",
      "abreviacion": "EB"
    },
    {
      "idComuna": "169",
      "descripcion": "El Carmen",
      "abreviacion": "EC"
    },
    {
      "idComuna": "303",
      "descripcion": "El Monte",
      "abreviacion": "EM"
    },
    {
      "idComuna": "45",
      "descripcion": "El Quisco",
      "abreviacion": "EQ"
    },
    {
      "idComuna": "46",
      "descripcion": "El Tabo",
      "abreviacion": "ET"
    },
    {
      "idComuna": "143",
      "descripcion": "Empedrado",
      "abreviacion": "EM"
    },
    {
      "idComuna": "202",
      "descripcion": "Ercilla",
      "abreviacion": "ER"
    },
    {
      "idComuna": "338",
      "descripcion": "Estación Central",
      "abreviacion": "EC"
    },
    {
      "idComuna": "189",
      "descripcion": "Florida",
      "abreviacion": "FL"
    },
    {
      "idComuna": "218",
      "descripcion": "Freire",
      "abreviacion": "FR"
    },
    {
      "idComuna": "27",
      "descripcion": "Freirina",
      "abreviacion": "FR"
    },
    {
      "idComuna": "247",
      "descripcion": "Fresia",
      "abreviacion": "FS"
    },
    {
      "idComuna": "248",
      "descripcion": "Frutillar",
      "abreviacion": "FT"
    },
    {
      "idComuna": "268",
      "descripcion": "Futaleufú",
      "abreviacion": "FF"
    },
    {
      "idComuna": "236",
      "descripcion": "Futrono",
      "abreviacion": "FU"
    },
    {
      "idComuna": "208",
      "descripcion": "Galvarino",
      "abreviacion": "GV"
    },
    {
      "idComuna": "1",
      "descripcion": "General Lagos",
      "abreviacion": "GL"
    },
    {
      "idComuna": "222",
      "descripcion": "Gorbea",
      "abreviacion": "GB"
    },
    {
      "idComuna": "83",
      "descripcion": "Graneros",
      "abreviacion": "GR"
    },
    {
      "idComuna": "270",
      "descripcion": "Guaitecas",
      "abreviacion": "GT"
    },
    {
      "idComuna": "66",
      "descripcion": "Hijuelas",
      "abreviacion": "HI"
    },
    {
      "idComuna": "266",
      "descripcion": "Hualaihué",
      "abreviacion": "HH"
    },
    {
      "idComuna": "125",
      "descripcion": "Hualañe",
      "abreviacion": "HÑ"
    },
    {
      "idComuna": "344",
      "descripcion": "Hualpén",
      "abreviacion": "HP"
    },
    {
      "idComuna": "192",
      "descripcion": "Hualqui",
      "abreviacion": "HQ"
    },
    {
      "idComuna": "5",
      "descripcion": "Huara",
      "abreviacion": "HR"
    },
    {
      "idComuna": "25",
      "descripcion": "Huasco",
      "abreviacion": "HS"
    },
    {
      "idComuna": "327",
      "descripcion": "Huechuraba",
      "abreviacion": "HU"
    },
    {
      "idComuna": "41",
      "descripcion": "Illapel",
      "abreviacion": "IP"
    },
    {
      "idComuna": "324",
      "descripcion": "Independencia",
      "abreviacion": "IN"
    },
    {
      "idComuna": "8",
      "descripcion": "Iquique",
      "abreviacion": "IQ"
    },
    {
      "idComuna": "305",
      "descripcion": "Isla de Maipo",
      "abreviacion": "IM"
    },
    {
      "idComuna": "50",
      "descripcion": "Isla de Pascua",
      "abreviacion": "IP"
    },
    {
      "idComuna": "74",
      "descripcion": "Juan Fernández",
      "abreviacion": "JF"
    },
    {
      "idComuna": "330",
      "descripcion": "La Cisterna",
      "abreviacion": "CI"
    },
    {
      "idComuna": "64",
      "descripcion": "La Cruz",
      "abreviacion": "LZ"
    },
    {
      "idComuna": "101",
      "descripcion": "La Estrella",
      "abreviacion": "LE"
    },
    {
      "idComuna": "316",
      "descripcion": "La Florida",
      "abreviacion": "LF"
    },
    {
      "idComuna": "332",
      "descripcion": "La Granja",
      "abreviacion": "LG"
    },
    {
      "idComuna": "29",
      "descripcion": "La Higuera",
      "abreviacion": "LH"
    },
    {
      "idComuna": "52",
      "descripcion": "La Ligua",
      "abreviacion": "LL"
    },
    {
      "idComuna": "334",
      "descripcion": "La Pintana",
      "abreviacion": "PT"
    },
    {
      "idComuna": "314",
      "descripcion": "La Reina",
      "abreviacion": "LR"
    },
    {
      "idComuna": "31",
      "descripcion": "La Serena",
      "abreviacion": "LS"
    },
    {
      "idComuna": "237",
      "descripcion": "La Unión",
      "abreviacion": "LU"
    },
    {
      "idComuna": "238",
      "descripcion": "Lago Ranco",
      "abreviacion": "LR"
    },
    {
      "idComuna": "273",
      "descripcion": "Lago Verde",
      "abreviacion": "LV"
    },
    {
      "idComuna": "282",
      "descripcion": "Laguna Blanca",
      "abreviacion": "LG"
    },
    {
      "idComuna": "176",
      "descripcion": "Laja",
      "abreviacion": "LJ"
    },
    {
      "idComuna": "293",
      "descripcion": "Lampa",
      "abreviacion": "LA"
    },
    {
      "idComuna": "229",
      "descripcion": "Lanco",
      "abreviacion": "LN"
    },
    {
      "idComuna": "87",
      "descripcion": "Las Cabras",
      "abreviacion": "CA"
    },
    {
      "idComuna": "313",
      "descripcion": "Las Condes",
      "abreviacion": "LC"
    },
    {
      "idComuna": "213",
      "descripcion": "Lautaro",
      "abreviacion": "LO"
    },
    {
      "idComuna": "147",
      "descripcion": "Lebu",
      "abreviacion": "LB"
    },
    {
      "idComuna": "129",
      "descripcion": "Licantén",
      "abreviacion": "LC"
    },
    {
      "idComuna": "67",
      "descripcion": "Limache",
      "abreviacion": "LI"
    },
    {
      "idComuna": "119",
      "descripcion": "Linares",
      "abreviacion": "LN"
    },
    {
      "idComuna": "100",
      "descripcion": "Litueche",
      "abreviacion": "LH"
    },
    {
      "idComuna": "250",
      "descripcion": "Llanquihue",
      "abreviacion": "LQ"
    },
    {
      "idComuna": "61",
      "descripcion": "Llay-Llay",
      "abreviacion": "LY"
    },
    {
      "idComuna": "311",
      "descripcion": "Lo Barnechea",
      "abreviacion": "LB"
    },
    {
      "idComuna": "328",
      "descripcion": "Lo Espejo",
      "abreviacion": "LE"
    },
    {
      "idComuna": "319",
      "descripcion": "Lo Prado",
      "abreviacion": "LP"
    },
    {
      "idComuna": "112",
      "descripcion": "Lolol",
      "abreviacion": "LO"
    },
    {
      "idComuna": "223",
      "descripcion": "Loncoche",
      "abreviacion": "LC"
    },
    {
      "idComuna": "121",
      "descripcion": "Longaví",
      "abreviacion": "LG"
    },
    {
      "idComuna": "203",
      "descripcion": "Lonquimay",
      "abreviacion": "LY"
    },
    {
      "idComuna": "148",
      "descripcion": "Los Álamos",
      "abreviacion": "LW"
    },
    {
      "idComuna": "72",
      "descripcion": "Los Andes",
      "abreviacion": "AN"
    },
    {
      "idComuna": "177",
      "descripcion": "Los Ángeles",
      "abreviacion": "LA"
    },
    {
      "idComuna": "233",
      "descripcion": "Los Lagos",
      "abreviacion": "LL"
    },
    {
      "idComuna": "251",
      "descripcion": "Los Muermos",
      "abreviacion": "LS"
    },
    {
      "idComuna": "201",
      "descripcion": "Los Sauces",
      "abreviacion": "LE"
    },
    {
      "idComuna": "42",
      "descripcion": "Los Vilos",
      "abreviacion": "LV"
    },
    {
      "idComuna": "193",
      "descripcion": "Lota",
      "abreviacion": "LT"
    },
    {
      "idComuna": "204",
      "descripcion": "Lumaco",
      "abreviacion": "LM"
    },
    {
      "idComuna": "86",
      "descripcion": "Machalí",
      "abreviacion": "MA"
    },
    {
      "idComuna": "342",
      "descripcion": "Macul",
      "abreviacion": "ML"
    },
    {
      "idComuna": "231",
      "descripcion": "Máfil",
      "abreviacion": "MA"
    },
    {
      "idComuna": "320",
      "descripcion": "Maipú",
      "abreviacion": "MA"
    },
    {
      "idComuna": "97",
      "descripcion": "Malloa",
      "abreviacion": "ML"
    },
    {
      "idComuna": "103",
      "descripcion": "Marchigue",
      "abreviacion": "MH"
    },
    {
      "idComuna": "12",
      "descripcion": "María Elena",
      "abreviacion": "ME"
    },
    {
      "idComuna": "298",
      "descripcion": "María Pinto",
      "abreviacion": "MP"
    },
    {
      "idComuna": "228",
      "descripcion": "Mariquina",
      "abreviacion": "MQ"
    },
    {
      "idComuna": "142",
      "descripcion": "Maule",
      "abreviacion": "MU"
    },
    {
      "idComuna": "254",
      "descripcion": "Maullín",
      "abreviacion": "ML"
    },
    {
      "idComuna": "16",
      "descripcion": "Mejillones",
      "abreviacion": "MJ"
    },
    {
      "idComuna": "215",
      "descripcion": "Melipeuco",
      "abreviacion": "MP"
    },
    {
      "idComuna": "299",
      "descripcion": "Melipilla",
      "abreviacion": "ME"
    },
    {
      "idComuna": "131",
      "descripcion": "Molina",
      "abreviacion": "MI"
    },
    {
      "idComuna": "38",
      "descripcion": "Monte Patria",
      "abreviacion": "MP"
    },
    {
      "idComuna": "183",
      "descripcion": "Mulchén",
      "abreviacion": "MC"
    },
    {
      "idComuna": "181",
      "descripcion": "Nacimiento",
      "abreviacion": "NC"
    },
    {
      "idComuna": "110",
      "descripcion": "Nancagua",
      "abreviacion": "NG"
    },
    {
      "idComuna": "280",
      "descripcion": "Natales",
      "abreviacion": "NA"
    },
    {
      "idComuna": "99",
      "descripcion": "Navidad",
      "abreviacion": "NA"
    },
    {
      "idComuna": "182",
      "descripcion": "Negrete",
      "abreviacion": "NE"
    },
    {
      "idComuna": "154",
      "descripcion": "Ninhue",
      "abreviacion": "NN"
    },
    {
      "idComuna": "156",
      "descripcion": "Ñiquén",
      "abreviacion": "ÑI"
    },
    {
      "idComuna": "62",
      "descripcion": "Nogales",
      "abreviacion": "NO"
    },
    {
      "idComuna": "211",
      "descripcion": "Nueva Imperial",
      "abreviacion": "NI"
    },
    {
      "idComuna": "340",
      "descripcion": "Ñuñoa",
      "abreviacion": "ÑU"
    },
    {
      "idComuna": "279",
      "descripcion": "O`Higgins",
      "abreviacion": "OH"
    },
    {
      "idComuna": "90",
      "descripcion": "Olivar",
      "abreviacion": "OR"
    },
    {
      "idComuna": "14",
      "descripcion": "Ollagüe",
      "abreviacion": "OG"
    },
    {
      "idComuna": "68",
      "descripcion": "Olmué",
      "abreviacion": "OL"
    },
    {
      "idComuna": "242",
      "descripcion": "Osorno",
      "abreviacion": "OS"
    },
    {
      "idComuna": "35",
      "descripcion": "Ovalle",
      "abreviacion": "OV"
    },
    {
      "idComuna": "306",
      "descripcion": "Padre Hurtado",
      "abreviacion": "PH"
    },
    {
      "idComuna": "227",
      "descripcion": "Padre las Casas",
      "abreviacion": "PD"
    },
    {
      "idComuna": "34",
      "descripcion": "Paihuano",
      "abreviacion": "PG"
    },
    {
      "idComuna": "235",
      "descripcion": "Paillaco",
      "abreviacion": "PL"
    },
    {
      "idComuna": "310",
      "descripcion": "Paine",
      "abreviacion": "PA"
    },
    {
      "idComuna": "269",
      "descripcion": "Palena",
      "abreviacion": "PE"
    },
    {
      "idComuna": "106",
      "descripcion": "Palmilla",
      "abreviacion": "PM"
    },
    {
      "idComuna": "230",
      "descripcion": "Panguipulli",
      "abreviacion": "PG"
    },
    {
      "idComuna": "60",
      "descripcion": "Panquehue",
      "abreviacion": "PU"
    },
    {
      "idComuna": "54",
      "descripcion": "Papudo",
      "abreviacion": "PP"
    },
    {
      "idComuna": "104",
      "descripcion": "Paredones",
      "abreviacion": "PD"
    },
    {
      "idComuna": "122",
      "descripcion": "Parral",
      "abreviacion": "PA"
    },
    {
      "idComuna": "329",
      "descripcion": "Pedro Aguirre Cerda",
      "abreviacion": "PC"
    },
    {
      "idComuna": "140",
      "descripcion": "Pelarco",
      "abreviacion": "PR"
    },
    {
      "idComuna": "134",
      "descripcion": "Pelluhue",
      "abreviacion": "PH"
    },
    {
      "idComuna": "170",
      "descripcion": "Pemuco",
      "abreviacion": "PH"
    },
    {
      "idComuna": "302",
      "descripcion": "Peñaflor",
      "abreviacion": "PE"
    },
    {
      "idComuna": "315",
      "descripcion": "Peñalolén",
      "abreviacion": "PN"
    },
    {
      "idComuna": "138",
      "descripcion": "Pencahue",
      "abreviacion": "PN"
    },
    {
      "idComuna": "188",
      "descripcion": "Penco",
      "abreviacion": "PC"
    },
    {
      "idComuna": "105",
      "descripcion": "Peralillo",
      "abreviacion": "PL"
    },
    {
      "idComuna": "209",
      "descripcion": "Perquenco",
      "abreviacion": "PB"
    },
    {
      "idComuna": "51",
      "descripcion": "Petorca",
      "abreviacion": "PE"
    },
    {
      "idComuna": "93",
      "descripcion": "Peumo",
      "abreviacion": "PO"
    },
    {
      "idComuna": "10",
      "descripcion": "Pica",
      "abreviacion": "PC"
    },
    {
      "idComuna": "95",
      "descripcion": "Pichidegua",
      "abreviacion": "PG"
    },
    {
      "idComuna": "102",
      "descripcion": "Pichilemu",
      "abreviacion": "PI"
    },
    {
      "idComuna": "165",
      "descripcion": "Pinto",
      "abreviacion": "PX"
    },
    {
      "idComuna": "296",
      "descripcion": "Pirque",
      "abreviacion": "PI"
    },
    {
      "idComuna": "221",
      "descripcion": "Pitrufquén",
      "abreviacion": "PF"
    },
    {
      "idComuna": "111",
      "descripcion": "Placilla",
      "abreviacion": "PK"
    },
    {
      "idComuna": "160",
      "descripcion": "Portezuelo",
      "abreviacion": "PZ"
    },
    {
      "idComuna": "287",
      "descripcion": "Porvenir",
      "abreviacion": "PI"
    },
    {
      "idComuna": "9",
      "descripcion": "Pozo Almonte",
      "abreviacion": "PZ"
    },
    {
      "idComuna": "286",
      "descripcion": "Primavera",
      "abreviacion": "PR"
    },
    {
      "idComuna": "337",
      "descripcion": "Providencia",
      "abreviacion": "PR"
    },
    {
      "idComuna": "73",
      "descripcion": "Puchuncaví",
      "abreviacion": "PC"
    },
    {
      "idComuna": "225",
      "descripcion": "Pucón",
      "abreviacion": "PO"
    },
    {
      "idComuna": "317",
      "descripcion": "Pudahuel",
      "abreviacion": "PD"
    },
    {
      "idComuna": "295",
      "descripcion": "Puente Alto",
      "abreviacion": "PU"
    },
    {
      "idComuna": "252",
      "descripcion": "Puerto Montt",
      "abreviacion": "PM"
    },
    {
      "idComuna": "245",
      "descripcion": "Puerto Octay",
      "abreviacion": "PT"
    },
    {
      "idComuna": "249",
      "descripcion": "Puerto Varas",
      "abreviacion": "PV"
    },
    {
      "idComuna": "108",
      "descripcion": "Pumanque",
      "abreviacion": "PQ"
    },
    {
      "idComuna": "37",
      "descripcion": "Punitaqui",
      "abreviacion": "PN"
    },
    {
      "idComuna": "285",
      "descripcion": "Punta Arenas",
      "abreviacion": "PA"
    },
    {
      "idComuna": "263",
      "descripcion": "Puqueldón",
      "abreviacion": "PU"
    },
    {
      "idComuna": "200",
      "descripcion": "Purén",
      "abreviacion": "PN"
    },
    {
      "idComuna": "246",
      "descripcion": "Purranque",
      "abreviacion": "PQ"
    },
    {
      "idComuna": "56",
      "descripcion": "Putaendo",
      "abreviacion": "PT"
    },
    {
      "idComuna": "2",
      "descripcion": "Putre",
      "abreviacion": "PU"
    },
    {
      "idComuna": "243",
      "descripcion": "Puyehue",
      "abreviacion": "PY"
    },
    {
      "idComuna": "264",
      "descripcion": "Queilén",
      "abreviacion": "QE"
    },
    {
      "idComuna": "265",
      "descripcion": "Quellón",
      "abreviacion": "QU"
    },
    {
      "idComuna": "257",
      "descripcion": "Quemchi",
      "abreviacion": "QM"
    },
    {
      "idComuna": "185",
      "descripcion": "Quilaco",
      "abreviacion": "QI"
    },
    {
      "idComuna": "323",
      "descripcion": "Quilicura",
      "abreviacion": "QC"
    },
    {
      "idComuna": "180",
      "descripcion": "Quilleco",
      "abreviacion": "QC"
    },
    {
      "idComuna": "166",
      "descripcion": "Quillón",
      "abreviacion": "QL"
    },
    {
      "idComuna": "65",
      "descripcion": "Quillota",
      "abreviacion": "QL"
    },
    {
      "idComuna": "79",
      "descripcion": "Quilpué",
      "abreviacion": "QP"
    },
    {
      "idComuna": "261",
      "descripcion": "Quinchao",
      "abreviacion": "QO"
    },
    {
      "idComuna": "94",
      "descripcion": "Quinta de Tilcoco",
      "abreviacion": "QC"
    },
    {
      "idComuna": "336",
      "descripcion": "Quinta Normal",
      "abreviacion": "QN"
    },
    {
      "idComuna": "75",
      "descripcion": "Quintero",
      "abreviacion": "QT"
    },
    {
      "idComuna": "153",
      "descripcion": "Quirihue",
      "abreviacion": "QH"
    },
    {
      "idComuna": "85",
      "descripcion": "Rancagua",
      "abreviacion": "RA"
    },
    {
      "idComuna": "164",
      "descripcion": "Ranquil",
      "abreviacion": "RQ"
    },
    {
      "idComuna": "126",
      "descripcion": "Rauco",
      "abreviacion": "RU"
    },
    {
      "idComuna": "325",
      "descripcion": "Recoleta",
      "abreviacion": "RC"
    },
    {
      "idComuna": "198",
      "descripcion": "Renaico",
      "abreviacion": "RE"
    },
    {
      "idComuna": "322",
      "descripcion": "Renca",
      "abreviacion": "RE"
    },
    {
      "idComuna": "98",
      "descripcion": "Rengo",
      "abreviacion": "RE"
    },
    {
      "idComuna": "92",
      "descripcion": "Requínoa",
      "abreviacion": "RN"
    },
    {
      "idComuna": "120",
      "descripcion": "Retiro",
      "abreviacion": "RT"
    },
    {
      "idComuna": "70",
      "descripcion": "Rinconada",
      "abreviacion": "RI"
    },
    {
      "idComuna": "239",
      "descripcion": "Río Bueno",
      "abreviacion": "RB"
    },
    {
      "idComuna": "136",
      "descripcion": "Río Claro",
      "abreviacion": "RC"
    },
    {
      "idComuna": "36",
      "descripcion": "Río Hurtado",
      "abreviacion": "RH"
    },
    {
      "idComuna": "275",
      "descripcion": "Río Ibañez",
      "abreviacion": "RI"
    },
    {
      "idComuna": "244",
      "descripcion": "Río Negro",
      "abreviacion": "RN"
    },
    {
      "idComuna": "284",
      "descripcion": "Río Verde",
      "abreviacion": "RV"
    },
    {
      "idComuna": "128",
      "descripcion": "Romeral",
      "abreviacion": "RL"
    },
    {
      "idComuna": "216",
      "descripcion": "Saavedra",
      "abreviacion": "SA"
    },
    {
      "idComuna": "130",
      "descripcion": "Sagrada Familia",
      "abreviacion": "SG"
    },
    {
      "idComuna": "43",
      "descripcion": "Salamanca",
      "abreviacion": "SA"
    },
    {
      "idComuna": "48",
      "descripcion": "San Antonio",
      "abreviacion": "SA"
    },
    {
      "idComuna": "308",
      "descripcion": "San Bernardo",
      "abreviacion": "SB"
    },
    {
      "idComuna": "155",
      "descripcion": "San Carlos",
      "abreviacion": "SC"
    },
    {
      "idComuna": "141",
      "descripcion": "San Clemente",
      "abreviacion": "SL"
    },
    {
      "idComuna": "69",
      "descripcion": "San Esteban",
      "abreviacion": "SE"
    },
    {
      "idComuna": "157",
      "descripcion": "San Fabián",
      "abreviacion": "SM"
    },
    {
      "idComuna": "58",
      "descripcion": "San Felipe",
      "abreviacion": "SN"
    },
    {
      "idComuna": "107",
      "descripcion": "San Fernando",
      "abreviacion": "SF"
    },
    {
      "idComuna": "82",
      "descripcion": "San Francisco de Mostazal",
      "abreviacion": "MO"
    },
    {
      "idComuna": "283",
      "descripcion": "San Gregorio",
      "abreviacion": "SG"
    },
    {
      "idComuna": "168",
      "descripcion": "San Ignacio",
      "abreviacion": "SI"
    },
    {
      "idComuna": "115",
      "descripcion": "San Javier",
      "abreviacion": "SJ"
    },
    {
      "idComuna": "341",
      "descripcion": "San Joaquín",
      "abreviacion": "SJ"
    },
    {
      "idComuna": "294",
      "descripcion": "San José de Maipo",
      "abreviacion": "JM"
    },
    {
      "idComuna": "240",
      "descripcion": "San Juan de la Costa",
      "abreviacion": "JC"
    },
    {
      "idComuna": "335",
      "descripcion": "San Miguel",
      "abreviacion": "SM"
    },
    {
      "idComuna": "158",
      "descripcion": "San Nicolás",
      "abreviacion": "SN"
    },
    {
      "idComuna": "241",
      "descripcion": "San Pablo",
      "abreviacion": "SP"
    },
    {
      "idComuna": "300",
      "descripcion": "San Pedro",
      "abreviacion": "SP"
    },
    {
      "idComuna": "15",
      "descripcion": "San Pedro de Atacama",
      "abreviacion": "SP"
    },
    {
      "idComuna": "195",
      "descripcion": "San Pedro de la Paz",
      "abreviacion": "PP"
    },
    {
      "idComuna": "144",
      "descripcion": "San Rafael",
      "abreviacion": "SR"
    },
    {
      "idComuna": "331",
      "descripcion": "San Ramón",
      "abreviacion": "SR"
    },
    {
      "idComuna": "173",
      "descripcion": "San Rosendo",
      "abreviacion": "SS"
    },
    {
      "idComuna": "96",
      "descripcion": "San Vicente",
      "abreviacion": "SV"
    },
    {
      "idComuna": "184",
      "descripcion": "Santa Bárbara",
      "abreviacion": "SB"
    },
    {
      "idComuna": "109",
      "descripcion": "Santa Cruz",
      "abreviacion": "ST"
    },
    {
      "idComuna": "194",
      "descripcion": "Santa Juana",
      "abreviacion": "SJ"
    },
    {
      "idComuna": "59",
      "descripcion": "Santa María",
      "abreviacion": "SM"
    },
    {
      "idComuna": "339",
      "descripcion": "Santiago",
      "abreviacion": "ST"
    },
    {
      "idComuna": "49",
      "descripcion": "Santo Domingo",
      "abreviacion": "SD"
    },
    {
      "idComuna": "0",
      "descripcion": "Seleccione Comuna...",
      "abreviacion": "  "
    },
    {
      "idComuna": "17",
      "descripcion": "Sierra Gorda",
      "abreviacion": "SG"
    },
    {
      "idComuna": "304",
      "descripcion": "Talagante",
      "abreviacion": "TG"
    },
    {
      "idComuna": "139",
      "descripcion": "Talca",
      "abreviacion": "TC"
    },
    {
      "idComuna": "187",
      "descripcion": "Talcahuano",
      "abreviacion": "TH"
    },
    {
      "idComuna": "19",
      "descripcion": "Taltal",
      "abreviacion": "TL"
    },
    {
      "idComuna": "212",
      "descripcion": "Temuco",
      "abreviacion": "TE"
    },
    {
      "idComuna": "123",
      "descripcion": "Teno",
      "abreviacion": "TN"
    },
    {
      "idComuna": "217",
      "descripcion": "Teodoro Schmidt",
      "abreviacion": "TS"
    },
    {
      "idComuna": "24",
      "descripcion": "Tierra Amarilla",
      "abreviacion": "TA"
    },
    {
      "idComuna": "291",
      "descripcion": "Til Til",
      "abreviacion": "TT"
    },
    {
      "idComuna": "288",
      "descripcion": "Timaukel",
      "abreviacion": "TK"
    },
    {
      "idComuna": "151",
      "descripcion": "Tirúa",
      "abreviacion": "TU"
    },
    {
      "idComuna": "11",
      "descripcion": "Tocopilla",
      "abreviacion": "TC"
    },
    {
      "idComuna": "220",
      "descripcion": "Toltén",
      "abreviacion": "TT"
    },
    {
      "idComuna": "186",
      "descripcion": "Tomé",
      "abreviacion": "TM"
    },
    {
      "idComuna": "281",
      "descripcion": "Torres del Paine",
      "abreviacion": "TP"
    },
    {
      "idComuna": "278",
      "descripcion": "Tortel",
      "abreviacion": "TO"
    },
    {
      "idComuna": "205",
      "descripcion": "Traiguén",
      "abreviacion": "TN"
    },
    {
      "idComuna": "159",
      "descripcion": "Trehuaco",
      "abreviacion": "TR"
    },
    {
      "idComuna": "178",
      "descripcion": "Tucapel",
      "abreviacion": "TL"
    },
    {
      "idComuna": "232",
      "descripcion": "Valdivia",
      "abreviacion": "VV"
    },
    {
      "idComuna": "345",
      "descripcion": "Valle Grande",
      "abreviacion": "VL"
    },
    {
      "idComuna": "26",
      "descripcion": "Vallenar",
      "abreviacion": "VA"
    },
    {
      "idComuna": "78",
      "descripcion": "Valparaíso",
      "abreviacion": "VP"
    },
    {
      "idComuna": "124",
      "descripcion": "Vichuquén",
      "abreviacion": "VQ"
    },
    {
      "idComuna": "206",
      "descripcion": "Victoria",
      "abreviacion": "VI"
    },
    {
      "idComuna": "30",
      "descripcion": "Vicuña",
      "abreviacion": "VÑ"
    },
    {
      "idComuna": "214",
      "descripcion": "Vilcún",
      "abreviacion": "VC"
    },
    {
      "idComuna": "116",
      "descripcion": "Villa Alegre",
      "abreviacion": "VG"
    },
    {
      "idComuna": "77",
      "descripcion": "Villa Alemana",
      "abreviacion": "VA"
    },
    {
      "idComuna": "224",
      "descripcion": "Villarrica",
      "abreviacion": "VR"
    },
    {
      "idComuna": "76",
      "descripcion": "Viña del Mar",
      "abreviacion": "VM"
    },
    {
      "idComuna": "312",
      "descripcion": "Vitacura",
      "abreviacion": "VI"
    },
    {
      "idComuna": "117",
      "descripcion": "Yerbas Buenas",
      "abreviacion": "YB"
    },
    {
      "idComuna": "174",
      "descripcion": "Yumbel",
      "abreviacion": "YL"
    },
    {
      "idComuna": "171",
      "descripcion": "Yungay",
      "abreviacion": "YY"
    },
    {
      "idComuna": "55",
      "descripcion": "Zapallar",
      "abreviacion": "ZP"
    }
  ]
class ResponseAI:
    def __init__(self, temperature=0):
        self.key = os.environ["OPENAI_KEY"]
        self.client = OpenAI(api_key=self.key)
        self.temperature = temperature
        self.prefix_system_message = ""

        stream = open(os.path.join(ROOT_DIR, "resources/test.yaml"), "r")
        self.queries = yaml.safe_load(stream).get("query")
        stream.close()

    def _complete_response(self, data, system_message=""):
        response = self.client.chat.completions.create(
            temperature=self.temperature,
            model="gpt-4o",
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": system_message,
                },
                {
                    "role": "user",
                    "content": f"Por favor, procesa la siguiente información en español: {data}",
                },
            ],
        )
        return response

    def first_stage(self, data):
        FIRST_STAGE_MESSAGE = self.queries.get("preparse")
        response = self._complete_response(data, FIRST_STAGE_MESSAGE)
        intent_dict = response.choices[0].message.content
        json_intent = json.loads(intent_dict)
        intent = json_intent["intent"]
        answer = self.query_LLM(json_intent["intent"], data)
        answer = json.loads(answer)

        
        # Revisamos si hay campos con valores vacíos
        print(answer)
        
        missing_fields = []

        for item in answer.get("response", []):
            if item['value'] is False:  # Comprobamos si el valor es False
                missing_fields.append(item['key'])

        # Si hay campos faltantes, generar un mensaje amable
        if missing_fields:
            missing_fields_str = ', '.join(missing_fields)
            message = f"Parece que falta información en los siguientes campos: {missing_fields_str}. ¿Podrías proporcionarnos los datos faltantes?"

            print("missing_fields", missing_fields)
            if intent == "hipotecario":
                if len(missing_fields) == 1 and (missing_fields[0] == "Tipo de propiedad"):
                    message = "¡Gracias por toda la información! Todo está completo."
            
            if intent == "buscar":
                if "Comuna" not in missing_fields and "Region" not in missing_fields and "Tipo de contrato" not in missing_fields:
                    message = "¡Gracias por toda la información! Todo está completo."
            if intent  == "tasar":
                if len(missing_fields) == 1 and (missing_fields[0] == "Rol" or missing_fields[0] == "Direccion"):
                    comuna_value = next((item['value'] for item in answer['response'] if item['key'] == 'Comuna'), None)
                    comuna_id=""
                    for item in comunas :
                        if item["descripcion"] == comuna_value:
                            comuna_id = item["idComuna"]
                            break

                    payload = {}

                    role_value = next((item["value"] for item in answer["response"] if item["key"] == "Rol"), None)
                    headers = {
                    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkdlcmFyZG8gTXXDsW96IiwiaWF0IjoxNTE2MjM5MDIyLCJ1c2VyX2lkIjoiMTIzNCJ9.FpthiZ_xC_U0RlVnlvR-axVKCmUVoN200VXJ6FD8mAU'
                    }
                    url = f"https://gw.toctoc.com/1.0/info/role?role={role_value}&idCommune={comuna_id}"
                    print(url)
                    response = requests.request("GET", url, headers=headers, data=payload)
                    response = response.json()
                    latitude, longitude = response["data"]["location"]["coordinates"][1], response["data"]["location"]["coordinates"][0]
                    property_type = response["data"]["housingType"]["housingTypeName"]
                    usable_area = response["data"]["information"]["areaofConstructionLine"]
                    #using this as an example ("https://gw.toctoc.com/1.0/valorization/appraisal/sale?lat=40.7128&long=-74.006&propertyFamilyTypeId=1&usableArea=10", requestOptions)
                    url = f"https://gw.toctoc.com/1.0/valorization/appraisal/sale?lat={latitude}&long={longitude}&propertyFamilyTypeId=1&usableArea={usable_area}"
                    response = requests.request("GET", url, headers=headers, data=payload)
                    response = response.json()
                    tasamin = response["data"]["minPrice"]
                    tasamax = response["data"]["maxPrice"]
                    message = f"El precio de tu propiedad oscila entre {tasamin} y {tasamax} UF"
                    print(message)
        else:
            message = "¡Gracias por toda la información! Todo está completo."
            #llamar api
        return message


    # Probably this method could replace every upper method
    def query_LLM(self, query_name, data):
        query = self.queries.get(query_name)
        response = ""

        if query_name == "buscar":
            MESSAGE = self.queries.get("buscar")
            response = self._complete_response(data, MESSAGE)
            data = response.choices[0].message.content
            print(data)

        if query_name == "tasar":
            MESSAGE = self.queries.get("tasar")
            response = self._complete_response(data, MESSAGE)
            data = response.choices[0].message.content

        if query_name == "hipotecario":
            MESSAGE = self.queries.get("hipotecario")
            response = self._complete_response(data, MESSAGE)
            data = response.choices[0].message.content
            print(data)

        return response.choices[0].message.content