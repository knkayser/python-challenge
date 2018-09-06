#imports
import os
import csv

#Create path to read CSV file
csvpath = os.path.join("election_data.csv")

votes = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    cand_list = []
    khan_count = 0
    correy_count = 0
    li_count = 0
    otooley_count = 0

    for row in csvreader:

#Calculate total number of votes cast
        votes = votes + 1

# Create a complete list of candidates who received votes
        if row[2] not in cand_list:
            cand_list.append(row[2])

# Calculate the total number of votes each candidate won
        if row[2] == "Khan":
            khan_count = khan_count + 1
        elif row[2] == "Correy":
            correy_count = correy_count + 1
        elif row[2] == "Li":
            li_count = li_count + 1
        else:
            otooley_count = otooley_count + 1

# Calculate the percentage of votes each candidate won
khan_per = str(round((khan_count / votes) * 100, 4))
correy_per = str(round((correy_count / votes) * 100, 4))
li_per = str(round((li_count / votes) * 100, 4))
otooley_per = str(round((otooley_count / votes) * 100, 4))

# Determine the winner of the election based on popular vote
winner = max(khan_count, correy_count, li_count, otooley_count)

if winner == khan_count:
    winner_name = "Khan"
elif winner == correy_count:
    winner_name = "Correy"
elif winner == li_count:
    winner_name = "Li"
else:
    winner_name = "O'Tooley"



print("Election Results")
print("--------------------")
print("Total Votes: " + str(votes))
print("--------------------")
print("Khan : " + str(khan_per) + "% (" + str(khan_count) + ")")
print("Correy : " + str(correy_per) + "% (" + str(correy_count) + ")")
print("Li : " + str(li_per) + "% (" + str(li_count) + ")")
print("O'Tooley : " + str(otooley_per) + "% (" + str(otooley_count) + ")")
print("--------------------")
print("Winner: " + str(winner_name))

output_file = open("PyPoll_outputs.txt", "w")
output_file.write("Election Results")
output_file.write("--------------------")
output_file.write("Total Votes: " + str(votes))
output_file.write("--------------------")
output_file.write("Khan : " + str(khan_per) + "% (" + str(khan_count) + ")")
output_file.write("Correy : " + str(correy_per) + "% (" + str(correy_count) + ")")
output_file.write("Li : " + str(li_per) + "% (" + str(li_count) + ")")
output_file.write("O'Tooley : " + str(otooley_per) + "% (" + str(otooley_count) + ")")
output_file.write("--------------------")
output_file.write("Winner: " + str(winner_name))
