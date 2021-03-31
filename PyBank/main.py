import csv

with open('budget_data.csv', 'r') as csvfile:
    PL_file = csv.reader(csvfile)
    next(PL_file)
    PL_data = list(PL_file) 

PL_only = []
dates_only = []

for i in range(len(PL_data)):
    PL_only.append(int(PL_data[i][1]))
    dates_only.append(PL_data[i][0])

dates_only2 = dates_only[1:len(dates_only)]
n = len(PL_only)
PL_sum = sum(PL_only)
PL_diff = []

for j in range(1, len(PL_only)):
    diff = PL_only[j] - PL_only[j - 1]
    PL_diff.append(diff)

PL_change_average = round(sum(PL_diff) / (n - 1), 2)
PL_change_max = max(PL_diff)
PL_change_min = min(PL_diff)

PL_max_change_index = PL_diff.index(PL_change_max)
PL_min_change_index = PL_diff.index(PL_change_min)
max_change_month = dates_only2[PL_max_change_index]
min_change_month = dates_only2[PL_min_change_index]


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {n}")
print(f"Total: ${PL_sum}")
print(f"Average Change: ${PL_change_average}")
print(f"Greatest Increase in Profits: {max_change_month} (${PL_change_max})")
print(f"Greatest Decrease in Profits: {min_change_month} (${PL_change_min})")


    

          

