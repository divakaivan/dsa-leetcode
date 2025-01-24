class StockSpanner:
    def __init__(self):
        # Stack to store pairs of (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1  
        # ["StockSpanner","next","next","next","next","next","next","next","next"]
        # [[],[100],[80],[60],[70],[60],[75],[85],[80]]
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        
        return span
        
        # [(100, 1)]
        # [(100, 1), (80, 1)]
        # [(100, 1), (80, 1), (60, 1)]
        # [(100, 1), (80, 1), (70, 2)]
        # [(100, 1), (80, 1), (70, 2), (60, 1)]
        # [(100, 1), (80, 1), (75, 4)]
        # [(100, 1), (85, 6)]
        # [(100, 1), (85, 6), (80, 1)]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)