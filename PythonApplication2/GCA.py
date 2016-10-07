import searchProblem;
import searchNode;
import state;
import cell;
import PriorityW;
#import maze;
from multiprocessing import Queue
class GCA(searchProblem.searchProblem):
    """description of class"""
    
    def __init__(self):
        self.myname = "GCA"

    def search(self, maz, strategy, visualize):
        print("ahmed");
        """def switch(x):
            return {
                #'a': self.BFS(maze, visualize),
                'b': self.Astar(maze, visualize),
            }[x]
        switch(strategy);"""
        #maze = [0 for x in range][];
        w, h = 10, 10; 
        m = [[0 for x in range(w)] for y in range(h)];
        #from maze import maze;
        #m = maze(); 
        i, j = 1, 1;
        from cell import cell
        cell2 = m[i][j];
        pokemons = 10;
        endX = 5;
        endY = 5;
        km = 10;
        from Queue import PriorityQueue
        from PriorityW import PriorityW
        #q = PriorityQueue();
        w = PriorityW();
        from state import state;
        s = state(i, j);
        parent = None;
        operator = [0,0,0,0]; 
        depth = 0;
        cost = 0;
        pokemonsRemaining = pokemons;
        from searchNode import searchNode;  
        n = searchNode(s, parent, operator, depth, cost, pokemonsRemaining);
        w.put(n, 0);
        c = 0;
        goal = None;
        print("lesgo");

        while w.qsize() != 0 :
            n = w.get();
            x = n.state.x;
            y = n.state.y;
            cell2 = m[x][y];
            pokemonsRemaining = n.pokemonsRemaining - cell2.pokemon;
            print("currently at "+str(x)+" and "+str(y));
            c = c + 1;
            # check if goal reached
            #if goalTest(m, x, y, pokemonsRemaining) :
            if pokemonsRemaining == 0 and x == endX and y == endY and n.cost >= km :
                goal = n;
                break;
            #if visualize :
                #printMap(m, x, y); 
            q = Queue();
            if cell2.surroundings[0] == 1 :
                s = state(x-1, y);
                parent = n;
                operator = [1,0,0,0]; 
                depth = n.depth + 1;
                cost = n.cost + 1;
                n1 = searchNode(s, parent, operator, depth, cost, pokemonsRemaining);
                q.put(n1);
                print("0: "+str(n1.depth));

            if cell2.surroundings[1] == 1 :
                s = state(x, y+1);
                parent = n;
                operator = [0,1,0,0]; 
                depth = n.depth + 1;
                cost = n.cost + 1;
                n1 = searchNode(s, parent, operator, depth, cost, pokemonsRemaining);
                q.put(n1);
                print("1: "+str(n1.depth));

            if cell2.surroundings[2] == 1 :
                s = state(x+1, y);
                parent = n;
                operator = [0,0,1,0]; 
                depth = n.depth + 1;
                cost = n.cost + 1;
                n1 = searchNode(s, parent, operator, depth, cost, pokemonsRemaining);
                q.put(n1);
                print("2: "+str(n1.depth));

            if cell2.surroundings[3] == 1 :
                s = state(x, y-1);
                parent = n;
                operator = [0,0,0,1]; 
                depth = n.depth + 1;
                cost = n.cost + 1;
                n1 = searchNode(s, parent, operator, depth, cost, pokemonsRemaining);
                q.put(n1);
                print("3: "+str(n1.depth));
            
            while q.qsize() != 0 :
                n1 = w.get();
                if strategy == "BF" :
                    w.put(n1, w.upper + 1);
                if strategy == "DF" :
                    w.put(n1, w.lower - 1);
                if strategy == "UC" :
                    w.put(n1, n1.cost);
                if strategy == "GR1" :
                    w.put(n1, h1(n1));
                if strategy == "GR2" :
                    w.put(n1, h2(n1));
                if strategy == "GR3" :
                    w.put(n1, h3(n1));
                if strategy == "AS1" :
                    w.put(n1, n1.cost + h1(n1));
                if strategy == "AS2" :
                    w.put(n1, n1.cost + h2(n1));
                if strategy == "AS3" :
                    w.put(n1, n1.cost + h3(n1));
            
        if goal != None :
            solCost = goal.cost;
            nodeCount = c;
            moves = [];
            n = goal;
            while n.parent != None :
                if n.operator == [1,0,0,0] :
                    moves.append("Left");
                if n.operator == [0,1,0,0] :
                    moves.append("Up");
                if n.operator == [0,0,1,0] :
                    moves.append("Right");
                if n.operator == [0,0,0,1] :
                    moves.append("Down");
                n = n.parent;
            moves = moves.reverse;
            return [moves, solCost, nodeCount];
        
        print("no solution");
        return None;

    def h1(n1):
        return n1.depth;
    
gca = GCA();
res = gca.search('', 'a' , '');
print("he77");
print(res[0]);
print(res[1]);
print(res[2]);


