#import the necessary modules
import os
import csv

##To set the current directory to the correct directory, may need to change to Grader's preferences
# new_directory = 'C://Users//guerr//Desktop//Berkeley_Bootcamp_DataAnalysis//Module 3//Homework//Python-Challenge//python-challenge//PyBank'
# os.chdir(new_directory)

##check current_directory in terminal
# current_directory = os.getcwd()
# print('The current working directory is: ', current_directory)

#Create file pathway to import csv
bank_path = os.path.join('..','Pybank', 'Resources', 'budget_data.csv')

#Open file in read mode
with open(bank_path, 'r') as bank_file:
    csvreader = csv.reader(bank_file, delimiter=",")
    print(csvreader)
    # create header
    csv_header = next(csvreader)

    ## 1. Obtain num of months in the dataset
    
    #User defined function to count all months in dataset
    def total_num_months(csvreader):
        total = 0
        for row in csvreader:
            total += 1
        return total
    
    total_months = total_num_months(csvreader)
    print(total_months)

    ## 2. Net total of profit/losses
    
    # resets the csvfile to run csv file again
    bank_file.seek(0)
    next(csvreader)

    #user defined function that sum all P/L values
    def total_profits_loss(csvreader):
        total = 0
        for row in csvreader:
            total += int(row[1])
        return total
    total_p_l = total_profits_loss(csvreader)
    print(total_p_l)        

    ## 3. Average of changes in profit/losses
    #create profit and loss list to hold/manipulate values
    
    # resets the csvfile to run csv file again
    bank_file.seek(0)
    next(csvreader)

    #P/L value holder list
    p_l_list = [int(row[1]) for row in csvreader]
    print(p_l_list)
    
    #comprehension of finding average changes between P/L from value holder list and adding it to avg_change_list
    avg_change_list = [(p_l_list[i] - p_l_list[i-1]) for i in range(1, len(p_l_list))]
    
    #user defined function to average the changes in avg_change_list
    def avg_value(avg_change_list):
        total = sum(avg_change_list)
        length = len(avg_change_list)
        return total / length
        
    avg_change_p_l = avg_value(avg_change_list)
    print(avg_change_p_l)

    ## 4. Greatest increase in profits (Date, Amount)
    ## 5. Greatest decrease in profits (Date, Amount)

    #initialize the variables
    p_l_change = []
    up = 0
    down = 0
    
    #iterate to find max/min value indices. Conditionals created to find iterator index for max/min values
    for i in range(1, len(p_l_list)):
        diff = p_l_list[i] - p_l_list[i-1]
        p_l_change.append(diff)
        if diff > up:
            up = diff
            inc_finder = i
        elif diff < down:
            down = diff
            dec_finder = i
    
    # resets the csvfile to run csv file again
    bank_file.seek(0)
    next(csvreader)

    #Comprehensive list to extract all rows from csvreader
    bd_list = [row for row in csvreader]

    # obtained values of greatest p/l increase/decrease associated months
    print(bd_list[inc_finder][0])
    print(bd_list[dec_finder][0])
    
    ## 6. Export answers in text file
    #create path to store the txt file in
    store_path = os.path.join("..", "Pybank", "analysis", "analysis.txt")

    #In csv writer, list of outputs for each line wanted in the txt file created for iteration
    with open(store_path,"w") as file:
        outputs = ["Financial Analysis", "---------------------------------------------------------------------", f"Total Months: {str(total_months)}",
                   f"Total: {str(total_p_l)}", f"Greatest Increase in Profits: {(up)} ({str(bd_list[inc_finder][0])})", f"Greatest Decrease in Profits: {str(down)} ({str(bd_list[dec_finder][0])})"]
        for text in outputs:
            file.write(f"{text} \n")