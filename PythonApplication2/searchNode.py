class searchNode(object):
    """description of class"""

    def __init__(self, state, parent, operator, depth, cost, pokemonsRemaining):     
        self.state = state;
        self.parent = parent;
        self.operator = operator;
        self.depth = depth;
        self.cost = cost;
        self.pokemonsRemaining = pokemonsRemaining;


