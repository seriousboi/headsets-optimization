from parsers import getData
from mip import *



def createModel():
    durations , capacities , demands , distances , travelCost = getData()

    headsetsAmount = 3
    factoriesAmount = 3
    citiesAmount = 21

    model = Model(name = "headsets", sense = mip.MINIMIZE, solver_name="CBC")

    #création des variables de décision
    shipping = []
    for factory in range(factoriesAmount):
        shipping += [[]]
        for city in range(citiesAmount):
            shipping[factory] += [[]]
            for headset in range(headsetsAmount):
                shipping[factory][city] += [model.add_var(var_type=INTEGER)]

    #définition de l'objectif
    model.objective = minimize(xsum(xsum(xsum(
    shipping[factory][city][headset]*distances[city][factory]*travelCost
    for factory in range(factoriesAmount))
    for city in range(citiesAmount))
    for headset in range(headsetsAmount))
    )

    #contraintes des demandes des villes
    for city in range(citiesAmount):
        for headset in range(headsetsAmount):
            model += ( xsum( shipping[factory][city][headset] for factory in range(factoriesAmount)) >= demands[city][headset] )

    #contraintes des capacitées des usines
    for factory in range(factoriesAmount):
        model += ( xsum( xsum( shipping[factory][city][headset]*durations[factory][headset] for city in range(citiesAmount) ) for headset in range(headsetsAmount) ) <= capacities[factory] )

    return model , shipping
