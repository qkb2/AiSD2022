import graphs
import statistics as st
import time
import csv


def calc_time(func):
    start_time = time.perf_counter()
    func()
    stop_time = time.perf_counter()
    return stop_time - start_time

def testing_suit():
    rw_nm = []
    rw_sm = []

    dir_50s_ham = []
    dir_50s_ham_sd = []
    dir_50s_eul = []
    dir_50s_eul_sd = []

    ndir_50s_ham = []
    ndir_50s_ham_sd = []
    ndir_50s_eul = []
    ndir_50s_eul_sd = []

    dir_12n_ham = []
    dir_12n_ham_sd = []
    dir_12n_eul = []
    dir_12n_eul_sd = []

    ndir_12n_ham = []
    ndir_12n_ham_sd = []
    ndir_12n_eul = []
    ndir_12n_eul_sd = []

    dir_3d_ham = [[] for i in range(10)]
    dir_3d_eul = [[] for i in range(10)]
    ndir_3d_ham = [[] for i in range(10)]
    ndir_3d_eul = [[] for i in range(10)]

    d_graph = graphs.DirAdjList()
    ud_graph = graphs.UndirAdjMatrix()

    # constant s (50%)
    for i in range(10, 20):
        print("loop {}".format(i))
        rw_nm.append(i)

        dir_50s_ham_n = []
        dir_50s_eul_n = []
        ndir_50s_ham_n = []
        ndir_50s_eul_n = []

        for j in range(10):
            # dir graph
            d_graph.create_random_dir_graph(i, 0.5)
            dir_50s_eul_n.append(calc_time(d_graph.eulerian_cycle))
            dir_50s_ham_n.append(calc_time(d_graph.hamiltonian_cycle))

            # undir graph
            ud_graph.create_random_undir_graph(i, 0.5)
            ndir_50s_eul_n.append(calc_time(ud_graph.eulerian_cycle))
            ndir_50s_ham_n.append(calc_time(ud_graph.hamiltonian_cycle))

        dir_50s_eul.append(st.mean(dir_50s_eul_n))
        dir_50s_eul_sd.append(st.stdev(dir_50s_eul_n))
        dir_50s_ham.append(st.mean(dir_50s_ham_n))
        dir_50s_ham_sd.append(st.stdev(dir_50s_ham_n))

        ndir_50s_eul.append(st.mean(ndir_50s_eul_n))
        ndir_50s_eul_sd.append(st.stdev(ndir_50s_eul_n))
        ndir_50s_ham.append(st.mean(ndir_50s_ham_n))
        ndir_50s_ham_sd.append(st.stdev(ndir_50s_ham_n))

    with open("data_1.csv", "w+") as d1_csv:
        csv_writ = csv.writer(d1_csv, delimiter=" ",
        quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        csv_writ.writerow(["n", "dir_50s_ham", "dir_50s_ham_sd", "dir_50s_eul", "dir_50s_eul_sd",
                           "ndir_50s_ham", "ndir_50s_ham_sd", "ndir_50s_eul", "ndir_50s_eul_sd"])
        for i in range(len(rw_nm)):
            csv_writ.writerow([rw_nm[i],dir_50s_ham[i], dir_50s_ham_sd[i], dir_50s_eul[i], dir_50s_eul_sd[i],
                                ndir_50s_ham[i], ndir_50s_ham_sd[i], ndir_50s_eul[i], ndir_50s_eul_sd[i]])

    # constant n (12)
    i = 0.1
    while i < 1:
        print("loop {}".format(i))
        rw_sm.append(i)

        dir_12n_ham_n = []
        dir_12n_eul_n = []
        ndir_12n_ham_n = []
        ndir_12n_eul_n = []

        for j in range(10):
            # dir graph
            d_graph.create_random_dir_graph(12, i)
            dir_12n_eul_n.append(calc_time(d_graph.eulerian_cycle))
            dir_12n_ham_n.append(calc_time(d_graph.hamiltonian_cycle))

            # undir graph
            ud_graph.create_random_undir_graph(12, i)
            ndir_12n_eul_n.append(calc_time(ud_graph.eulerian_cycle))
            ndir_12n_ham_n.append(calc_time(ud_graph.hamiltonian_cycle))

        dir_12n_eul.append(st.mean(dir_12n_eul_n))
        dir_12n_eul_sd.append(st.stdev(dir_12n_eul_n))
        dir_12n_ham.append(st.mean(dir_12n_ham_n))
        dir_12n_ham_sd.append(st.stdev(dir_12n_ham_n))

        ndir_12n_eul.append(st.mean(ndir_12n_eul_n))
        ndir_12n_eul_sd.append(st.stdev(ndir_12n_eul_n))
        ndir_12n_ham.append(st.mean(ndir_12n_ham_n))
        ndir_12n_ham_sd.append(st.stdev(ndir_12n_ham_n))

        i += 0.1
        i = round(i, 1)

    with open("data_2.csv", "w+") as d2_csv:
        csv_writ = csv.writer(d2_csv, delimiter=" ",
        quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        csv_writ.writerow(["s", "dir_12n_ham", "dir_12n_ham_sd", "dir_12n_eul", "dir_12n_eul_sd",
                           "ndir_12n_ham", "ndir_12n_ham_sd", "ndir_12n_eul", "ndir_12n_eul_sd"])
        for i in range(len(rw_sm)):
            csv_writ.writerow([rw_sm[i],dir_12n_ham[i], dir_12n_ham_sd[i], dir_12n_eul[i], dir_12n_eul_sd[i],
                                ndir_12n_ham[i], ndir_12n_ham_sd[i], ndir_12n_eul[i], ndir_12n_eul_sd[i]])

    # 3d chart
    k = 0
    for i in range(10, 20):
        j = 0.1
        while j < 1:
            print("loop {} {}".format(i, j))

            dir_3d_ham_n = []
            dir_3d_eul_n = []
            ndir_3d_ham_n = []
            ndir_3d_eul_n = []

            for o in range(10):
                # dir graph
                d_graph.create_random_dir_graph(i, j)
                dir_3d_eul_n.append(calc_time(d_graph.eulerian_cycle))
                dir_3d_ham_n.append(calc_time(d_graph.hamiltonian_cycle))

                # undir graph
                ud_graph.create_random_undir_graph(i, j)
                ndir_3d_eul_n.append(calc_time(ud_graph.eulerian_cycle))
                ndir_3d_ham_n.append(calc_time(ud_graph.hamiltonian_cycle))

            dir_3d_eul[k].append(st.mean(dir_3d_eul_n))
            dir_3d_ham[k].append(st.mean(dir_3d_ham_n))
            ndir_3d_eul[k].append(st.mean(ndir_3d_eul_n))
            ndir_3d_ham[k].append(st.mean(ndir_3d_ham_n))

            j += 0.1
            j = round(j, 1)

        k += 1

    with open("data_3d_dir_ham.csv", "w+") as d3_csv:
        csv_writ = csv.writer(d3_csv, delimiter=" ",
        quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        csv_writ.writerow(["s\\n"] + [n for n in rw_nm])
        for i in range(len(rw_sm)):
            csv_writ.writerow([rw_sm[i]] + [n for n in dir_3d_ham[i]])

    with open("data_3d_dir_eul.csv", "w+") as d3_csv:
        csv_writ = csv.writer(d3_csv, delimiter=" ",
        quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        csv_writ.writerow(["s\\n"] + [n for n in rw_nm])
        for i in range(len(rw_sm)):
            csv_writ.writerow([rw_sm[i]] + [n for n in dir_3d_eul[i]])

    with open("data_3d_ndir_ham.csv", "w+") as d3_csv:
        csv_writ = csv.writer(d3_csv, delimiter=" ",
        quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        csv_writ.writerow(["s\\n"] + [n for n in rw_nm])
        for i in range(len(rw_sm)):
            csv_writ.writerow([rw_sm[i]] + [n for n in ndir_3d_ham[i]])

    with open("data_3d_ndir_eul.csv", "w+") as d3_csv:
        csv_writ = csv.writer(d3_csv, delimiter=" ",
        quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        csv_writ.writerow(["s\\n"] + [n for n in rw_nm])
        for i in range(len(rw_sm)):
            csv_writ.writerow([rw_sm[i]] + [n for n in ndir_3d_eul[i]])


if __name__ == "__main__":
    testing_suit()
