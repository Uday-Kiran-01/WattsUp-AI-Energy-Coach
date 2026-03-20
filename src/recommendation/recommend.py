# src/recommendations/recommend.py
def get_recommendations(row):
    cluster = int(row['cluster'])
    cost_per_kwh = 0.2
    co2_factor = 0.05
    age_profile = row.get('age_profile', None)

    if cluster == 0:
        recs = [
            "Shift energy usage to off-peak hours",
            "Reduce evening appliance usage",
            "Consider smart scheduling devices"
        ]
        kwh_savings = row['kWh'] * 0.1
    elif cluster == 1:
        recs = [
            "Maintain current efficient usage",
            "Monitor standby power consumption",
            "Optimize appliance usage timing"
        ]
        kwh_savings = row['kWh'] * 0.05
    else:
        recs = [
            "Reduce base load consumption",
            "Upgrade inefficient appliances",
            "Identify always-on devices"
        ]
        kwh_savings = row['kWh'] * 0.15

    # Tailor recommendations by age profile
    if age_profile == "senior":
        recs.append("Consider safety checks for electrical devices and avoid peak usage in the evening.")
    elif age_profile == "family":
        recs.append("Engage the whole family in energy-saving habits, especially during peak hours.")
    elif age_profile == "young_adult":
        recs.append("Leverage smart home tech and apps to monitor and reduce your energy footprint.")

    cost_savings = kwh_savings * cost_per_kwh
    co2_savings = kwh_savings * co2_factor
    return recs, kwh_savings, cost_savings, co2_savings