import csv
import pandas as pd
import math
import numpy as np

file = open('shots_data.csv')
type(file)
csvreader = csv.reader(file)

header = []
header = next(csvreader)
#print(header)

rows = []
for row in csvreader:
    row1 = rows.append(float(row[1]))
    row2 = rows.append(float(row[2]))
    row3 = rows.append(float(row[3]))
rows
# print(rows)


with open('shots_data.csv') as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]

data = pd.read_csv('shots_data.csv')
#print(data)


x = data.x
#print(x)
y = data.y
#print(y)
fgmade = data.fgmade
#print(fgmade)


data_x = np.array(x)
ser_x = pd.Series(data_x)
data_y = np.array(y)
ser_y = pd.Series(data_y)

# retrieve the first element
# Team A

#Set Variables

ThPMA= 0     #Three Point Make
ThPAA = 0    #Three Point Attempt
FGMA = 0     #Field Goal Make
FGAA = 0     #Field Goal Attempt
NCThA = 0    #NonCorner Three Make
NCThAA = 0   #NonCorner Three Attempt
TwPMA = 0    #Two point Make
TwPAA = 0    #Two Point Attempt
CThMA = 0    #Corner Three Make
CThAA = 0    #Corner Three Attempt

#Loop

for i in range(0,280):

    dist = math.sqrt(math.pow(x[i], 2) + math.pow(y[i], 2))
    #print()
    #print(dist)

    if fgmade[i] == 1:
        if y[i] > 7.8 and dist > 23.75:
            ThPMA = ThPMA + 1
            ThPAA = ThPAA + 1
            FGMA = FGMA + 1
            FGAA = FGAA + 1
            NCThA = NCThA + 1
            NCThAA = NCThAA + 1
        elif y[i] < 7.8 and x[i] > 22:
            ThPMA = ThPMA + 1
            ThPAA = ThPAA + 1
            FGMA = FGMA + 1
            FGAA = FGAA + 1
            CThMA = CThMA + 1
            CThAA = CThAA + 1
        else:
            FGMA = FGMA + 1
            FGAA = FGAA + 1
            TwPMA=TwPMA + 1
            TwPAA = TwPAA + 1
    else:
        if y[i] < 7.8 and x[i] > 22:
            CThAA = CThAA + 1
            FGAA = FGAA + 1
        elif y[i] > 7.8 and dist > 23.75:
            NCThAA = NCThAA + 1
            FGAA = FGAA + 1
        else:
            TwPAA = TwPAA +1
            FGAA = FGAA + 1


eFGA = (((FGMA+(0.5*ThPMA))/FGAA)*100)
print("The effective field goal percentage of Team A is", eFGA, "%")

#FG Percentages

TweFGA = (TwPMA/TwPAA)
print("The effective field goal percentage of Team A in the Two Point zone is", TweFGA, "%")
CeFGA = (CThMA/CThAA)
print("The effective field goal percentage of Team A in the Corner Three zone is", CeFGA, "%")
NeFGA = (NCThA/NCThAA)
print("The effective field goal percentage of Team A in the NonCorner Three zone is", NeFGA, "%")


#Shot distributions

TPDA = TwPAA / FGAA
NCTDA = NCThAA / FGAA
CTDA = CThAA / FGAA

print(TPDA, "% of shots by Team A are Two Point Attempts")
print(NCTDA, "% of shots bt Team A are Non Corner Three Attempts")
print("And", CTDA, "% of shots by Team A are Corner Three Attempts")

#Team B

#Set Variables for Team B

ThPMB= 0     #Three Point Make
ThPAB = 0    #Three Point Attempt
FGMB = 0     #Field Goal Make
FGAB = 0     #Field Goal Attempt
NCThB = 0    #NonCorner Three Make
NCThAB = 0   #NonCorner Three Attempt
TwPMB = 0    #Two point Make
TwPAB = 0    #Two Point Attempt
CThMB = 0    #Corner Three Make
CThAB = 0    #Corner Three Attempt

#Loop

for i in range(280,560):

    dist = math.sqrt(math.pow(x[i], 2) + math.pow(y[i], 2))
    #print()
    #print(dist)

    if fgmade[i] == 1:
        if y[i] > 7.8 and dist > 23.75:
            ThPMB = ThPMB + 1
            ThPAB = ThPAB + 1
            FGMB = FGMB + 1
            FGAB = FGAB + 1
            NCThB = NCThB + 1
            NCThAB = NCThAB + 1
        elif y[i] < 7.8 and x[i] > 22:
            ThPMB = ThPMB + 1
            ThPAB = ThPAB + 1
            FGMB = FGMB + 1
            FGAB = FGAB + 1
            CThMB = CThMB + 1
            CThAB = CThAB + 1
        else:
            FGMB = FGMB + 1
            FGAB = FGAB + 1
            TwPMB=TwPMB + 1
            TwPAB = TwPAB + 1
    else:
        if y[i] < 7.8 and x[i] > 22:
            CThAB = CThAB + 1
            FGAB = FGAB + 1
        elif y[i] > 7.8 and dist > 23.75:
            NCThAB = NCThAB + 1
            FGAB = FGAB + 1
        else:
            TwPAB = TwPAB +1
            FGAB = FGAB + 1


eFGB = (((FGMB+(0.5*ThPMB))/FGAB)*100)
print("The effective field goal percentage of Team B is", eFGB, "%")

#Shot distributions

TPDB = TwPAB / FGAB
NCTDB = NCThAB / FGAB
CTDB = CThAB / FGAB

print(TPDB, "% of shots by Team B are Two Point Attempts")
print(NCTDB, "% of shots by Team B are Non Corner Three Attempts")
print("And", CTDB, "% of shots by Team B are Corner Three Attempts")

#FG Percentages

TweFGB = (TwPMB/TwPAB)
print("The effective field goal percentage of Team B in the Two Point zone is", TweFGB, "%")
CeFGB = (CThMB/CThAB)
print("The effective field goal percentage of Team B in the Corner Three zone is", CeFGB, "%")
NeFGB = (NCThB/NCThAB)
print("The effective field goal percentage of Team B in the NonCorner Three zone is", NeFGB, "%")

