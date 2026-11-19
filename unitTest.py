"""
Unit Test - Population Model
"""

import popmodel as mod

testTemp = [5,8,2,4,5,8,1,13,8,10]
testMoist = [65,66,66,67,68,45,23,89,100,13]
testHumid = [100,10,23,5,6,7,59,40,89,12]
testPop = 4000
count = 0
length = len(testTemp)


def UnitTestpop(testTemp, testMoist, testHumid, testPop, count):
    if count > 10:
        testPop += -15
    if testTemp > 18:
        testPop += -8
    if testMoist < 65:
        if testTemp > 9:
            count =+ 1
            testPop += -9
        else:
            count = 0
            testPop += -9
    if testHumid < 25:
        testPop += -9
    return testPop

            
def UnitTest():
    false = 0
    true = 0
    for i in range(0, length):
        pop = mod.popModel(testTemp[i], testMoist[i], testHumid[i], testPop, count)
        test = UnitTestpop(testTemp[i], testMoist[i], testHumid[i], testPop, count)
        if pop != test:
            false += 1
        else:
            true += 1
    print("False:", false, "True:", true)
            

print(UnitTest())