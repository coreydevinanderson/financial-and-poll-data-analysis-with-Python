import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
          election_file = csv.reader(csvfile)
          next(election_file)
          election_data = list(election_file)

vote_data = []

# Extract vote data from column three of each row
for ballot in range(len(election_data)):
    vote_data.append(election_data[ballot][2])


total_votes = len(vote_data)

# Determine unique candidates via set(); transform back to list object
candidates = list(set(vote_data))
candidates.sort() # Ensure list from set is in alphabetical order.


# Count number of votes for each candidate via nested for loop.
# For each candidate (i), iterate over each vote (j) to count the votes for that candidate.

vote_counts = []
count = 0

for i in candidates:
    for j in vote_data:
        if i == j:
            count +=1
    vote_counts.append(count)
    count = 0

# Convert counts to percentages
vote_percentages = []

for k in range(len(vote_counts)):
    vote_prop = float(vote_counts[k]) / total_votes
    vote_percentage = vote_prop * 100
    vote_percentage_formatted = "{0:.3f}".format(round(vote_percentage, 3))
    vote_percentages.append(vote_percentage_formatted)

# Determine the winner's index in candidate list
max_votes = max(vote_counts)
winner_index = vote_counts.index(max_votes)

# Print results to screen
print("Election Results\n")
print("-------------------------\n")
print("Total Votes: " + str(total_votes) + "\n")
print("-------------------------\n")
print("Khan: " + vote_percentages[1] + "% (" + str(vote_counts[1]) + ")\n")
print("Correy: " + vote_percentages[0] + "% (" + str(vote_counts[0]) + ")\n")
print("Li: " + vote_percentages[2] + "% (" + str(vote_counts[2]) + ")\n")
print("O'Tooley: " + vote_percentages[3] + "% (" + str(vote_counts[3]) + ")\n")
print("-------------------------\n")
print("Winner: " + str(candidates[winner_index]) + "\n")
print("-------------------------\n")

# Write to results to text file
txtout = os.path.join("analysis", "output.txt")

f = open(txtout, 'w')
print("Election Results\n", file = f)
print("-------------------------\n", file = f)
print("Total Votes: " + str(total_votes) + "\n", file = f)
print("-------------------------\n", file = f)
print("Khan: " + vote_percentages[1] + "% (" + str(vote_counts[1]) + ")\n", file = f)
print("Correy: " + vote_percentages[0] + "% (" + str(vote_counts[0]) + ")\n", file = f)
print("Li: " + vote_percentages[2] + "% (" + str(vote_counts[2]) + ")\n", file = f)
print("O'Tooley: " + vote_percentages[3] + "% (" + str(vote_counts[3]) + ")\n", file = f)
print("-------------------------\n", file = f)
print("Winner: " + str(candidates[winner_index]) + "\n", file = f)
print("-------------------------\n", file = f)
f.close()




        
          
