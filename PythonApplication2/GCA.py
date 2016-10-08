import searchProblem;
import searchNode;
import state;
import cell;
import PriorityW;
import maze;
import queue;
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
        #w, h = 10, 10; 
        #m = [[0 for x in range(w)] for y in range(h)];
        from maze import maze;
        m = maze();
        m.constant();
        i = m.currentAgentPosition[0];
        j = m.currentAgentPosition[1];
        from cell import cell
        cell2 = m.map[i][j];
        pokemons = m.pokemons;
        endX = m.endPosition[0];
        endY = m.endPosition[1];
        km = m.eggsKilometers;
        from PriorityW import PriorityW
        #q = PriorityQueue();
        w = PriorityW();
        from state import state;
        
        s = state(i, j, []);
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
            cell2 = m.map[x][y];
            #if n.state.seen[str(x)+","+str(y)] == True :
            #    continue;
            if cell2.pokemon == 1 and not str(x)+","+str(y) in n.state.seen :
                pokemonsRemaining = n.pokemonsRemaining - 1;
                n.state.seen.append(str(x)+","+str(y));
            #n.state.seen[str(x)+","+str(y)] = True;
            print("currently at "+str(x)+" and "+str(y));
            c = c + 1;
            # check if goal reached
            #if goalTest(m, x, y, pokemonsRemaining) :
            #if pokemonsRemaining == 0 and x == endX and y == endY and n.cost >= km :
            if x == endX and y == endY and n.cost >= km :
                print("goal");
                goal = n;
                break;
            #if visualize :
                #printMap(m, x, y); 
            q = queue.Queue();
            if cell2.surroundings[0] == 0 :
                s = state(x, y-1, n.state.seen);
                parent = n;
                operator = [1,0,0,0]; 
                depth = n.depth + 1;
                cost = n.cost + 1;
                n1 = searchNode(s, parent, operator, depth, cost, pokemonsRemaining);
                q.put(n1);
                print("Left: "+str(n1.depth));

            if cell2.surroundings[1] == 0 :
                s = state(x-1, y, n.state.seen);
                parent = n;
                operator = [0,1,0,0]; 
                depth = n.depth + 1;
                cost = n.cost + 1;
                n1 = searchNode(s, parent, operator, depth, cost, pokemonsRemaining);
                q.put(n1);
                print("Up: "+str(n1.depth));

            if cell2.surroundings[2] == 0 :
                s = state(x, y+1, n.state.seen);
                parent = n;
                operator = [0,0,1,0]; 
                depth = n.depth + 1;
                cost = n.cost + 1;
                n1 = searchNode(s, parent, operator, depth, cost, pokemonsRemaining);
                q.put(n1);
                print("Right: "+str(n1.depth));

            if cell2.surroundings[3] == 0 :
                s = state(x+1, y, n.state.seen);
                parent = n;
                operator = [0,0,0,1]; 
                depth = n.depth + 1;
                cost = n.cost + 1;
                n1 = searchNode(s, parent, operator, depth, cost, pokemonsRemaining);
                q.put(n1);
                print("Down: "+str(n1.depth));
            
            while q.qsize() != 0 :
                n1 = q.get();
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
            print("after hena");
         
        print("after after hena");   
        if goal != None :
            print("solution");
            solCost = goal.cost;
            nodeCount = c;
            moves = [];
            n = goal;
            while n.parent != None :
                if n.operator == [1,0,0,0] :
                    moves.insert(0, "Left");
                    #moves = ["Left"] + moves;
                if n.operator == [0,1,0,0] :
                    moves.insert(0, "Up");
                if n.operator == [0,0,1,0] :
                    moves.insert(0, "Right");
                if n.operator == [0,0,0,1] :
                    moves.insert(0, "Down");
                n = n.parent;
            #moves.reverse;
            return [moves, solCost, nodeCount];
        
        print("no solution");
        return None;

    def h1(n1):
        return n1.depth;
    
gca = GCA();
res = gca.search('', 'BF' , '');
print("he77");
print(res[0]);
print(res[1]);
print(res[2]);


