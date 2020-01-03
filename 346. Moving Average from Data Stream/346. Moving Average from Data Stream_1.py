class MovingAverage:
    
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        self.size = size
        self.count = 0
        self.total = 0
        

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.count += 1
        tail = self.queue.popleft() if self.count > self.size else 0
        self.total = self.total - tail + val
        return self.total/min(self.count,self.size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)