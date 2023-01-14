#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os
import csv

budget_csv = os.path.join(".", "Resources","budget_data.csv")

profit_loss = []
change = []
month = []
greatest_increase = 0
greatest_decrease = 0
best_month = ''
worst_month = ''

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(csvreader)
          
    total_months = 0
        
    for row in csvreader:
        total_months += 1                        # to count total months
        profit_loss.append(int(row[1]))      # to create a list of all profit/loss
        month.append(row[0])                 # to create a lsit of all months
           
    total = sum (profit_loss)                # to calculate total profit/loss 
        
    change = [profit_loss[i+1] - profit_loss[i] for i in range(0,len(profit_loss)-1)]      # to calculate the change in profit/loss over entire period
    total_change = sum(change)                     # calculate total change
    
    average = round(total_change/len(change),2)     # calculate average of total change
       
    maximum = max(change)                         # to find the greatest increase in the profits
    
    minimum = min(change)                         # to find the greatest decrease in the profits
              
    max_index = change.index(maximum)             # to find the index number of the greatest increase in profit
    max_month = month[max_index+1]                # to map the month with the greatest increase in profit
        
    min_index = change.index(minimum)             # to find the index number of the greatest increase in profit
    min_month = month[min_index+1]                # to map the month with the greatest decrease in profit  
    
analysisOutput = (f"Financial Analysis\n"
                  f"----------------------------\n"
                  f"Total months : {total_months}\n"
                  f"Total : ${total}\n"
                  f"Average change : ${average}\n"
                  f"Greatest Increase in Profits: {max_month} (${maximum})\n"
                  f"Greatest Decrease in Profits: {min_month} (${minimum})\n"
)

#--- print analysis output to terminal ---
print(analysisOutput)

financial_analysis = os.path.join(".","analysis","financial_analysis.txt")

#- -- create a text file with the analysis output ---
with open(financial_analysis, 'w') as textfile:
    textfile.write(analysisOutput)


# In[ ]:




