def bfs_to_list(self):
    temp = self.root
    arr = list()
    if temp:
        q = deque()
        q.append(temp)
        while q:
            elem = q.popleft()
            arr.append(elem.value)
            if elem.left:
                q.append(elem.left)
            if elem.right:
                q.append(elem.right)
    return arr