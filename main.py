from pathlib import Path
import cash_on_hand
import overheads
import profit_loss

file_path = Path.cwd()/"summary_report.txt"
#writes results into the text file
with file_path.open(mode = "w") as file:
    file.write(overheads.topoverhead() + '\n') #newline
    file.write(cash_on_hand.cashonhand())
    file.write(profit_loss.netprofit())