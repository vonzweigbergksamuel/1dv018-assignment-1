def task5():
    print("================")
    print("Task 5 - Three Sum")
    print("================")

    array = [-1, 0, 1, 2, -1, -4]
    three_sum = ThreeSum(array)
    triplets = three_sum.find_triplets()
    print(triplets)


class ThreeSum:
    def __init__(self, array: list[int]):
        self.array = sorted(array)

    def find_triplets(self) -> list[tuple[int, int, int]]:
        triplets = []
        n = len(self.array)

        for i in range(n):
            if i > 0 and self.array[i] == self.array[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = self.array[i] + self.array[left] + self.array[right]
                if total == 0:
                    triplets.append(
                        (self.array[i], self.array[left], self.array[right])
                    )
                    left += 1
                    right -= 1
                    while left < right and self.array[left] == self.array[left - 1]:
                        left += 1
                    while left < right and self.array[right] == self.array[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return triplets
