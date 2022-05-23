#this version uses 0..n-1 matrices, which seem to be problematic for ST matrix.

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



class Vertex:
    def __init__(self, name: int) -> None:
        self.name = name
        self.in_deg = 0
        self.visit_color = 0 # 0 - white, 1 - grey, 2 - black



class AdjMatrix():
    def __init__(self) -> None:
        self.V = 0
        self.E = 0
        self.matrix = []
        self.vertices = [] # vertices start at 0

    def __repr__(self) -> str:
        repr = ''
        for i in range(self.V):
            for j in range(self.V):
                repr += str(self.matrix[i][j])+'\t'
            repr += '\n'
        return repr
    
    def create_from_edge_list(self, edge_list: list, vertex_list: list) -> None:
        self.V = len(vertex_list)
        self.E = len(edge_list)

        self.matrix = [[0 for _ in vertex_list] for _ in vertex_list]
        for el in edge_list:
            self.matrix[el[0]][el[1]] = 1
            self.matrix[el[1]][el[0]] = -1

        self.vertices = [Vertex(v) for v in vertex_list]

    def get_fl_io(self, u: int, fl: int, io: int) -> int:
        helper_list = self.matrix[u]
        for i in range(0, self.V, fl):
            if helper_list[i] == io:
                return i

    def update_all_in_degs(self) -> None:
        for v in self.vertices:
            v.in_deg = 0
            for i in range(self.V):
                if self.matrix[v.name][i] == -1:
                    v.in_deg += 1

    def kahn_top_sort(self) -> list:
        self.update_all_in_degs()
        # for i in self.vertices:
        #     print(i.in_deg)
        sorted_v = []
        helper_vertices = self.vertices.copy()
        # print("The array")
        n = self.V
        while True:
            # print("in loop")
            u = None
            for v in helper_vertices:
                if v.in_deg == 0:
                    u = v
                    # print("vertex chosen {}".format(u.name))
                    break
            if u is None:
                return []
            sorted_v.append(u.name)
            for i in range(self.V):
                if self.matrix[u.name][i] == 1:
                    self.vertices[i].in_deg -= 1
                    # print("vertex indeg -1: {}".format(i))
            helper_vertices.remove(u)
            n -= 1
            if n == 0:
                return sorted_v

    def small_dfs(self, u: Vertex, stack: list, flag: bool) -> bool:
        if flag:
            helper_list = self.matrix[u.name]
            u.visit_color = 1
            for i in range(self.V):
                if helper_list[i] == 1 and self.vertices[i].visit_color == 1:
                    flag = False
                    break
                if helper_list[i] == 1 and self.vertices[i].visit_color == 0:
                    flag = self.small_dfs(self.vertices[i], stack, flag)
            u.visit_color = 2
            stack.insert(0, u.name)
            return flag

    def dfs_top_sort(self) -> list:
        stack = []
        u = None
        for v in self.vertices:
            if v.in_deg == 0:
                u = v
                break
        if u is None:
            return []
        
        u.visit_color = 1
        while True:
            check = self.small_dfs(u, stack, True)
            if not check:
                return []
            flag = True
            for v in self.vertices:
                if v.visit_color != 2:
                    flag = False
                    break
            if flag:
                return stack
            
            for v in self.vertices:
                if v.visit_color == 0:
                    u = v

    def create_max_dag(self, n: int) -> None:
        self.V = n
        self.E = n*(n-1)//2
        self.vertices = [Vertex(v) for v in range(n)]
        for i in range(n):
            helper_list1 = [1 for _ in range(i)]
            helper_list1.append(0)
            helper_list1.extend([-1 for _ in range(n-i-1)])
            self.matrix.append(helper_list1)
        
    def randomize_max_dag(self) -> None:
        c = 0
        random.seed()
        while c < self.E//2:
            x = random.randint(0, self.V-1)
            y = random.randint(0, self.V-1)
            if self.matrix[x][y] != 0:
                self.matrix[x][y] = 0
                self.matrix[y][x] = 0
                c += 1

    def create_random_dag(self, n: int) -> None:
        self.create_max_dag(n)
        self.randomize_max_dag()

        

