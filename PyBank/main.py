import csv
import os

csv_path = os.path.join("Resources", "budget_data.csv")
txt_export = os.path.join("Analysis","budget_analysis.txt")

total_months = 0
change_month = []
earnings_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",999999999999]
earnings_total = 0

with open(csv_path) as info:
    reader = csv.reader(info)

    header = next(reader)

    first_row = next(reader)
    total_months += 1
    earnings_total += int(first_row[1])
    previous_total = int(first_row[1])

    for row in reader:
        total_months += 1
        earnings_total += int(row[1])

        #Track net change
        earnings_change = int(row[1]) - previous_total
        previous_total = int(row[1])
        earnings_change_list += [earnings_change]
        change_month += row[0]

        #calculate greatest increase
        if earnings_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = earnings_change

        #calculate greatest decrease
        if earnings_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = earnings_change

#Calculate the Average Net Change
monthly_avg = sum(earnings_change_list) / len(earnings_change_list)

#Generate Output Summary
output = (
    f"Financial Analysis\n"
    f"-----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${earnings_total}\n"
    f"Average Change: ${monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)
