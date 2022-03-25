import csv



def graph_sort_with_data_types_swaps_of_n(sort_name, dest):
    dest.write(sort_name+"\n")
    dest.write("numbers_of_elements ")
    [dest.write(str(k)+" ") for k in range(250, 3250, 250)]
    dest.write("\n")
    for generator in ["random_generator", "increasing_generator", "decreasing_generator", "a_shaped_generator", "v_shaped_generator"]:
        dest.write(generator+" ")
        with open('data_for_excel.csv', 'r') as source:
            source_reader = csv.reader(source, delimiter=' ', quotechar='|')        
            for row in source_reader:
                if row[0] == sort_name and row[1] == generator:
                    s = str(float(row[3])+float(row[4]))
                    dest.write(s+" ")
            dest.write("\n")


def graph_sort_with_data_types_time_of_n(sort_name, dest):
    dest.write(sort_name+"\n")
    dest.write("numbers_of_elements ")
    [dest.write(str(k)+" ") for k in range(250, 3250, 250)]
    dest.write("\n")
    for generator in ["random_generator", "increasing_generator", "decreasing_generator", "a_shaped_generator", "v_shaped_generator"]:
        dest.write(generator+" ")
        with open('data_for_excel.csv', 'r') as source:
            source_reader = csv.reader(source, delimiter=' ', quotechar='|')        
            for row in source_reader:
                if row[0] == sort_name and row[1] == generator:
                    dest.write(row[5]+" ")
            dest.write("\n")


def graph_data_type_with_sorts_time_of_n(data_name):
    pass











with open('excel_sheets.csv', 'a') as dest:
    dest_writer = csv.writer(dest, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for sort_name in ["insertion_sort_wrapper", "shell_sort_wrapper", "quick_sort_wrapper", "merge_sort_wrapper", "heap_sort_wrapper"]:
        graph_sort_with_data_types_swaps_of_n(sort_name, dest)
        dest.write("\n")
        graph_sort_with_data_types_time_of_n(sort_name, dest)
        dest.write("\n")