from pathlib import Path
import csv
fp = Path.cwd()/"csv_reports\\Profit-and-Loss.csv" 
# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list
    profit_and_loss=[] 

    # append net profit into the profit and loss list
    for row in reader:
        #get the net profit
        #and append to the profit and loss
        profit_and_loss.append([row[0], row[4]])  

def netprofit():
    highest_surplus = 0
    upward_trend = True
    downward_trend = True
    profit_deficit = [] #list to store deficits
    deficit_days = {} #dictionary to store and retrieve the day when a deficit occurs
    prev_net_profit = 0
    first_loop = True
    ## checks what trend the net profit follows, calculates surpluses and deficits
    for record in profit_and_loss:
        if first_loop == True:
            prev_net_profit = int(record[1])
            first_loop = False
        else:
            day = int(record[0])
            net_profit = int(record[1])
            difference = net_profit - prev_net_profit
            if difference > highest_surplus: #records highest surplus for scenario 1
                highest_surplus = difference
                highest_day = day
            if difference < 0:  #records deficits, disables scenario 1
                upward_trend = False 
                deficit_days[abs(difference)] = day
                profit_deficit.append(abs(difference))
            if difference > 0: #disables scenario 2 
                downward_trend = False
            prev_net_profit = net_profit