class AdjList:
    def __init__(self) -> None:
        self.V = 0
        self.E = 0
        self.in_dict = {}
        self.out_dict = {}
        self.non_dict = {}

    def create_from_edge_list(self, edge_list: list, vertex_list: list) -> None:
        self.V = len(vertex_list)
        self.E = len(edge_list)


        for v in vertex_list:
            self.in_dict.update({v: []})
            self.out_dict.update({v: []})
            self.non_dict.update({v: []})

        for el in edge_list:
            u = el[0]
            v = el[1]
            self.out_dict[u].append(v)
            self.in_dict[v].append(u)

        for i in range(self.V):
            self.in_dict[i].sort()
            self.out_dict[i].sort()
            self.non_dict[i].sort()

    def create_from_adj_matrix(self, adj_matrix: AdjMatrix):
        self.V = adj_matrix.V
        self.E = adj_matrix.E
        for v in range(self.V):
            self.in_dict.update({v: []})
            self.out_dict.update({v: []})
            self.non_dict.update({v: []})

        for u in range(self.V):
            for v in range(self.V):
                if adj_matrix.matrix[u][v] == 1:
                    self.out_dict[u].append(v)
                elif adj_matrix.matrix[u][v] == -1:
                    self.in_dict[u].append(v)
                else:
                    self.non_dict[u].append(v)

        for i in range(self.V):
            self.in_dict[i].sort()
            self.out_dict[i].sort()
            self.non_dict[i].sort()



class TheSaintMatrix(AdjMatrix):
    def build_the_saint_matrix(self, edge_list: list, vertex_list: list):
        self.V = len(vertex_list)
        self.E = len(edge_list)
        self.st_matrix = [[0 for _ in range(self.V+3)] for _ in range(self.V)]
        #do not use zero as a node name in this matrix
        for u in range(self.V):
            self.st_matrix[u][self.V+1] = self.get_fl_io(u, 1, 1) # fl: 1: first, -1: last
            last_out = self.get_fl_io(u, -1, 1) # io: 1: out, 0: non, 1: in
            self.st_matrix[u][self.V+2] = self.get_fl_io(u, 1, -1)
            last_in = self.get_fl_io(u, -1, -1)
            self.st_matrix[u][self.V+3] = self.get_fl_io(u, 1, 0)
            last_non = self.get_fl_io(u, -1, 0)
            for i in range(self.V):
                x = self.matrix[u][i]
                if x == 1:
                    self.st_matrix[u][i] = last_out
                elif x == -1:
                    self.st_matrix[u][i] = 2*last_in
                else:
                    self.st_matrix[u][i] = -last_non

    def tsm_update_all_in_degs(self) -> None:
        for v in self.vertices:
            v.in_deg = 0
            for i in range(self.V):
                if self.matrix[v.name][i] == -1:
                    v.in_deg += 1


    def tsm_kahn_top_sort(self) -> list:
        self.tsm_update_all_in_degs()
        # for i in self.vertices:
        #     print(i.in_deg)
        sorted_v = []
        helper_vertices = self.vertices.copy()
        # print("The array")
        n = self.V
        while True:
            # print("in loop")
            u = None
            for v in helper_vertices:
                if v.in_deg == 0:
                    u = v
                    # print("vertex chosen {}".format(u.name))
                    break
            if u is None:
                return []
            sorted_v.append(u.name)
            for i in range(self.V):
                if self.matrix[u.name][i] == 1:
                    self.vertices[i].in_deg -= 1
                    # print("vertex indeg -1: {}".format(i))
            helper_vertices.remove(u)
            n -= 1
            if n == 0:
                return sorted_v

    def tsm_small_dfs(self, u: Vertex, stack: list, flag: bool) -> bool:
        if flag:
            helper_list = self.matrix[u.name]
            u.visit_color = 1
            for i in range(self.V):
                if helper_list[i] == 1 and self.vertices[i].visit_color == 1:
                    flag = False
                    break
                if helper_list[i] == 1 and self.vertices[i].visit_color == 0:
                    flag = self.small_dfs(self.vertices[i], stack, flag)
            u.visit_color = 2
            stack.insert(0, u.name)
            return flag

    def tsm_dfs_top_sort(self) -> list:
        stack = []
        u = None
        for v in self.vertices:
            if v.in_deg == 0:
                u = v
                break
        if u is None:
            return []
        
        u.visit_color = 1
        while True:
            check = self.small_dfs(u, stack, True)
            if not check:
                return []
            flag = True
            for v in self.vertices:
                if v.visit_color != 2:
                    flag = False
                    break
            if flag:
                return stack
            
            for v in self.vertices:
                if v.visit_color == 0:
                    u = v



if __name__ == "__main__":

    adj_mat = AdjMatrix()
    adj_mat.create_from_edge_list([[1, 2], [1, 3], [3, 4], [3, 5], [0, 1]], [i for i in range(6)])
    st_mat = TheSaintMatrix()
    st_mat.create_from_edge_list([[1, 2], [1, 3], [3, 4], [3, 5], [0, 1]], [i for i in range(6)])
    print(adj_mat)
    print(st_mat)
    adj_mat.update_all_in_degs()
    # for v in adj_mat.vertices:
        # print(v.name, v.in_deg, v.visit_color)

    print(adj_mat.kahn_top_sort())
    print(adj_mat.dfs_top_sort())

    rand_mat = AdjMatrix()
    rand_mat.create_random_dag(100)
    print(rand_mat)
    print(rand_mat.kahn_top_sort())
    print(rand_mat.dfs_top_sort())