#!/usr/bin/env python3
# Aug. 7, 2016. CYT.
import Group
from operator import attrgetter
from myRandom import myRandom
import os.path

myRandom = myRandom()
nameList = []
for line in open('NameList.txt','r'):
   nameList.append(Group.Person(line))

nameList.sort()

# Analyze the raw data
group = [] 
for i in range(0,15):
   group.append(Group.Group())
totalMale = 0
groupedMale = 0
groupedFemale = 0
for p in nameList:
   if p.group != -1:
      group[p.group-1].add(p)
   if p.gender == '男':
      totalMale += 1
      if p.group != -1:
         groupedMale += 1
   else:
      if p.group != -1:
         groupedFemale += 1
totalFemale = len(nameList) - totalMale

nameList[0:totalMale] = myRandom.shuffle(nameList[0:totalMale])
nameList[totalMale:] = myRandom.shuffle(nameList[totalMale:])

# Start grouping/ Grouping males
rnd = 0
startGroupIndex = myRandom.randrange(0,15)
groupIndex = startGroupIndex
while groupedMale < totalMale:
   if groupIndex == startGroupIndex:
      rnd += 1
   if group[groupIndex].male >= rnd:
      groupIndex = (groupIndex+1)%15
      continue
   nameIndex = myRandom.randrange(0,totalMale)
   while nameList[nameIndex].group != -1:
      nameIndex = myRandom.randrange(0,totalMale)
   nameList[nameIndex].group = groupIndex+1
   group[groupIndex].add(nameList[nameIndex])
   groupIndex = (groupIndex+1)%15
   groupedMale += 1

# Grouping Females
rnd = 0
startGroupIndex = groupIndex
while groupedFemale < totalFemale:
   if groupIndex == startGroupIndex:
      rnd += 1
   if group[groupIndex].female >= rnd:
      groupIndex = (groupIndex+1)%15
      continue
   nameIndex = myRandom.randrange(totalMale, totalMale+totalFemale)
   while nameList[nameIndex].group != -1:
      nameIndex = myRandom.randrange(totalMale, totalMale+totalFemale)
   nameList[nameIndex].group = groupIndex+1
   group[groupIndex].add(nameList[nameIndex])
   groupIndex = (groupIndex+1) % 15
   groupedFemale += 1

# Try and find appropriate output file name:
num = 0
filename = 'Result' + str(num) + '.txt'
while os.path.isfile(filename):
   num += 1
   filename = 'Result' + str(num) + '.txt'

# Write the result to a new file
fout = open(filename,'w')
for p in group: 
   p.sort()
   fout.write(str(p) + '\n')
fout.close()
