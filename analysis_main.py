def analyze_risk(entry, stop_loss, target, shares):
    risk_per_share = entry - stop_loss
    reward_per_share = target - entry
    risk = round(risk_per_share * shares, 2)
    reward = round(reward_per_share * shares, 2)
    risk_percent = round((risk / (entry * shares)) * 100, 2)
    reward_percent = round((reward / (entry * shares)) * 100, 2)
    ratio = round(reward_per_share / risk_per_share, 2)
    if ratio >= 3:
        status = "GOOD TRADE"
    elif ratio >= 2:
        status = "AVERAGE TRADE"
    else:
        status = "HIGH RISK TRADE"

    return risk, reward, risk_percent, reward_percent, ratio, status