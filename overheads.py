from pathlib import Path 
import csv
fp = Path.cwd()/"csv_reports\\Overheads.csv" #file path
# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list
    overhead_records=[] 

    # append net profit into the profit and loss list
    for row in reader:
        #get the net profit
        #and append to the profit and loss
        overhead_records.append([row[0], row[1]])  