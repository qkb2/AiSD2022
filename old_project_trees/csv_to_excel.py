import csv
import statistics as st

class ExcelHandler:
    def __init__(self, tree_type: str, sample_num: int, num_arr: list) -> None:
        self.tree_type = tree_type
        self.sample_num = sample_num
        self.num_arr = num_arr
        self.avg_gen = []
        self.avg_search = []
        self.avg_trav = []
        self.avg_bal = []
        self.sd_gen = []
        self.sd_search = []
        self.sd_trav = []
        self.sd_bal = []

    def handler(self) -> None:
        is_avl = False
        if self.tree_type == 'avl':
            is_avl = True
        with open("data_is_avl_{}.csv".format(is_avl), "r") as source:
            source_reader = csv.reader(source, delimiter=' ', quotechar='|')
            gen_times = []
            search_times = []
            trav_times = []
            bal_times = []
            for row in source_reader:
                gen_times.append(float(row[1]))
                search_times.append(float(row[2]))
                trav_times.append(float(row[3]))
                bal_times.append(float(row[4]))

            def handler_helper(arr: list):
                avg_arr = []
                sd_arr = []
                helper_arr = []
                for i in range(len(arr)):
                    helper_arr.append(arr[i])
                    if (i+1)%self.sample_num == 0:
                        x = st.mean(helper_arr)
                        sd = st.stdev(helper_arr)
                        avg_arr.append(x)
                        sd_arr.append(sd)
                        helper_arr.clear()
                return avg_arr, sd_arr

            self.avg_gen, self.sd_gen = handler_helper(gen_times)
            self.avg_search, self.sd_search = handler_helper(search_times)
            self.avg_trav, self.sd_trav = handler_helper(trav_times)
            self.avg_bal, self.sd_bal = handler_helper(bal_times)
        source.close()

    def write_to_csv(self, data_type: str) -> None:
        with open("excel_data_{}_{}.csv".format(self.tree_type, data_type), "w+") as dest:
            dest.write("n generating_time search_time traversing_time balancing_time\n")
            dest_writer = csv.writer(
                dest, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            if data_type == "avg":
                for i in range(len(self.num_arr)):
                    dest_writer.writerow(
                        [str(self.num_arr[i]), str(self.avg_gen[i]), 
                        str(self.avg_search[i]), str(self.avg_trav[i]), 
                        str(self.avg_bal[i])])
            else:
                for i in range(len(self.num_arr)):
                    dest_writer.writerow(
                        [str(self.num_arr[i]), str(self.sd_gen[i]), 
                        str(self.sd_search[i]), str(self.sd_trav[i]), 
                        str(self.sd_bal[i])])                
                    

if __name__ == '__main__':
    arr  =[i for i in range(50, 550, 50)]
    avl_data = ExcelHandler('avl', 10, arr)
    bst_data = ExcelHandler('bst', 10, arr)
    avl_data.handler()
    bst_data.handler()
    avl_data.write_to_csv('avg')
    avl_data.write_to_csv('sd')
    bst_data.write_to_csv('avg')
    bst_data.write_to_csv('sd')

