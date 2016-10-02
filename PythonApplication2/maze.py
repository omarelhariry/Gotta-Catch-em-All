import random;
class maze(object):

    def __init__(self):
        self.columns = random.randint(1,100);
        self.rows = random.randint(1,100);
        self.map = [[0 for x in range(self.rows)] for y in range(self.columns)] ;
        i = 0;
        for row in range(len(self.map)):
            for column in range(len(self.map[row])):
                self.map[row][column] = i;


    def printMaze(self):
        for row in range(len(self.map)):
            for column in range(len(self.map[row])):
                print( self.map[row][column]); 


x = maze();
x.printMaze();


