class FolderCrawler:
    def __init__(self):
        self.stack = []
        self.length = 0

    def minOperations(self, logs: list[str]) -> int:
        for op in logs:
            if op == "../":
                if self.length > 0:
                    self.stack.pop()
                    self.length -= 1
            elif op == "./":
                continue
            else:
                self.stack.append(op)
                self.length += 1
        return self.length
    
log1 = ["d1/","d2/","../","d21/","./"]
crawler1 = FolderCrawler()
assert crawler1.minOperations(log1) == 2

log2 = ["d1/","d2/","./","d3/","../","d31/"]
crawler2 = FolderCrawler()
assert crawler2.minOperations(log2) == 3

log3 = ["d1/","../","../","../"]
crawler3 = FolderCrawler()
assert crawler3.minOperations(log3) == 0