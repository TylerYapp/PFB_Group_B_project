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
            
    # checks what code to run based on trend type
    final_output = ""
    if upward_trend == True: #Scenario 1, returns highest surplus
        return f"""[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY
[HIGHEST NET PROFIT SURPLUS] DAY: {highest_day}, AMOUNT: SGD{highest_surplus}\n"""
    elif downward_trend == True: #Scenario 2, returns highest deficit
        profit_deficit.sort(reverse = True) #sorts in descending order to get highest deficit
        return f"""[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN THE PREVIOUS DAY
[HIGHEST NET PROFIT DEFICIT] DAY: {deficit_days[profit_deficit[0]]}, AMOUNT: SGD{profit_deficit[0]}\n"""
    else: #Scenario 3, returns all deficits and 3 highest deficits
        for deficit in profit_deficit: #lists all deficits
            output = f"[NET PROFIT DEFICIT] DAY: {deficit_days[deficit]}, AMOUNT: SGD{deficit}"
            final_output += output + '\n'
             #shows 3 highest deficits, if else is to check for missing values and return nil
        profit_deficit.sort(reverse = True) #sorts in descending order to find highest deficits
        final_output += f"[HIGHEST PROFIT DEFICIT] DAY: {deficit_days[profit_deficit[0]]}, AMOUNT: SGD{profit_deficit[0]}\n"
        if len(profit_deficit) > 1:
            final_output += f"[2ND HIGHEST PROFIT DEFICIT] DAY: {deficit_days[profit_deficit[1]]}, AMOUNT: SGD{profit_deficit[1]}\n"
        else:
            final_output += "[2ND HIGHEST PROFIT DEFICIT] DAY: nil, AMOUNT: nil\n"
        if len(profit_deficit) > 2:
            final_output += f"[3RD HIGHEST PROFIT DEFICIT] DAY: {deficit_days[profit_deficit[2]]}, AMOUNT: SGD{profit_deficit[2]}\n"
        else:
            final_output += "[3RD HIGHEST PROFIT DEFICIT] DAY: nil, AMOUNT: nil\n"
        return final_output


    
# print(netprofit()) #test