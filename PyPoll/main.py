import os
import csv

resource_file = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("Resources", "output.txt")

total_votes = 0 # The total number of votes cast
candidates_votes = {} # A complete list of candidates who received votes
candidates = []


with open(resource_file) as election_data:
    data = csv.reader(election_data)

    # Header
    header = next(data)

    for row in data:

        total_votes = total_votes + 1

        candidate_name = row[2]

        if candidate_name not in candidates_votes:
            candidates.append(candidate_name)
            candidates_votes[candidate_name] = 0
        
        elif candidate_name in candidates_votes:
            candidates_votes[candidate_name] = candidates_votes[candidate_name] +1


# print(candidates_votes)

# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

    percentages = []
    winning_count = 0
    winning_pct = 0
    winner = ""

    for candidate in candidates_votes:
        votes = candidates_votes[candidate]
        votes_pct = (votes / total_votes)*100
        percentages.append(votes_pct)
        if votes > winning_count:
            winning_count = votes
            winning_pct = votes_pct
            winner = candidate


# print(candidates_votes)
# print(percentages)


output = (
f"\nElection Results\n"
f"----------------------------\n"
f"Total Votes: {total_votes}\n"
f"----------------------------\n"
f"Winner: {winner} with {winning_count} votes ({winning_pct: .2f}%)\n"
f"Candidates' Results: \n"
f"{candidates_votes}\n")
    
# Export the results to text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)

# output_file = open("output.txt", "w") 
# output_file.write(output)  
# output_file.close()
