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
       randomPokemonProbability = random.randint(1,10);
       if(randomPokemonProbability <= 1):
        self.pokemon = 1;
       else:
        self.pokemon = 0; 
       self.visited = False;  

    def hasPokemon(self):
        return self.pokemon == 1;
    def removeWall(self, wallNumber): # 0 --> left 1 --> up 2 --> right 3 --> down
        self.surroundings[wallNumber] = 0;

    def getCell(self):
        return "["+str(self.surroundings[0]) + ", "+  str(self.surroundings[1])+", "+ str(self.surroundings[2])+", "+ str(self.surroundings[3])+"]"+ str(self.hasPokemon());

