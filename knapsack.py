import random

def dec2bin(x, n):
    if x == 0:
        return [0]
    bit = []
    i = 0
    while i < n:
        bit.append(x % 2)
        x >>= 1
        i += 1
    return bit[::-1]

class Thing:
    def __init__(self, idx: int, weight: int, price: int) -> None:
        self.idx = idx
        self.weight = weight
        self.price = price
        self.approx = price/weight

class Knapsack:
    def __init__(self) -> None:
        self.elements = []
        self.n = 0
        self.b = 0
        self.m = []
        self.sol_array = []

    def create_from_list(self, b: int, arr: list) -> None:
        self.b = b
        self.n = len(arr)
        i = 1
        for pair in arr:
            el = Thing(i, pair[0], pair[1])
            self.elements.append(el)
            i += 1

    def create_random(self, n: int, b: int=0) -> None:
        if b == 0:
            b = random.randint(n, 3*n)
        self.b = b
        self.n = n
        for i in range(1, n+1):
            r1 = random.randint(1, b)
            r2 = random.randint(1, 3*n)
            el = Thing(i, r1, r2)
            self.elements.append(el)

    def brute_force(self):
        fmax = 0
        solution = []
        for i in range(1, 2**self.n-1):
            bin_hack = dec2bin(i, self.n)
            w = 0
            f = 0
            for i in range(self.n):
                if bin_hack[i] == 1:
                    w += self.elements[i].weight
                    f += self.elements[i].price
            if w <= self.b and f > fmax:
                fmax = f
                sol_str = bin_hack

        for i in range(self.n):
            if sol_str[i] == 1:
                solution.append(i+1)

        return solution, fmax, w # if fmax = 0 then the solution is invalid

    def greedy(self):
        greedy_array = sorted(self.elements, key=lambda thing: thing.approx, reverse=True)
        w = 0
        fmax = 0
        solution = []
        for el in greedy_array:
            if el.weight + w <= self.b:
                w += el.weight
                fmax += el.price
                solution.append(el.idx)
                if w == self.b:
                    break
        return solution, fmax, w # if fmax = 0 then the solution is invalid

    def __dynamic_helper(self, i: int, j: int):
        if i == 0:
            return []
        if self.m[i][j] > self.m[i-1][j]:
            arr = [i]
            arr.extend(self.__dynamic_helper(i-1, j-self.elements[i-1].weight))
            return arr
        else:
            arr = self.__dynamic_helper(i-1, j)
            return arr


    def dynamic(self):
        self.m = [[0 for _ in range(self.b+1)] for _ in range(self.n+1)]
        for i in range(1, self.n+1):
            for j in range(1, self.b+1):
                if self.elements[i-1].weight > j:
                    self.m[i][j] = self.m[i-1][j]
                else:
                    self.m[i][j] = max(self.m[i-1][j], self.m[i-1][j-self.elements[i-1].weight] + self.elements[i-1].price)
        
        fmax = self.m[self.n][self.b]
        solution = []
        if fmax == 0:
            return solution, fmax, 0 # invalid solution return
        else:
            solution = self.__dynamic_helper(self.n, self.b)
            w = 0
            for el in solution:
                w += self.elements[el-1].weight
            return solution, fmax, w


if __name__ == '__main__':
    ks = Knapsack()
    arr = [[2, 4], [1, 3], [4, 6], [4, 8]]
    ks.create_from_list(8, arr)
    print(ks.brute_force())
    print(ks.greedy())
    print(ks.dynamic())