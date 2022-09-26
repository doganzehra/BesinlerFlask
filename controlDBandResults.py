from itertools import combinations
from unidecode import unidecode


def controlResults(yemekIkilileriDict, foodsFromDatabase):
    # A gelen liste

    unicodeFoodName = []
    for food in foodsFromDatabase:
        unicodeFoodName.append(unidecode(food))
    ikiliYemeklerDatabase = combinations(unicodeFoodName, 2)

    # ('dsfds', 'asaa') şeklinde
    returnedIkililer = {}
    for x in list(ikiliYemeklerDatabase):
        for key, value in yemekIkilileriDict.items():
            if (x[0] == key and x[1] == value) or (x[1] == key and x[0] == value):
                returnedIkililer[key] = value
    return returnedIkililer
