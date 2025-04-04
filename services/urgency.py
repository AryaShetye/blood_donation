def calculate_urgency(age, heart_rate, bp, oxygen):
    urgency = (abs(80 - heart_rate) * 0.4) + (abs(120 - bp) * 0.2) + ((100 - oxygen) * 0.2) + (age * 0.2)
    return round(urgency, 2)

