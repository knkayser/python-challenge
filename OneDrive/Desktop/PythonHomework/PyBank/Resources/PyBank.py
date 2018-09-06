#imports
import os
import csv

#Create path to read CSV file
csvpath = os.path.join("budget_data.csv")

months = 0
tot_profit = 0
max_increase = 0
max_decrease = 0 
orig_profit = 0
profit_change = 0
difference = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

#Count total number of months included in the dataset
    for row in csvreader:
        months = months + 1
        
#Calculate total net amount of "Profits/Lossess" over the entire period
        tot_profit = tot_profit + int(row[1])

#Calculate the average change in "Profit/Losses" between months over the entire period
        difference =  int(orig_profit) - int(row[1])
        profit_change += difference
        orig_profit = row[1]

#Calculate the greatest increase in profits (date and amount) over the entire period
        if int(row[1]) > max_increase:
            max_increase = int(row[1]) 
            max_increase_mon = row[0] 

#Calculate the greatest decrease in losses (date and amount) over the netire period
        if int(row[1]) < max_decrease:
            max_decrease = int(row[1])
            max_decrease_mon = row[0]

average_change = profit_change / months

print("Financial Analysis")
print("--------------------")
print("Total Months : " + str(months))
print("Total : $" + str(tot_profit))
print("Average Change : $" + str(average_change))
print("Greatest Increase in Profits: " + str(max_increase_mon) + ", ($" + str(max_increase) + ")")
print("Greatest Decrease in Profits: " + str(max_decrease_mon) + ", $" + str(max_decrease) + ")")

