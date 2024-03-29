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

 #checks what code to run based on trend type
    final_output = ""
    if upward_trend == True: #Scenario 1, returns highest surplus
        return f"""[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY
[HIGHEST CASH SURPLUS] DAY: {highest_day}, AMOUNT: SGD{highest_surplus}\n"""
    
    elif downward_trend == True: #Scenario 2, returns highest deficit
        cash_deficit.sort(reverse = True) #sorts in descending order to get highest deficit
        return f"""[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY
[HIGHEST CASH DEFICIT] DAY: {deficit_days[cash_deficit[0]]}, AMOUNT: SGD{cash_deficit[0]}\n"""
    
    else: #Scenario 3, returns all deficits and 3 highest deficits
        for deficit in cash_deficit:
            output = f"[CASH DEFICIT] DAY: {deficit_days[deficit]}, AMOUNT: SGD{deficit}"
            final_output += output + '\n'
            #shows 3 highest deficits, if else is to check for missing values and return nil
        cash_deficit.sort(reverse = True) #sorts in descending order to find highest deficits
        final_output += f"[HIGHEST CASH DEFICIT] DAY: {deficit_days[cash_deficit[0]]}, AMOUNT: SGD{cash_deficit[0]}\n"
        final_output += f"[2ND HIGHEST CASH DEFICIT] DAY: {deficit_days[cash_deficit[1]]}, AMOUNT: SGD{cash_deficit[1]}\n"
        final_output += f"[3RD HIGHEST CASH DEFICIT] DAY: {deficit_days[cash_deficit[2]]}, AMOUNT: SGD{cash_deficit[2]}\n"
        return final_output
    
