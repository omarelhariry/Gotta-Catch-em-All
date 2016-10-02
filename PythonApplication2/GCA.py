import searchProblem;
import searchNode;
import state;
from multiprocessing import Queue
class GCA(searchProblem.searchProblem):
    """description of class"""
    print("mahmoud");
    
    def __init__(self):
        self.myname = "GCA"

    def BFS(self, maze, visualize):
        #maze = [0 for x in range][];
        w, h = 10, 10; 
        m = [[0 for x in range(w)] for y in range(h)];
        i, j = 1, 1;
        cell = m[i][j];

        q = Queue();
        from state import state;
        s = state(1, 1);
        parent = None;
        operator = [1,0,1,0]; # cell.surroundings
        depth = 0;
        cost = 0;
        from searchNode import searchNode;  
        n = searchNode(s, parent, operator, depth, cost);
        q.put(n);
        i = 0;

        while q.qsize() != 0 :
            n = q.get();
            x = n.state.x;
            y = n.state.y;
            # check if goal reached 
            print("depth of "+`i`+"th element is "+`n.depth`);
            i = i + 1;
            if n.operator[0] == 1 :
                s = state(x-1, y);
                parent = n;
                operator = [0,0,1,0]; # m[x-1][y].surroundings;
                depth = n.depth + 1;
                cost = n.cost + 1;
                n1 = searchNode(s, parent, operator, depth, cost);
                q.put(n1);
                print("0: "+`n1.depth`);

            if n.operator[1] == 1 :
                s = state(x, y+1);
                parent = n;
                operator = [0,0,0,0]; # m[x][y+1].surroundings;
                depth = n.depth + 1;
                cost = n.cost + 1;
                n1 = searchNode(s, parent, operator, depth, cost);
                q.put(n1);
                print("1: "+`n1.depth`);

            if n.operator[2] == 1 :
                s = state(x+1, y);
                parent = n;
                operator = [0,0,0,0]; # m[x+1][y].surroundings;
                depth = n.depth + 1;
                cost = n.cost + 1;
                n1 = searchNode(s, parent, operator, depth, cost);
                q.put(n1);
                print("2: "+`n1.depth`);

            if n.operator[3] == 1 :
                s = state(x, y-1);
                parent = n;
                operator = [0,0,0,0]; # m[x][y-1].surroundings;
                depth = n.depth + 1;
                cost = n.cost + 1;
                n1 = searchNode(s, parent, operator, depth, cost);
                q.put(n1);
                print("3: "+`n1.depth`);
            
        
        print("BFS");

    def search(self, maze, strategy, visualize):
        print("ahmed");
        def switch(x):
            return {
                'a': self.BFS(maze, visualize),
            }[x]
        switch(strategy);
    
gca = GCA();
gca.search('', 'a' , '');


