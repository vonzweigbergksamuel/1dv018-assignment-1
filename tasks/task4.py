def task4():
    print("================")
    print("Task 4 - Brute Force 3 Sum")
    print("================")

    array = [-1, 0, 1, 2, -1, -4]
    brute_force_3_sum = BruteForce3Sum(array)
    triplets = brute_force_3_sum.find_triplets()
    print(triplets)


class BruteForce3Sum:
    def __init__(self, array: list[int]):
        self.array = array

    def find_triplets(self) -> list[tuple[int, int, int]]:
        triplets = []
        for i in range(len(self.array)):
            for j in range(i + 1, len(self.array)):
                for k in range(j + 1, len(self.array)):
                    if self.array[i] + self.array[j] + self.array[k] == 0:
                        triplet = tuple(
                            sorted([self.array[i], self.array[j], self.array[k]])
                        )
                        if triplet not in triplets:
                            triplets.append(triplet)
        return triplets
