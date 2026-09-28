from datetime import datetime
def save_trade(entry, stop_loss, target, shares,
               invested, risk, reward, ratio, status):
    with open("trade_history.txt", "a") as file:
        file.write("Date: " + str(datetime.now()) + "\n")
        file.write("Entry Price: ₹" + str(entry) + "\n")
        file.write("Stop Loss: ₹" + str(stop_loss) + "\n")
        file.write("Target: ₹" + str(target) + "\n")
        file.write("Shares: " + str(shares) + "\n")
        file.write("Capital Invested: ₹" + str(invested) + "\n")
        file.write("Risk: ₹" + str(risk) + "\n")
        file.write("Expected Reward: ₹" + str(reward) + "\n")
        file.write("Risk : Reward: 1 : " + str(ratio) + "\n")
        file.write("Status: " + str(status) + "\n")
        file.write("-" * 50 + "\n")
        
def show_previous_trades():
    choice = input("\nDo you want to view previous trades? (yes/no): ")
    if choice=="yes":
        try:
            with open("trade_history.txt","r") as file:
                records = file.read()
            if records:
                print("====PREVIOUS TRADES====")
                print(records)
            else:
                print("\nNo previous trades found.")
        except FileNotFoundError:
            print("\nNo previous trades found.")
    elif choice=="no":
        print("\nPrevious records not displayed.")
    else:
        print("\nPlease enter yes or no.")