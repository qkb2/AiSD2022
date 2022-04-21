import csv

with open("excel_std.csv", 'a') as dest:
    dest.write("sort_name data_type n comparison_std time_std\n")
    with open('data_for_excel.csv', 'r') as source:
        source_reader = csv.reader(source, delimiter=' ', quotechar='|')        
        for row in source_reader:
            dest.write("{} {} {} {} {}\n".format(row[0],row[1],row[2],row[6],row[8]))