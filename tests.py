import matrices
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
    tsm_kahn = []
    tsm_dfs = []

    for i in range(100, 600, 50):
        rw_nm.append(i)

        # adj matrix
        mtx = matrices.TheSaintMatrix()
        mtx.create_random_dag(i)
        adj_kahn.append(calc_time(mtx.kahn_top_sort))
        adj_dfs.append(calc_time(mtx.dfs_top_sort))

        # saint matrix
        mtx.build_the_saint_matrix()
        tsm_kahn.append(calc_time(mtx.tsm_kahn_top_sort))
        tsm_dfs.append(calc_time(mtx.tsm_dfs_top_sort))

    with open("data.csv", "w") as mat_csv:
        csv_writ = csv.writer(mat_csv, delimiter=" ", quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writ.writerow(["n", "adj_kahn", "adj_dfs", "tsm_kahn", "tsm_dfs"])
        for i in range(10):
            csv_writ.writerow([rw_nm[i], adj_kahn[i], adj_dfs[i], tsm_kahn[i], tsm_dfs[i]])


if __name__ == "__main__":
    testing_suit()
