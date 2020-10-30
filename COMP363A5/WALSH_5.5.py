#COMP 363 Assignment 5: Counting
#Thomas Walsh
#The approach I took when coding this was that in my interpretation of the question
#there were 2 conditions required to determine whether or not a triplet was a valid
#answer.
#Condition 1: There must be one gene in the triplet where all healhy people
#have the same value (whether it be 0 or 1)
#Condition 2: Every diseased column must have at least one instance of the opposite
#of the healthy people's shared trait

import csv
from itertools import combinations

#TODO: Add comments

def main():
    with open("COMP363A5/data.csv") as csvfile:
        data = csv.reader(csvfile, delimiter = ",")
        x = 0
        healthy, sick, totalRows = [], [], []
        for row in data:
            if x == 0:
                for num in range(1,11):
                    if row[num] == "H":
                        healthy.append(num)
                    else:
                        sick.append(num)
                x = 1
            elif x == 1:
                x += 1
            elif x == 20:
                x+=1
            else:
                totalRows.append(row)
        combos = combinations(totalRows, 3)
        answer = []
        counter = 0
        for triplet in combos:
            htrigene = []
            strigene = []
            for row in triplet:
                subh = []
                subs = []
                answer.append(row[0])
                for index in healthy:
                    subh.append(row[index])
                for index in sick:
                    subs.append(row[index])
                htrigene.append(subh)
                strigene.append(subs)
            check1 = 0
            save = 2
            for gene in htrigene:
                check1 = 1
                save = gene[0]
            if check1 == 1:
                if save == 1:
                    save = 0
                else:
                    save = 1
            check2 = 0
            for gene in strigene:
                if str(save) in gene:
                    check2 += 1
            if check1 == 1 and check2 == 3:
                counter += 1
            
        print(counter)
            
                
        
main()
