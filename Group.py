#!/usr/bin/env python3
# Aug. 7, 2016. CYT.

SEP = '\t'
class Person:
   def __init__(self,s):
      s = s.split('\n')[0]
      tokens = s.split(SEP)
      self.ID = int(tokens[0])
      self.group = -1 if tokens[1]=='' else int(tokens[1])
      self.name = tokens[2]
      self.gender = tokens[3]
      self.other_information = tokens[4:]
   def __str__(self):
      ret = SEP.join([str(self.ID), str(self.group), self.name, self.gender] + self.other_information) 
      return ret
   def __repr__(self):
      return self.__str__()
   def __lt__(self,other):
      if self.gender == other.gender:
         return self.ID < other.ID
      else:
         return self.gender == '男'

class Group:
   def __init__(self):
      self.male = 0
      self.female = 0
      self.data = []
   def add(self,person):
      if person.gender == '男':
         self.male += 1
      elif person.gender == '女':
         self.female += 1
      else:
         print('Error: No gender -- \n\t{0}'.format(person))
      self.data.append(person)
   def sort(self):
      self.data.sort()
   def __str__(self):
      ret = ''
      for p in self.data:
         ret += str(p) + '\n'
      ret += 'Male: {0}, Female: {1}, Total: {2}'.format(self.male, self.female, self.male+self.female)
      return ret
   def __repr__(self):
      return self.__str__()
