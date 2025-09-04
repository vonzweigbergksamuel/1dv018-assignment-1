class WeightedCompressedQuickUnion:
    def __init__(self, length: int):
        self.parent = list(range(length))
        self.size = [1] * length

    def find(self, element: int):
        if element != self.parent[element]:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, element1: int, element2: int):
        root1, root2 = self.find(element1), self.find(element2)

        if root1 == root2:
            return

        if self.size[root1] < self.size[root2]:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]

    def connected(self, element1: int, element2: int):
        return self.find(element1) == self.find(element2)

    def count(self):
        roots = {self.find(i) for i in range(len(self.parent))}
        return len(roots)
