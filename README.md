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

