import matrices
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
    adj_kahn = []
    adj_dfs = []
    adj_kahn_sd = []
    adj_dfs_sd = []
    tsm_kahn = []
    tsm_dfs = []
    tsm_kahn_sd = []
    tsm_dfs_sd = []
    mtx = matrices.TheSaintMatrix()

    for i in range(100, 1100, 100):
        print("loop {}".format(i))
        rw_nm.append(i)

        adj_kahn_n = []
        adj_dfs_n = []
        tsm_kahn_n = []
        tsm_dfs_n = []


        for j in range(10):
            # adj matrix
            mtx.create_random_dag(i)
            print("dag {} created".format(j))
            adj_kahn_n.append(calc_time(mtx.kahn_top_sort))
            adj_dfs_n.append(calc_time(mtx.dfs_top_sort))

            # tsm matrix
            mtx.build_the_saint_matrix()
            print("matrix {} created".format(j))
            tsm_kahn_n.append(calc_time(mtx.tsm_kahn_top_sort))
            tsm_dfs_n.append(calc_time(mtx.tsm_dfs_top_sort))


        adj_kahn.append(st.mean(adj_kahn_n))
        adj_dfs.append(st.mean(adj_dfs_n))
        adj_kahn_sd.append(st.stdev(adj_kahn_n))
        adj_dfs_sd.append(st.stdev(adj_dfs_n))
        tsm_kahn.append(st.mean(tsm_kahn_n))
        tsm_dfs.append(st.mean(tsm_dfs_n))
        tsm_kahn_sd.append(st.stdev(tsm_kahn_n))
        tsm_dfs_sd.append(st.stdev(tsm_dfs_n))
        print("values for {} set".format(i))


    with open("data.csv", "w+") as mat_csv:
        csv_writ = csv.writer(mat_csv, delimiter=" ",
        quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        csv_writ.writerow(["n", "adj_kahn", "adj_kahn_ds", "adj_dfs", "adj_dfs_sd",
        "tsm_kahn", "tsm_kahn_sd", "tsm_dfs", "tsm_dfs_sd"])
        for i in range(10):
            csv_writ.writerow([rw_nm[i], adj_kahn[i], adj_kahn_sd[i], adj_dfs[i], adj_dfs_sd[i],
            tsm_kahn[i], tsm_kahn_sd[i], tsm_dfs[i], tsm_dfs_sd[i],])


if __name__ == "__main__":
    testing_suit()
