#Import csv and operating system

import os
import csv

#Locate CSV File
csvpath = os.path.join('..', 'pypoll', 'election_data.csv')
newfile = os.path.join('..', 'pypoll','election_final.txt')

#Track parameters
votes = []
candidates = []
total_votes = 0


#open and read csv file and convert to dictionaries
with open (csvpath, newline="") as election_data:
        csv_reader = csv.reader(election_data)
#Read first row
        title = next(csv_reader)
        first_row = next(csv_reader)



#Extract first row
        total_votes = total_votes + 1
        candidates = first_row[2]
        print(candidates)
#For loop to gather parameters
        for row in csv_reader:
        # count the total votes
                total_votes = total_votes + 1 
                print(total_votes)
#Calculate winner

#Generate Output

#Print Output