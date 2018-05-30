import os
import csv

# Set path for file
budgetCSV = os.path.join('budget_data_1.csv')

# Read in the csv file
with open(budgetCSV, newline = '') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)

    for row in csvreader:
        print(row)
