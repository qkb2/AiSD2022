import graphs
import sys

def small_test_eu():
    for i in range(100, 1000, 100): # slows down significantly after about 400 but even n=900 d=90% are possible
        for d in range(1, 10):
            for c in range(1): # change to 10 when actually testing for data
                mx = graphs.UndirAdjMatrix()
                lt = graphs.DirAdjList()
                mx.create_random_undir_graph(i, d/10)
                lt.create_random_dir_graph(i, d/10)
                mx.eulerian_cycle()
                lt.eulerian_cycle()
                print("at i: {}, d: {}, try: {}".format(i, d, c))

def small_test_ham():
    for i in range(10, 100, 10): # slows down significantly after about 30, maybe even halts
        for d in range(1, 10):
            for c in range(1): # change to 10 when actually testing for data
                mx = graphs.UndirAdjMatrix()
                lt = graphs.DirAdjList()
                print("at i: {}, d: {}, try: {} - start".format(i, d, c))
                mx.create_random_undir_graph(i, d/10)
                lt.create_random_dir_graph(i, d/10)
                mx.hamiltonian_cycle()
                lt.hamiltonian_cycle()
                print("at i: {}, d: {}, try: {} - end".format(i, d, c))

if __name__ == '__main__':
    sys.setrecursionlimit(10**8)
    small_test_ham()
