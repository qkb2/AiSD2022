from sys import setrecursionlimit
import unittest
import graphs_depr

setrecursionlimit(10**8)

class TestEulerianCycles(unittest.TestCase):

    def test_undir_graph_dense(self, n: int=100):
        for i in range(1, 10):
            with self.subTest(i=i):
                gr = graphs_depr.UndirAdjMatrix()
                gr.create_random_undir_graph(n, i/10)
                self.assertEqual(gr.eulerian_cycle(), gr.euler_decision())

    def test_undir_graph_nodes(self, d: float=0.5):
        for i in range(10, 200, 10):
            with self.subTest(i=i):
                gr = graphs_depr.UndirAdjMatrix()
                gr.create_random_undir_graph(i, d)
                self.assertEqual(gr.eulerian_cycle(), gr.euler_decision())

    def test_dir_graph_dense(self, n: int=100):
        for i in range(1, 10):
            with self.subTest(i=i):
                gr = graphs_depr.DirAdjList()
                gr.create_random_dir_graph(n, i/10)
                self.assertEqual(gr.eulerian_cycle(), gr.euler_decision())

    def test_dir_graph_nodes(self, d: float=0.5):
        for i in range(10, 200, 10):
            with self.subTest(i=i):
                gr = graphs_depr.DirAdjList()
                gr.create_random_dir_graph(i, d)
                self.assertEqual(gr.eulerian_cycle(), gr.euler_decision())

    def test_case_undir(self, n: int=10):
        for i in range(n):
            print("New test case undir no {}".format(i))
            self.test_undir_graph_dense()
            self.test_undir_graph_nodes()

    def test_case_dir(self, n: int=10):
        for i in range(n):
            print("New test case dir no {}".format(i))
            self.test_dir_graph_dense()
            self.test_dir_graph_nodes()

if __name__ == '__main__':
    unittest.main()