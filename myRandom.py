import random
class myRandom:
   def __init__(self):
      self.rnd = random.SystemRandom()
   def randrange(self,start,stop):
      self.rnd = random.SystemRandom(self.rnd.randrange(0,2147483647))
      return self.rnd.randrange(start,stop)
   def randint(self,start,stop):
      self.rnd = random.SystemRandom(self.rnd.randrange(0,2147483647))
      return self.rnd.randint(start,stop)
   def shuffle(self,ll):
      self.rnd.shuffle(ll)
      return ll
