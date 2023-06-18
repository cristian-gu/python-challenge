## Test functions
import os
import csv

new_directory = 'C://Users//guerr//Desktop//Berkeley_Bootcamp_DataAnalysis//Module 3//Homework//Python-Challenge//python-challenge//PyBank'
os.chdir(new_directory)

current_directory = os.getcwd()
print('The current working directory is: ', current_directory)

bank_path = os.path.join('..','Pybank', 'Resources', 'budget_data.csv')

## Open file in read mode
with open(bank_path, 'r') as bank_file:
    csvreader = csv.reader(bank_file, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)

    # for row in csvreader:
    #    print(row)
    # test passes

    # print(f"CSV Header: {csv_header}")

    # for row in csvreader:
    #     value = row[1]
    #     print(type(value))

    ## find your changes
    # def avg_change(p_l_list):
    #     average_change_list = []
    #     for i in range(1, len(p_l_list)):
    #         val = p_l_list[i] - p_l_list[i-1]
    #         average_change_list.append(val)
    #     return

    # print(avg_change_list)
        
    # sam_list = [1, 3, 6, 9]
    # average_change_list = []
    # for i in range(len(sam_list)):
    #     if i == 0:
    #         pass
    #     else:
    #         val = sam_list[i] - sam_list[i-1]
    #         average_change_list.append(val)
    # print(average_change_list)

    # sam_list = [1, 3, 6, 9]
    # total = 0.0
    # length = range(len(sam_list))
    # for i in sam_list:
    #     total += sam_list[i]
    # print(total / length)

    # print(max(p_l_change))
    # print(min(p_l_change))