import random;
from cell import cell;
class maze(object):

    def randomize(self):
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

               
    def constant(self):
        self.columns = 5;
        self.rows = 5;
        self.map = [[0 for x in range(self.rows)] for y in range(self.columns)] ;
        self.map[0][0] =  cell(1,1,0,0);
        self.map[1][0] =  cell(0,1,1,0);
        self.map[2][0] =  cell(1,1,0,1);
        self.map[3][0] =  cell(0,1,0,1);
        self.map[4][0] =  cell(0,1,1,0);

        self.map[0][1] =  cell(1,0,1,1);
        self.map[1][1] =  cell(1,0,0,0);
        self.map[2][1] =  cell(0,1,1,0);
        self.map[3][1] =  cell(1,1,0,1);
        self.map[4][1] =  cell(0,0,1,0);

        self.map[0][2] =  cell(1,1,0,0);
        self.map[1][2] =  cell(0,0,1,0);
        self.map[2][2] =  cell(1,0,0,1);
        self.map[3][2] =  cell(0,1,1,0);
        self.map[4][2] =  cell(1,0,1,0);

        self.map[0][3] =  cell(1,0,1,1);
        self.map[1][3] =  cell(1,0,0,0);
        self.map[2][3] =  cell(0,1,1,1);
        self.map[3][3] =  cell(1,0,1,0);
        self.map[4][3] =  cell(1,0,1,0);

        self.map[0][4] =  cell(1,1,0,1);
        self.map[1][4] =  cell(0,0,1,1);
        self.map[2][4] =  cell(1,1,0,1);
        self.map[3][4] =  cell(0,0,0,1);
        self.map[4][4] =  cell(0,0,1,1);




                   


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
x.constant();
x.printMaze();



