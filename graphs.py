from copy import deepcopy
import random


def edge_list_to_vertex_list(edge_list: list):
    max_key = 0
    for el in edge_list:
        if el[0] > max_key:
            max_key = el[0]
        if el[1] > max_key:
            max_key = el[1]
    return [i for i in range(max_key+1)]
    # assuming that since it's impossible to create "solitary" nodes via edge list
    # it's better to just create all the possible nodes that could exist



class UndirAdjMatrix():
    def __init__(self) -> None:
        self.V = 0
        self.E = 0
        self.matrix = []
        self.is_visited = [] # vertices start at 0

    def __repr__(self) -> str:
        repr = ''
        for i in range(self.V):
            for j in range(self.V):
                repr += str(self.matrix[i][j])+'\t'
            repr += '\n'
        return repr
    
    def create_from_edge_list(self, edge_list: list, vertex_list: list) -> None:
        self.V = len(vertex_list) # from 0 to n not included
        self.E = len(edge_list)

        self.matrix = [[0 for _ in range(self.V)] for _ in range(self.V)]
        for el in edge_list:
            self.matrix[el[0]][el[1]] = 1
            self.matrix[el[1]][el[0]] = 1

        self.is_visited = [False for _ in vertex_list]

    def create_matrix_wrapper(self, edge_list: list):
        vertex_list = edge_list_to_vertex_list(edge_list)
        self.create_from_edge_list(edge_list, vertex_list)

    def create_random_undir_graph(self, n: int, D: float) -> None:
        self.V = n
        self.E = int(n*(n-1)*D//2)
        self.matrix = [[0 for _ in range(self.V)] for _ in range(self.V)]
        self.is_visited = [False for _ in range(self.V)]
        c = 0
        c_panic = 0
        random.seed()
        while c < self.E and c_panic < 10*self.E:
            c_panic += 1
            x = random.randint(0, self.V-1)
            y = random.randint(0, self.V-1)
            if self.matrix[x][y] == 0 and x != y:
                self.matrix[x][y] = 1
                self.matrix[y][x] = 1
                c += 1

    def __hamiltonian(self, v: int) -> bool:
        self.is_visited[v] = True
        self.visited += 1
        helper_list = self.matrix[v]
        for i in range(self.V):
            if  helper_list[i] == 1 and i == self.start and self.visited == self.V:
                return True
            if helper_list[i] == 1 and not self.is_visited[i]:
                db = self.__hamiltonian(i)
                if db:
                    self.hpath[self.k] = v
                    self.k += 1
                    return True
        self.is_visited[v] = False
        self.visited -= 1
        return False

    def hamiltonian_cycle(self) -> bool:
        self.hpath = [-1 for _ in range(self.V)]
        self.is_visited = [False for _ in range(self.V)]
        self.hpath[0] = 0
        self.start = 0
        self.visited = 0
        self.k = 1
        is_ham = self.__hamiltonian(self.start)
        return is_ham

    def __dfs_euler(self, v: int):
        for u in range(self.V):
            if self.matrix_copy[v][u] == 1:
                self.matrix_copy[v][u] = 0
                self.matrix_copy[u][v] = 0
                self.__dfs_euler(u)
        self.epath.append(v)

    def euler_helper(self) -> int:
        v = 0
        while True:
            for i in self.matrix[v]:
                if i == 1:
                    return v
            v += 1
            if v == self.V:
                return -1

    def eulerian_cycle(self) -> bool:
        self.epath = []
        self.matrix_copy = deepcopy(self.matrix)
        v = self.euler_helper()
        self.__dfs_euler(v)
        if len(self.epath) == self.E+1 and self.epath[0] == self.epath[-1]:
            return True
        else:
            return False

    def euler_decision(self) -> bool:
        for i in range(self.V):
            c = 0
            for j in self.matrix[i]:
                if j == 1:
                    c += 1
            if c%2 != 0:
                return False
        return True


class AdjList:
    def __init__(self) -> None:
        self.V = 0
        self.E = 0
        self.out_nodes = {}
        self.is_visited = []

    def __repr__(self) -> str:
        repr = ''
        for i in range(self.V):
            repr += str(i)+' -> '+str(self.out_nodes[i])+'\n'
        repr += '\n'
        return repr

    def create_from_edge_list(self, edge_list: list, vertex_list: list) -> None:
        self.V = len(vertex_list)
        self.E = len(edge_list)

        for v in vertex_list:
            self.out_nodes.update({v: []})
            self.is_visited.append(False)

        for el in edge_list:
            u = el[0]
            v = el[1]
            self.out_nodes[u].append(v)

        for i in range(self.V):
            self.out_nodes[i].sort()

    def create_list_wrapper(self, edge_list: list):
        vertex_list = edge_list_to_vertex_list(edge_list)
        self.create_from_edge_list(edge_list, vertex_list)

    def create_random_dir_graph(self, n: int, D: float) -> None:
        self.V = n
        self.E = int(n*(n-1)*D)

        for v in range(self.V):
            self.out_nodes.update({v: []})
            self.is_visited.append(False)

        c = 0
        c_panic = 0
        random.seed()
        while c < self.E and c_panic < 10*self.E:
            c_panic += 1
            x = random.randint(0, self.V-1)
            y = random.randint(0, self.V-1)
            if y not in self.out_nodes[x] and y != x:
                self.out_nodes[x].append(y)
                c += 1
        
        for i in range(self.V):
            self.out_nodes[i].sort()

    def __hamiltonian(self, v: int) -> bool:
        self.is_visited[v] = True
        self.visited += 1
        for i in self.out_nodes[v]:
            if i == self.start and self.visited == self.V:
                return True
            if not self.is_visited[i]:
                db = self.__hamiltonian(i)
                if db:
                    self.hpath[self.k] = v
                    self.k += 1
                    return True
        self.is_visited[v] = False
        self.visited -= 1
        return False

    def hamiltonian_cycle(self) -> bool:
        self.hpath = [-1 for _ in range(self.V)]
        self.is_visited = [False for _ in range(self.V)]
        self.hpath[0] = 0
        self.start = 0
        self.visited = 0
        self.k = 1
        is_ham = self.__hamiltonian(self.start)
        return is_ham

    def __dfs_euler(self, v: int):
        for u in self.nodes_copy[v]:
            self.nodes_copy[v].remove(u)
            if v in self.nodes_copy[u]:
                self.nodes_copy[u].remove(v)
            self.__dfs_euler(u)
        self.epath.append(v)

    def eulerian_cycle(self) -> bool:
        self.epath = []
        self.nodes_copy = deepcopy(self.out_nodes)
        v = 0
        while len(self.out_nodes[v]) == 0:
            v += 1
        self.__dfs_euler(v)
        if len(self.epath) == self.E+1 and self.epath[0] == self.epath[-1]:
            return True
        else:
            return False

    def euler_decision(self) -> bool:
        self.out_degs = [len(i) for i in self.out_nodes]


def easy_test(test_list: list):
    adj_mat = UndirAdjMatrix()
    adj_list = AdjList()
    adj_mat.create_matrix_wrapper(test_list)
    adj_list.create_list_wrapper(test_list)
    print(adj_mat)
    print(adj_list)
    print(adj_mat.hamiltonian_cycle())
    print(adj_mat.eulerian_cycle())
    print(adj_list.hamiltonian_cycle())
    print(adj_list.eulerian_cycle())    


if __name__ == "__main__":

    test_list = [[0, 1], [1, 2], [2, 3], [3, 0]]
    test_list_nothing = [[0, 1], [1, 2], [2, 3]]
    test_list_there_should_be_eulers = [[4, 1], [1, 2], [2, 3], [3, 4]]
    rand_mat = UndirAdjMatrix()
    rand_mat.create_random_undir_graph(10, 0.5)
    print(rand_mat)
    rand_list = AdjList()
    rand_list.create_random_dir_graph(10, 0.5)
    print(rand_list)
    easy_test(test_list)
    easy_test(test_list_nothing)
    easy_test(test_list_there_should_be_eulers)