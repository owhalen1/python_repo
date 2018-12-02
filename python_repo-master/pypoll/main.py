#Import csv and operating system

import os
import csv
import operator
#Locate CSV File
csvpath = os.path.join('..', 'pypoll', 'election_data.csv')
newfile = os.path.join('..', 'pypoll','election_final.txt')

#Track parameters
votes = []
candidate_list = []
candidate_votes_list = []

row_count = 0

#open and read csv file and convert to dictionaries
with open (csvpath, newline="") as election_data:
        csv_reader = csv.reader(election_data)
        # Read and extract first row
        next(csv_reader)
        first_row = next(csv_reader)

        #store first candidate name
        last_candidate = first_row[2]


        #sort by candidate
        #sort = sorted(csv_reader, key=operator.itemgetter(2))
        for row in csv_reader:

             #total the votes
             row_count = sum(1 for line in csv_reader)
             total_votes = row_count

             #store candidate
             candidate = row[2]

             if candidate not in candidate_list:
                 candidate_list.append(candidate)
                 candidate_votes = candidate.count(candidate)
                 candidate_votes_list.append(candidate_votes)
                 print(candidate_list)





#Gather output
output = (
      f"\nElection Results\n"
      f"-------------------\n"
      f"Total Votes : {total_votes}\n"
      f"---------------------------\n"
      f"{candidate_list[0]}:{candidate_votes_list[0]}\n"
      f"{candidate_list[1]}:{candidate_votes_list[1]}\n"
      f"{candidate_list[2]}:{candidate_votes_list[2]}\n"
      f"{candidate_list[3]}:{candidate_votes_list[3]}\n")

#Print output to terminal
print(output)

#print output to new file
with open(newfile, "w") as txt_file:
    txt_file.write(output)


