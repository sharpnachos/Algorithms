#COMP 363 Assignment 5: Counting
#Thomas Walsh
#This program will analyze data from a csv

import csv

#TODO: Add comments

def readcsv():
    with open("COMP363A5/data.csv") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        x = 0
        healthy = []
        sick = []
        for row in data:
            if x == 0:
                for num in range(1, 7):
                    if row[num] == "H":
                        healthy.append(num)
                    else:
                        sick.append(num)
                x = 1
            elif x == 1:
                x = 2
            else:
                x += 1
                subh = []
                subs = []
                check1, check2, check3 = 1,1,1
                for index in healthy:
                    subh.append(row[index])
                for index in sick:
                    subs.append(row[index])
                for gene in range(0,(len(subh)-1)):
                    if subh[gene] != subh[gene + 1]:
                        check1 = 0
                        break
                for gene in range(0,(len(subs)-1)):
                    if subs[gene] != subs[gene + 1]:
                        check2 = 0
                        break
                if subh[0] == subs[0]:
                    check3 = 0
                if check1 == 1 and check2 == 1 and check3 == 1:
                    print("Gene " + str(x - 2) + ": Disease " + str(subs[0]) + "; Healthy " + str(subh[0]))
                
readcsv()
