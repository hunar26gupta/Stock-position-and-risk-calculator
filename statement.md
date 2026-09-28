# Project Statement & Scope Document

## 1. Problem Statement
Retail traders frequently suffer severe capital drawdowns due to unscientific position sizing and failure to strictly enforce risk management rules prior to trade execution. Standard retail order screens ask for share quantities rather than risk tolerances, forcing traders to perform manual arithmetic under fast-moving market conditions. This leads to common pitfalls such as over-leveraging, setting arbitrary stop-losses, accepting poor risk-to-reward profiles, and failing to maintain systematic trading journals.

## 2. Scope of the Project
The **Stock Position & Risk Calculator** addresses these trading vulnerabilities by automating position sizing and trade metric evaluation.

### Included in Scope:
- Mathematical determination of maximum allowable position sizes based on explicit risk percentage caps.
- Instant evaluation of Risk-to-Reward (R:R) ratios, capital allocation, and risk percentages relative to invested equity.
- Categorization of trades into risk tiers (`GOOD TRADE`, `AVERAGE TRADE`, `HIGH RISK TRADE`).
- Comprehensive error validation preventing invalid pricing orders (e.g., negative inputs, target below entry, stop-loss above entry).
- Persistent trade history logging to local file storage for record-keeping and auditability.
- Interactive terminal-based display of historical trades.

### Out of Scope:
- Direct broker API integration for live automated order placement.
- Real-time stock ticker price feeds via web sockets.
- Graphical User Interface (GUI) or mobile app interface (pure CLI focus).

## 3. Target Users
- **Day Traders & Swing Traders:** Individuals who need immediate position sizing rules prior to entering market positions.
- **Beginner Investors:** Novice market participants learning quantitative risk management concepts and discipline.
- **Financial Analysts & Students:** Users looking for a structured Python tool to study portfolio exposure and trade mechanics.

## 4. High-Level Features
1. **Mathematical Position Sizing Engine:** Computes optimal share count based on maximum capital loss limits.
2. **Quantitative Risk Analyzer:** Computes exact R:R metrics, percentages, and trade classification.
3. **Data Validation Module:** Sanitizes and checks logical constraints on user inputs before processing.
4. **Local Audit Logger:** Writes full execution metadata into a structured log text file (`trade_history.txt`).
5. **Interactive Console Dashboard:** Clean, user-friendly interface for input collection and reporting.