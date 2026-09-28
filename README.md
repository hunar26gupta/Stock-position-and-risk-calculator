# Stock Position & Risk Calculator

A modular Python Command Line Interface (CLI) application engineered to assist retail traders and investors in managing risk, calculating precise position sizing, analyzing risk-to-reward ratios, and maintaining persistent historical trade records.

---

##  Project Overview

In equity and stock trading, capital preservation is paramount. Emotional decision-making, improper position sizing, and uncontrolled risk exposure are primary reasons retail traders experience significant drawdowns. 

The **Stock Position & Risk Calculator** provides an automated, mathematical framework for trade execution. By evaluating account equity, maximum allowable percentage loss per trade, entry price, stop-loss level, and expected profit targets, the system calculates exact share quantities and risk metrics before executing a trade. Executed trades are persistently logged for auditing and strategy analysis.

---

##  Features

- **Automated Position Sizing:** Calculates maximum allowable shares without exceeding user-defined risk limits.
- **Risk-to-Reward Analysis:** Computes actual risk, expected reward, percentage exposure, and risk-to-reward (R:R) ratios.
- **Trade Recommendation Classifier:** Automatically evaluates trade quality (e.g., `GOOD TRADE`, `AVERAGE TRADE`, `HIGH RISK TRADE`) based on R:R thresholds.
- **Strict Input Validation:** Handles invalid user inputs (e.g., negative capital, target below entry, stop-loss above entry) with informative error handling.
- **Persistent Audit Logging:** Appends trade history into `trade_history.txt` with timestamps and calculated financial metrics.
- **Interactive Record Viewer:** Allows users to query and view historical trade records directly from the command-line interface.

---

## Technologies & Tools Used
- **Programming Language:** Python 3.8+
- **Standard Libraries:** `datetime` (for timestamp generation)
- **File I/O:** Native Python file handling (`open()`, `with` context managers)
- **Version Control:** Git & GitHub

---

##  Steps to Install & Run the Project

### Prerequisites
Ensure Python 3.8 or higher is installed on your local machine.

```bash
python --version
```

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/stock-position-calculator.git
   cd stock-position-calculator
   ```

2. **Verify project structure:**
   Ensure the following modular Python files are present in the directory:
   - `Main code.py` (CLI entry point)
   - `calculator_main.py` (Position sizing logic)
   - `analysis_main.py` (Risk evaluation module)
   - `trade_history.py` (Persistent storage I/O)

3. **Execute the Application:**
   ```bash
   python "Main code.py"
   ```

---

##  Instructions for Testing

To verify the calculations, validation logic, and file storage functions:

### Test Case 1: Valid Inputs & Ideal R:R Trade
- **Capital:** `100000`
- **Max Loss (%):** `2`
- **Entry Price:** `500`
- **Stop Loss Price:** `480`
- **Target Price:** `560`
- **Expected Outcome:** 
  - Max Risk = ₹2000
  - Risk per share = ₹20
  - Shares = 100
  - Risk:Reward Ratio = 1 : 3.0
  - Recommendation = `GOOD TRADE`

### Test Case 2: Validation Failure (Stop Loss > Entry)
- **Capital:** `50000`
- **Max Loss (%):** `1`
- **Entry Price:** `200`
- **Stop Loss Price:** `210` *(Invalid)*
- **Target Price:** `250`
- **Expected Outcome:** Program triggers `ERROR: Entry price must be greater than Stop-Loss price.` without crashing.

---

## Terminal Execution Output (Simulated)

```text
===== STOCK POSITION & RISK CALCULATOR =====
Enter Capital Amount: 100000
Enter Maximum Loss (%): 2
Enter Entry Price: 500
Enter Stop-Loss Price: 480
Enter Expected Target Price: 560

----- CALCULATION RESULTS -----
Number of Shares: 100
Capital Invested: ₹ 50000.0
Remaining Capital: ₹ 50000.0
Actual Risk: ₹ 2000.0
Expected Profit: ₹ 6000.0
Risk Percentage: 2.0 %
Reward Percentage: 6.0 %
Risk : Reward: 1 : 3.0
Recommendation    : GOOD TRADE

Do you want to view previous trades? (yes/no): yes
====PREVIOUS TRADES====
Date: 2026-09-27 12:00:00.000000
Entry Price: ₹500.0
Stop Loss: ₹480.0
Target: ₹560.0
Shares: 100
Capital Invested: ₹50000.0
Risk: ₹2000.0
Expected Reward: ₹6000.0
Risk : Reward: 1 : 3.0
Status: GOOD TRADE
--------------------------------------------------
```