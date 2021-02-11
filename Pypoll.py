#dependancies
import csv
import os

#files to load
file_to_load = "Resources/election_data.csv"
file_to_output = "analysis/election_analysis.txt"


#total votes
total_votes = 0

#candidates
candidate_options = []
candidate_votes = {}

#winning candidates
winning_candidate = ""
winning_count = 0

#read csv then convert to dict
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

for row in reader:

#add to votes   
    total_votes = total_votes + 1

#get candidate name
candidate_name = row["Candidate"]

#if candidate does not match existing candidate...
if candidate_name not in candidate_options:

#add it to list of candidates
    candidate_options.append(candidate_names)

#track voter count
candidate_votes[candidate_name]

#then add a vote to that candidate
candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(file_to_output, "w") as txt_file:

#print final vote
    election_results = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"---------------------------\n"
     )
print(election_results)

#save to text file
txt_file.write(election_results)

#find winner by looping through count
for candidate in candidate_votes:

#get vote count and percentage
    votes = candidate_votes.get(candidate)
vote_percentage = float(votes)/ float (total_votes) * 100

#find winning vote count and winning candidate
if (votes > winning_count):
    winning_count = votes
winning_candidate = candidate

#print candidate count and percentage
voter_output = f"{candidate}: {vote_percentage:.3f}%({votes})\n"
print(voter_output)

#save to text file
txt_file.write(voter_output)

#print the winning candidate
winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"---------------------------\n"
)

print(winning_candidate_summary)

#save winner to text file
txt_file_write(winning_candidate_summary)
