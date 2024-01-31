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


def topoverhead(): #finds the highest overhead
    overhead_values = [] #list used to store values
    overhead_dict = {} #dictionary to store categories as values and overheads as keys
    for record in overhead_records: #adds values to both and keys to dict
        overhead_values.append(float(record[1]))
        overhead_dict[record[1]] = record[0]
    overhead_values.sort(reverse=True) #to find the highest overhead
    # use the dictionary to find the category
    return f"[HIGHEST OVERHEAD] {overhead_dict[str(overhead_values[0])].upper()}: {overhead_values[0]}%"

print(topoverhead())