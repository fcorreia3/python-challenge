import os;
import csv;

resource_file = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("Resources", "output.txt")


total_months = 0 # The total number of months included in the dataset
total_net_profit = 0 # The net total amount of "Profit/Losses" over the entire period
max_profit_increase = float("inf") # The greatest increase in losses (date and amount) over the entire period
max_profit_decrease = float("inf") # The greatest decrease in losses (date and amount) over the entire period
max_profit_increase_month = ""
max_profit_decrease_month = ""
total_profit_change = 0

with open(resource_file) as budget_data:
    data = csv.reader(budget_data)

    # Header
    header = next(data)

    # First row
    first_row_data = next(data)
    first_month_profit = float(first_row_data[1])
    profit_month_t = first_month_profit

    # Rest of the data
    for row in data:

        month_t1 = row[0]
        profit_month_t1 = float(row[1])

        # Calculate aggregates
        total_months = total_months + 1
        total_net_profit = total_net_profit + profit_month_t1
        
        # Calculate changes
        profit_increase = profit_month_t1 - profit_month_t
        total_profit_change = total_profit_change + profit_increase
        
        if(profit_increase > max_profit_increase):
            max_profit_increase = profit_increase
            max_profit_increase_month = month_t1

        if(profit_increase < max_profit_decrease):
            max_profit_decrease = profit_increase
            max_profit_decrease_month = month_t1

        #reset
        month_t = month_t1

    # The average of the changes in "Profit/Losses" over the entire period    
    avg_profit_change = total_profit_change/total_months
    
    # Total net profits
    total_net_profit = total_net_profit + first_month_profit

    output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Net Profit: ${total_net_profit}\n"
    f"Average Monthly Change: ${avg_profit_change:.2f}\n"
    f"Greatest Increase in Profits: ${max_profit_increase} ({max_profit_increase_month})\n"
    f"Greatest Decrease in Profits: ${max_profit_decrease} ({max_profit_decrease_month})\n")
    
# Export the results to text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)
