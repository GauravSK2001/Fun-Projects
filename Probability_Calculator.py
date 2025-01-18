import random

class Hat:
    def __init__(self,**kwarg):
      a=[]
      for key, value in kwarg.items():
        for i in range(value):
          (a).append(str(key))
      self.contents=a
      self.original=a
    def draw(self,N):
      if N >= len(self.contents):
          drawn=self.contents
          self.contents=[]
      else:
        drawn = random.sample(self.contents, k=N)
        for ball in drawn:
            self.contents.remove(ball)           
      return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  N=0
  for i in range(num_experiments):
    hat.contents=(hat.original).copy()
    drawn=hat.draw(num_balls_drawn)
    
    if all(drawn.count(f'{key}')>=value for key,value in expected_balls.items()):
      N+=1
  return N/num_experiments
#
    
      
        
