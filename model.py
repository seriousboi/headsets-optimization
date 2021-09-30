from parser import durations , capacities , demands , distances , travelCost
from mip import *



headsetsAmount = 3
factoriesAmount = 3
citiesAmount = 21

print(travelCost)

model = Model(name = "headsets", sense = mip.MINIMIZE, solver_name="CBC")

shipping = []
for factory in range(factoriesAmount):
    shipping += [[]]
    for city in range(citiesAmount):
        shipping[factory] += [[]]
        for headset in range(headsetsAmount):
            shipping[factory][city] += [model.add_var(var_type=INTEGER)]



model.objective = minimize(xsum(xsum(xsum( shipping[factory][city][headset]*distances[city][factory]*travelCost for factory in range(factoriesAmount))for city in range(citiesAmount))for headset in range(headsetsAmount)))



for city in range(citiesAmount):
    for headset in range(headsetsAmount):
        model += ( xsum( shipping[factory][city][headset] for factory in range(factoriesAmount)) >= demands[city][headset] )

for factory in range(factoriesAmount):
    model += ( xsum( xsum( shipping[factory][city][headset]*durations[factory][headset] for city in range(citiesAmount) ) for headset in range(headsetsAmount) ) <= capacities[factory] )


model.optimize()
print(model.objective.x)
