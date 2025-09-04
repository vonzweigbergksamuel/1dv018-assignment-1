class QuickFind:
    def __init__(self, length: int):
        self.parent = list(range(length))

    def find(self, a: int, b: int):
        return self.parent[a] == self.parent[b]

    def union(self, a: int, b: int):
        a_id, b_id = self.parent[a], self.parent[b]

        for i in range(len(self.parent)):
            value = self.parent[i]
            if value == a_id:
                self.parent[i] = b_id
