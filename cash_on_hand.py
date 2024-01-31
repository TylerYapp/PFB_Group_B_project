from pathlib import Path 
import csv
fp = Path.cwd()/"csv_reports\\Cash-on-Hand.csv" 
# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list
    cash_records=[] 

    # append net profit into the profit and loss list
    for row in reader:
        #get the net profit
        #and append to the profit and loss
        cash_records.append([row[0], row[1]])  

def cashonhand():
    highest_surplus = 0
    upward_trend = True
    downward_trend = True
    cash_deficit = [] #list to store deficits
    deficit_days = {} #dictionary to store and retrieve the day when a deficit occurs
    prev_cash_on_hand = 0
    first_loop = True
    ## checks what trend the net profit follows, calculates surpluses and deficits
    for record in cash_records:
        if first_loop == True:
            prev_cash_on_hand = int(record[1])
            first_loop = False
        else:
            day = int(record[0])
            cash_on_hand = int(record[1])
            difference = cash_on_hand - prev_cash_on_hand
            if difference > highest_surplus: #records highest surplus for scenario 1
                highest_surplus = difference
                highest_day = day
            if difference < 0:  #records deficits, disables scenario 1
                upward_trend = False 
                deficit_days[abs(difference)] = day
                cash_deficit.append(abs(difference))
            if difference > 0:
                downward_trend = False #disables scenario 2 
            prev_cash_on_hand = cash_on_hand