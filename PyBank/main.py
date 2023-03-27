import os
import csv
import sys

# set directory
os.chdir(os.path.dirname(__file__))

# set resources path
budget_data = os.path.join("C:/Users/Selin/Documents/Challenge 3 - Python/PyBank/Resources/budget_data.csv")

total_months = 0
total_profit_loss = 0
value = 0
change = 0
dates = []
profits = []

# open the CSV
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # get header
    csv_header = next(csvreader)
    
    # getting the first row
    first_row = next(csvreader)
    total_months += 1
    total_profit_loss += int(first_row[1])
    value = int(first_row[1])

    # going through each subsequent row
    for row in csvreader:
        #tracking dates
        dates.append(row[0])

        # finding the changes and adding it to the list
        change = int(row[1]) -value
        profits.append(change)
        value = int(row[1])

        # total months
        total_months += 1

        # total amount of profits and losses over the period
        total_profit_loss = total_profit_loss + int(row[1])

    # greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    # greatest decrease in profits
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    # average change between months for profits and losses
    average_change = sum(profits)/len(profits)

# printing the information
print("Financial Analysis: ")
print("_________________________________")
print(f"Total Months: {str(total_months)}")
print(f"Total:  ${str(total_profit_loss)}")
print(f"Average Change: ${str(round(average_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Prfits: {worst_date} (${str(greatest_decrease)})")

# exporting to txt file
results = open("result.txt", "w")

line1 = "Financial Analysis"
line2 = "__________________"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total:  ${str(total_profit_loss)}")
line5 = str(f"Average Change: ${str(round(average_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Prfits: {worst_date} (${str(greatest_decrease)})")
results.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7))
