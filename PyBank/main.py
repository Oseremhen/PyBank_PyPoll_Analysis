#import the dependencies
import csv
import os

# Assign your variables
months = 0

net_profit = 0

change = []

maximum_change = 0 

minimum_change = 0

max_month_change = ""

min_month_change = ''

# assign a variable for the open path
budget_data = os.path.join("Resources/budget_data.csv")

with open(budget_data, 'r') as budget_csv:
    budget_info = list(csv.reader(budget_csv, delimiter= ","))

    for row in range(1,int(len(budget_info))):
        months = months + 1
        current_profit = int(budget_info[row][1])
        net_profit = net_profit + current_profit
        

        if len(change) > 0 or len(change) < 0:
            change.append(current_profit - int(budget_info[row - 1][1]))
        
        else:
            change.append(current_profit)
        
        if maximum_change < max(change):
            maximum_change = max(change)
            max_month_change = budget_info[row][0]

        if minimum_change > min(change):
            minimum_change = min(change)
            min_month_change = budget_info[row][0]

# calculating average change
average_change = round(sum(change)/months, 2)
print(f"{average_change}")
            
# assign a variable to save the file as txt
budget_analysis = os.path.join("Analysis/budget_analysis.txt")

with open(budget_analysis, 'w')as output_file:


    pybank_analysis = (f"`````` text\n"
                       f"Financial Analysis\n"
                       f"----------------------------\n"
                       f"Total Months: {months:,}\n"
                       f"Total: ${net_profit:,}\n"
                       f"Average Change: ${average_change:,}\n"
                       f"Greatest Increase in Profits: {max_month_change} (${maximum_change:,})\n"
                       f"Greatest Decrease in Profits: {min_month_change} (${minimum_change:,})\n"
                       f"````````````")

    print(format(pybank_analysis))
# write your analysis in the created txt file
    with open(budget_analysis, 'w')as output_file:
        output_file.write(pybank_analysis)


