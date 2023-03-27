import os
import sys
import csv

election_data = os.path.join("C:/Users/Selin/Documents/Challenge 3 - Python/PyPoll/Resources/election_data.csv")

# creating a list for the names of the candidates
candidates = []

# creating a list for the number of votes
number_votes = []

# creating a list for the percentage of total votes
percentage_votes = []

# counter for total number fo votes
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # adding to the voter count
        total_votes += 1

        # adding new names to the list
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)
        else:
            index = candidates.index(row[2])
            number_votes[index] += 1
    
    # adding percentage of votes to the lsit
    for votes in number_votes:
        percentage = (votes/total_votes) * 100
        percentage = "%.3f%%" % percentage
        percentage_votes.append(percentage)

    # finding the candidate who won
    winner = max(number_votes)
    index = number_votes.index(winner)
    winning_candidate = candidates[index]


# printing results
print("Election Results")
print("_________________")
print(f"Total Votes: {str(total_votes)}")
print("_________________")
for i in range (len(candidates)):
    print(f"{candidates[i]}: {str(percentage_votes[i])}({str(number_votes[i])})")
print("_________________")
print(f"Winner: {winning_candidate}")
print("_________________")

# exporting to txt file
results = open("results.txt", "w")
line1 = "Election Results"
line2 = "_________________"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("_________________")
results.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percentage_votes[i])} (str{number_votes[i]})")
    results.write('{}\n'.format(line))
line5 = "_________________"
line6 = str(f"Winner: {winning_candidate}")
line7 = "_________________"
results.write('{}\n{}\n{}\n'.formaat(line5, line6, line7))
