import random;
class cell(object):
   def __init__(self, left, up, right, down):
       self.surroundings = [left,up,right,down];
       if(left > 1):
        self.surroundings[0] = random.randint(0,1);
       if(up > 1):
        self.surroundings[1] = random.randint(0,1);
       if(right > 1):
        self.surroundings[2] = random.randint(0,1);
       if(down > 1):
        self.surroundings[3] = random.randint(0,1);


