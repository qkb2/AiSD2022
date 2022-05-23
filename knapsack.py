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
        i = 0
        for pair in arr:
            el = Thing(i, pair[0], pair[1])
            self.elements.append(el)
            i += 1

    def brute_force(self):
        fmax = 0
        solution = 0
        for i in range(1, 2**self.n-1):
            bin_hack = bin(i)
            bin_hack = bin_hack[2:]
            w = 0
            f = 0
            for i in range(self.n):
                if bin_hack[i] == '1':
                    w += self.elements[i].weight
                    f += self.elements[i].price
            if w <= self.b and f > fmax:
                fmax = f
                solution = bin_hack

        return solution, fmax # if fmax = 0 then the solution is invalid

    def greedy(self):
        greedy_array = sorted(self.elements, key=lambda thing: thing.approx)
        w = 0
        fmax = 0
        solution = ''
        for el in greedy_array:
            if el.weight + w <= self.b:
                w += el.weight
                fmax += el.price
                solution += '1'
                if w == self.b:
                    break
            else:
                solution += '0'

        while len(solution) != self.n:
            solution += '0'
        return solution, fmax # if fmax = 0 then the solution is invalid

    def __dynamic_helper(self, i: int, j: int):
        if i == 0:
            return
        if self.m[i, j] > self.m[i-1, j]:
            self.__dynamic_helper(i-1, j-self.elements[i].weight)
            self.sol_array[i] = 1
            return
        else:
            self.__dynamic_helper(i-1, j)
            return


    def dynamic(self):
        self.m = [[0 for _ in range(self.b+1)] for _ in range(self.n+1)]
        for i in range(1, self.n+1):
            for j in range(1, self.b+1):
                if self.elements[i].weight > j:
                    self.m[i, j] = self.m[i-1, j]
                else:
                    self.m[i, j] = max(self.m[i-1, j], self.m[i-1, j-self.elements[i].weight] + self.elements[i].price)
        
        fmax = self.m[self.n][self.b]
        solution = ''
        if fmax == 0:
            solution = self.n * '0'
            return solution, fmax # invalid solution return
        else:
            self.sol_array = [0 for _ in range(self.n+1)]
            self.__dynamic_helper(self.n, self.b)
            for i in self.sol_array[1:]:
                if i == 1:
                    solution += '1'
                else:
                    solution += '0'
            return solution, fmax
