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
        self.vertices = []
    
    def create_from_edge_list(self, edge_list: list, vertex_list: list) -> None:
        self.V = len(vertex_list)
        self.E = len(edge_list)

        self.matrix = [[0 for _ in vertex_list] for _ in vertex_list]
        for el in edge_list:
            self.matrix[el[0]][el[1]] = 1
            self.matrix[el[1]][el[0]] = -1

        self.vertices = [Vertex(v) for v in vertex_list]

    def get_fl_io(self, u: int, fl: int, io: int):
        helper_list = self.matrix[u]
        for i in range(0, self.V, fl):
            if helper_list[i] == io:
                return i

    def update_all_in_degs(self) -> None:
        for v in self.vertices:
            for i in range(self.V):
                if self.matrix[i][v.name] == 1:
                    v.in_deg += 1

    def kahn_top_sort(self):
        sorted_v = []
        while True:
            u = None
            for v in self.vertices:
                if v.in_deg == 0:
                    u = v
                    break
            if u is None:
                return []
            sorted_v.append(u)
            for i in range(self.matrix[u.name]):
                if self.matrix[u.name][i] == 1:
                    self.vertices[i].in_deg -= 1
            self.vertices.remove(u)
            self.V -= 1
            if self.V == 0:
                return sorted_v
            
    def dfs_top_sort(self):
        sorted_v = []
        heap = []



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

            