"""Population Model - Great Spotted Woodpecker"""
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

#taking in user input to determine whether to use pre-made values or set values
ans = input("Welcome to population and drought modelling! Would you like to use pre-collected data? (Y/N): ").upper()
while True:
    if ans == "Y":
        #data collected by microbit and retrieval using pandas
        df = pd.read_csv('microbit.csv')

        temp = df['temp'].tolist()
        moist = df['moist'].tolist()
        humid = df['humid'].tolist()

        #drought  simulation data and lists:
        droughttemp = [20,20,20,13,13,14,14,12,12,12,11,13,14,15,16,17,20,21,23,19]
        droughtmoist = [10,10,8,9,2,3,4,6,7,2,5,0,3,1,7,8,9,11,13,10]
        droughthumid = [20,21,23,24,25,21,23,12,21,24,25,24,23,17,16,15,12,34,21,22]
        
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

        #modelling population risk with drought values 
        for x in range(0, len(droughttemp)):
            droughtsim = popModel(droughttemp[x], droughtmoist[x], droughthumid[x], startPop, count)
            dpopulation.append(droughtsim)
            drtime.append(x)
            
        #drought risk with simulated data
        for i in range(0, len(droughttemp)):
            droughtsimrisk = droughtRiskTest(droughttemp[i], droughtmoist[i], risk)
            drsrisk.append(droughtsimrisk)
            drstime.append(i)
        
        #graphs
        fig, (ax, cx) = plt.subplots(1,2, layout='constrained', sharey=True) #sorting population and drought risk into separate subplots
        fig1, (bx, dx) = plt.subplots(1,2, layout='constrained', sharey=True)

        #graph of poulation with set data
        ax.plot(time, population, linewidth=2.0)
        ax.set_ylabel('population')
        ax.set_xlabel('time')
        ax.set_title('projected population of the great spotted woodpecker', fontsize=8)
        ax.set_xticks([])

        #graph of population
        cx.plot(drtime, dpopulation, linewidth=2.0, color = 'r')
        cx.set_ylabel('population')
        cx.set_xlabel('time')
        cx.set_title('projected population of the great spotted woodpecker\n(drought conditions)', fontsize=8)
        cx.set_xticks([])
        fig.suptitle('Projected Populations', fontsize=16)

        #graph of risk with set values
        bx.plot(time, drisk, linewidth=2.0, linestyle = 'dotted')
        bx.set_ylabel('risk\n(%)')
        bx.set_xlabel('time')
        bx.set_title('projected drought risk', fontsize=8)
        bx.set_xticks([])

        #graph of risk with drought values

        dx.plot(drstime, drsrisk, linewidth=2.0, color = 'r', linestyle = 'dotted')
        dx.set_ylabel('risk\n(%)')
        dx.set_xlabel('time')
        dx.set_title('projected drought risk\n(drought conditions)', fontsize=8)
        dx.set_xticks([])
        fig1.suptitle('Projected Drought Risk', fontsize=16)


        plt.show()
    
    elif ans == 'N':
        humid = []
        temp = []
        moist = []
        time = []
        while True: #while loop so that if an incorrect value is input it will return to the original question
            answer = input("Continue adding values? (Y/N): ").upper()
            if answer == 'Y':
                humid.append(int(input("Please enter a value for humidity (0~100): ")))
                temp.append(int(input("Please enter a value for temperature (-10~100): ")))
                moist.append(int(input("Please enter a value for soil moisture (0~100): ")))
            elif answer == 'N':
                break #break to end loop
            else:
                print("Please input a valid answer (Y/N)")
    else:
        print("Please input a valid answer (Y/N)")
        
    print(population)
    
    #modelling population
    for i in range(0, len(temp)):
        pop = popModel(temp[i], moist[i], humid[i], startPop, count)
        population.append(pop)
        time.append(i)
        
    #modelling drought
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
    break







    