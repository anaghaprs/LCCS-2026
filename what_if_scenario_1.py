"""Population Model - Great Spotted Woodpecker (What-if Scenario 1)"""
#All TEMP data will increase by 10
import pandas as pd
import matplotlib.pyplot as plt

#population model
startPop = 4000
count = 0
population = []
time = []
def popModel(temp, moist, humid, startPop, count):
    if count > 10:
        startPop += -15
    if temp > 18:
        startPop += -8
    if moist < 65:
        if temp > 9:
            count =+ 1
            startPop += -9
        else:
            count = 0
            startPop += -9
    if humid < 25:
        startPop += -9
    return startPop

#disaster risk
risk = 0
def droughtRiskTest(temp, moist, risk):
    if temp > 15:
        risk += 10
    if moist < 25:
        if temp > 18:
            risk += 20
        else:
            risk += 7
    return risk

#empty lists that will be appended with created values
dpopulation = [] #"""drought population (set value)"""
drtime = [] #"""drought time lapsed (set value)"""


drisk = [] #"""DROUGHT RISK (SET VALUES)"""
dtime = [] #"""DROUGHT RISK TIME LAPSED (SET VALUES)"""

drsrisk = [] #"""DROUGHT RISK (DROUGHT VALUES)"""
drstime = [] #"""DROUGHT TIME LAPSET (DROUGHT VALUES)"""

df = pd.read_csv('microbit.csv')

temp = df['temp'].tolist()
moist = df['moist'].tolist()
humid = df['humid'].tolist()

        
for i in range(0, len(temp)):
    temp[i] = int(temp[i]) + 10



 #modelling population
for i in range(0, len(temp)):
    pop = popModel(temp[i], moist[i], humid[i], startPop, count)
    population.append(pop)
    time.append(i)

 #modelling disaster risk for given data
for y in range(0, len(temp)):
    driskval = droughtRiskTest(temp[y], moist[y], risk)
    drisk.append(driskval)
    dtime.append(y)

#graphs
fig, (ax) = plt.subplots(1, layout='constrained', sharey=True) #sorting population and drought risk into separate subplots
fig1, (bx) = plt.subplots(1, layout='constrained', sharey=True)

#graph of poulation with set data
ax.plot(time, population, linewidth=2.0)
ax.set_ylabel('population')
ax.set_xlabel('time')
ax.set_title('projected population of the great spotted woodpecker', fontsize=8)
ax.set_xticks([])

#graph of risk with set values
bx.plot(time, drisk, linewidth=2.0, linestyle = 'dotted')
bx.set_ylabel('risk\n(%)')
bx.set_xlabel('time')
bx.set_title('projected drought risk', fontsize=8)
bx.set_xticks([])

plt.show()
