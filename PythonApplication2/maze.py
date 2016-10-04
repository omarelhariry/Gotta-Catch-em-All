import random;
from cell import cell;
class maze(object):

    def __init__(self):
        self.columns = random.randint(1,10);
        self.rows = random.randint(1,10);
        self.map = [[0 for x in range(self.rows)] for y in range(self.columns)] ;
        i = 0;
        for row in range(len(self.map)):
            for column in range(len(self.map[row])):
                left = 2;
                up = 2;
                right = 2;
                down = 2;
                if(column == 0):
                    left = 1;
                if(column == self.columns - 1):
                    right = 1
                if(row == 0):
                    up = 1;
                if(row == self.rows - 1):
                    down = 1;
                if(row > 0):
                    up = self.map[row-1][column].surroundings[3];
                if(column > 0):
                    left = self.map[row][column-1].surroundings[2];
                self.map[row][column] = cell(left,up,right,down);

               

                   


    def printMaze(self):
        prevRow = 0;
        print2 = "";
        for row in range(len(self.map)):
            for column in range(len(self.map[row])):
                print2 += self.map[row][column].getCell();                 
                if(row > prevRow):
                    prevRow = row;
                    print(print2);
                    print2 = "";


x = maze();
#x = cell(1,0,0,0);
#print(x.getCell());
x.printMaze();



