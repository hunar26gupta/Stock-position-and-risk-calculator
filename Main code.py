from calculator_main import calculate_position 
from analysis_main import analyze_risk 
from trade_history import save_trade, show_previous_trades 

print("===== STOCK POSITION & RISK CALCULATOR =====") 

try: 
    # Taking input from the user 
    capital = float(input("Enter Capital Amount: ")) 
    loss_percent = float(input("Enter Maximum Loss (%): ")) 
    entry = float(input("Enter Entry Price: ")) 
    stop_loss = float(input("Enter Stop-Loss Price: ")) 
    target = float(input("Enter Expected Target Price: ")) 

    if capital <= 0: 
        raise ValueError("Capital must be greater than 0.") 

    if loss_percent <= 0 or loss_percent > 100: 
        raise ValueError("Maximum loss must be between 0 and 100%.") 

    if entry <= stop_loss: 
        raise ValueError("Entry price must be greater than Stop-Loss price.") 

    if target <= entry: 
        raise ValueError("Target price must be greater than Entry price.") 
     
    shares, invested, actual_loss, remaining = calculate_position( 
    capital, loss_percent, entry, stop_loss) 
     
    risk, reward, risk_percent, reward_percent, ratio, status = analyze_risk( 
    entry, stop_loss, target, shares) 
     
    print("----- CALCULATION RESULTS -----") 
    print("Number of Shares:", shares) 
    print("Capital Invested: ₹", invested) 
    print("Remaining Capital: ₹", remaining) 
    print("Actual Risk: ₹", actual_loss) 
    print("Expected Profit: ₹", reward) 
    print("Risk Percentage:", risk_percent, "%") 
    print("Reward Percentage:", reward_percent, "%") 
    print("Risk : Reward: 1 :", ratio) 
    print("Recommendation    :", status)
 
    save_trade(entry, stop_loss, target, shares, 
        invested, risk, reward, ratio, status) 
 
    show_previous_trades() 
 
except ValueError as error: 
    print("\nERROR:", error)