import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    PL_file = csv.reader(csvfile)
    next(PL_file)
    PL_data = list(PL_file) 

PL_only = []
dates_only = []

# Create separate lists for profit/losses column and dates
for i in range(len(PL_data)):
    PL_only.append(int(PL_data[i][1]))
    dates_only.append(PL_data[i][0])

# Exclude first date for change in proft/losses
dates_only2 = dates_only[1:len(dates_only)]

# Total months is equal to total number of rows.
months = len(dates_only)

# Total profits/losses over all months.
PL_sum = sum(PL_only)

# Create empty list to append month change in profit/losses via for loop
PL_diff = []

for j in range(1, len(PL_only)):
    diff = PL_only[j] - PL_only[j - 1]
    PL_diff.append(diff)


# Calculate summary statistics
PL_change_average = "{0:.2f}".format(sum(PL_diff) / float((months - 1)))
PL_change_max = max(PL_diff)
PL_change_min = min(PL_diff)

PL_max_change_index = PL_diff.index(PL_change_max)
PL_min_change_index = PL_diff.index(PL_change_min)
max_change_month = dates_only2[PL_max_change_index]
min_change_month = dates_only2[PL_min_change_index]

# Print results to screen
print("Financial Analysis\n")
print("----------------------------\n")
print("Total Months: " + str(months)+ "\n")
print("Total: $" + str(PL_sum) + "\n")
print("Average Change: $" + PL_change_average + "\n")
print("Greatest Increase in Profits: " + str(max_change_month) + " ($" + str(PL_change_max) + ")\n")
print("Greatest Decrease in Profits: " + str(min_change_month) + " ($" + str(PL_change_min) + ")\n")


# Write results to text file
txtout = os.path.join("analysis", "output.txt")

f = open(txtout, 'w')
print("Financial Analysis\n", file = f)
print("----------------------------\n", file = f)
print("Total Months: " + str(months)+ "\n", file = f)
print("Total: $" + str(PL_sum) + "\n", file = f)
print("Average Change: $" + PL_change_average + "\n", file = f)
print("Greatest Increase in Profits: " + str(max_change_month) + " ($" + str(PL_change_max) + ")\n", file = f)
print("Greatest Decrease in Profits: " + str(min_change_month) + " ($" + str(PL_change_min) + ")\n", file = f)
f.close()



















    

          


