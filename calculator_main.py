def calculate_position(capital,loss_percent,entry,stop_loss):
    max_loss=capital*loss_percent/100
    risk_per_share =entry-stop_loss
    shares=int(max_loss/risk_per_share)
    invested=shares*entry
    actual_loss=shares*risk_per_share
    remaining_capital=capital-invested
    return shares,invested,actual_loss,remaining_capital