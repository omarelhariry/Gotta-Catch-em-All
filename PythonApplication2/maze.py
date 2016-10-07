import random;
from cell import cell;
class maze(object):

    def randomize(self):
        self.rows = random.randint(1,100);
        self.columns = random.randint(1,100);
        self.currentAgentPosition = random.randint(0,self.rows-1), random.randint(0,self.columns-1);
        self.endPosition = random.randint(0,self.rows-1), random.randint(0,self.columns-1);
        self.eggsKilometers = random.randint(1,100);         
        self.map = [[0 for x in range(self.columns)] for y in range(self.rows)] ;
        self.pokemons = 0;
        for row in range(len(self.map)):
            for column in range(len(self.map[row])):
                self.map[row][column] = cell(1,1,1,1);
                if(self.map[row][column].hasPokemon()):
                    self.pokemons +=1;
        
        currentCell = random.randint(0,self.rows-1), random.randint(0,self.columns - 1);
        self.map[currentCell[0]][currentCell[1]].visited = True;
        unvisitedCells = self.columns * self.rows - 1;
        cellsStack = [];
        while unvisitedCells > 0:
            unVisitedNeighbors = self.getUnVisitedNeighbors(currentCell[0], currentCell[1]);
            if unVisitedNeighbors:
                randomUnvisistedCell = unVisitedNeighbors[random.randint(0,len(unVisitedNeighbors) - 1)];
                cellsStack.append(currentCell);
                self.map[currentCell[0]][currentCell[1]].removeWall(randomUnvisistedCell);
                if randomUnvisistedCell == 0:
                    currentCell = currentCell[0], currentCell[1] - 1;
                    self.map[currentCell[0]][currentCell[1]].removeWall(2);
                if randomUnvisistedCell == 1:
                    currentCell = currentCell[0] - 1, currentCell[1];
                    self.map[currentCell[0]][currentCell[1]].removeWall(3);
                if randomUnvisistedCell == 2:
                    currentCell = currentCell[0], currentCell[1] + 1;
                    self.map[currentCell[0]][currentCell[1]].removeWall(0);
                if randomUnvisistedCell == 3:
                    currentCell = currentCell[0] + 1, currentCell[1];
                    self.map[currentCell[0]][currentCell[1]].removeWall(1);
                self.map[currentCell[0]][currentCell[1]].visited = True;
                unvisitedCells -= 1;
            elif cellsStack:
                currentCell = cellsStack.pop();





                    

    def getUnVisitedNeighbors(self, i, j):
        unvisitedNeighbors = [];
        if j > 0:
            if not self.map[i][j-1].visited:
                unvisitedNeighbors.append(0); #left
        if j < self.columns - 1: 
            if not self.map[i][j+1].visited:
                unvisitedNeighbors.append(2); #right
        if i > 0:
            if not self.map[i-1][j].visited:
                unvisitedNeighbors.append(1); #up
        if i < self.rows - 1:
            if not self.map[i+1][j].visited:
                unvisitedNeighbors.append(3); #down
        return unvisitedNeighbors;
            
                                            
             
                              
    def constant(self):
        self.columns = 5;
        self.rows = 5;
        self.map = [[0 for x in range(self.rows)] for y in range(self.columns)] ;
        self.map[0][0] =  cell(1,1,0,0);
        self.map[0][1] =  cell(0,1,1,0);
        self.map[0][2] =  cell(1,1,0,1);
        self.map[0][3] =  cell(0,1,0,1);
        self.map[0][4] =  cell(0,1,1,0);

        self.map[1][0] =  cell(1,0,1,1);
        self.map[1][1] =  cell(1,0,0,0);
        self.map[1][2] =  cell(0,1,1,0);
        self.map[1][3] =  cell(1,1,0,1);
        self.map[1][4] =  cell(0,0,1,0);

        self.map[2][0] =  cell(1,1,0,0);
        self.map[2][1] =  cell(0,0,1,0);
        self.map[2][2] =  cell(1,0,0,1);
        self.map[2][3] =  cell(0,1,1,0);
        self.map[2][4] =  cell(1,0,1,0);

        self.map[3][0] =  cell(1,0,1,1);
        self.map[3][1] =  cell(1,0,0,0);
        self.map[3][2] =  cell(0,1,1,1);
        self.map[3][3] =  cell(1,0,1,0);
        self.map[3][4] =  cell(1,0,1,0);

        self.map[4][0] =  cell(1,1,0,1);
        self.map[4][1] =  cell(0,0,1,1);
        self.map[4][2] =  cell(1,1,0,1);
        self.map[4][3] =  cell(0,0,0,1);
        self.map[4][4] =  cell(0,0,1,1);



                   


    def printMaze(self):
        for row in range(len(self.map)):
            toBePrinted = [];
            for column in range(len(self.map[row])):
                toBePrinted.append(self.map[row][column].getCell());                 
                if(column == self.columns - 1):
                    print(toBePrinted);



x = maze();
#x = cell(1,0,1,0);
#print(x.getCell());
x.randomize();
#x.map[0][0].removeWall(0);
#print(x.map[88][98].getCell());
x.printMaze();
#print(x.map[8][9].getCell());


