# Dependencies
import csv
import os

# load files
pybank_csv = os.path.join("Resources", "budget_data.csv")

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0

#read csv 
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    
    # read header
csv_header = next(csvreader)

first_row = next(csvreader)
total_months += 1
total_net += int(first_row[1])
prev_net = int(first_row[1])

for row in csvreader:

total_months += 1
total_net += int(row[1])

net_change = int(row[1]) - prev_net
prev_net = int(row[1])
net_change_list += [net_change]
month_of_change += [row[0]]

#get the greatest increase
if net_change > greatest_increase[1]:
greatest_increase[0] = row[0]
greatest_increase[1] = net_change

#largest decrease
if net_change < greatest_decrease[1]:
greatest_decrease[0] = row[0]
greatest_decrease[1] = net_change

#get avg change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

output_analysis = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
    
print(output_analysis)

#export text file
budget_file = os.path.join("analysis", "budget_data.txt")
with open(budget_file, "w") as txt_file:
txt_file.write(output)






