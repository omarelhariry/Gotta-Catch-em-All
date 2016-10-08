import queue;

class PriorityW(queue.PriorityQueue):
    def __init__(self):
        queue.PriorityQueue.__init__(self)
        self.counter = 0
        self.lower = 0
        self.upper = 0

    def put(self, item, priority):
        queue.PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1
        if priority > self.upper :
            self.upper = priority;
        if priority < self.lower :
            self.lower = priority;
        

    def get(self, *args, **kwargs):
        _, _, item = queue.PriorityQueue.get(self, *args, **kwargs)
        return item

