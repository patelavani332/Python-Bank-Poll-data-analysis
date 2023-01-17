#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv

vote_csv = os.path.join(".","Resources","election_data.csv")    # Data file location

candidates = []   

candidate_votes = {}

winner_name = ''

winning_votes = 0

with open(vote_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")        # Read the CSV file
    
    total_votes =0
    header = next(csvreader)                             # skip the header 
        
    for row in csvreader:
        total_votes += 1                                 # count total rows(votes)
        
        candidate_name = row[2]                          # store candidate_name with names from data file
        
# Find unique candidates from the candidate_name list
        if candidate_name not in candidates:      
            candidates.append(candidate_name)         

            candidate_votes[candidate_name] = 0
# calculate total votes for each candidate            
        candidate_votes[candidate_name] += 1

# store output in variable
poll_analysis = (f"Election Results\n"
                 f"-------------------------------\n"
                 f"Total Votes : {total_votes}\n"
                 f"-------------------------------\n"
                )

print(poll_analysis)          # print the output

# Output file location
analysis_output = os.path.join(".","Analysis","election_analysis.txt")

with open (analysis_output,"w") as textfile:
    textfile.write(poll_analysis)        # write the output

# i is candidate   
    for i in candidate_votes:
        votes = candidate_votes[i]
        percent_votes = float(votes)/float(total_votes) *100  # calculate percent votes obtained by each candidate

# find the winner         
        if (votes > winning_votes):
            winning_votes = votes
            winner_name = i
        voting_details = f"{i}. {percent_votes: .3f}% ({votes})\n"
    
        print(voting_details)
            
        textfile.write(voting_details)       # update the output in output file
        
    winner_analysis = (
         f"-------------------------------\n"
         f"Winner : {winner_name}\n"
         f"-------------------------------\n"
    )
    print(winner_analysis)
    
    textfile.write(winner_analysis)      # update the output in output file


# In[ ]:




