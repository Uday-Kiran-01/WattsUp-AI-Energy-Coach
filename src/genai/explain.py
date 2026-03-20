# # src/genai/explain.py
# def generate_explanation(row, recs, kwh_savings, cost_savings, co2_savings):
#     """
#     Generates customer-friendly AI explanation report.
#     """
#     text = f"""
# Customer {int(row['household_id'])} Report:

# Your energy usage is {row['kWh']:.1f} kWh daily.

# You belong to segment {int(row['cluster'])}, which reflects your consumption pattern.

# Recommendations:
# - {'; '.join(recs)}

# By applying these changes, you could save approx:
# - {kwh_savings:.1f} kWh per day
# - €{cost_savings:.2f} per day
# - {co2_savings:.2f} kg CO₂ per day
# """
#     return text

# src/genai/explain.py

def generate_customer_explanation(consumption, avg, cluster, recommendations):
    """
    Generates a textual explanation for a household customer
    based on consumption, cluster, and recommendations.

    Args:
        consumption (float): Customer's average consumption
        avg (float): Average consumption across all households
        cluster (int): Assigned cluster
        recommendations (list): List of recommendation strings

    Returns:
        str: Explanation text
    """
    diff_pct = ((consumption - avg) / avg) * 100

    cluster_desc = f"You belong to segment {int(cluster)}, which reflects your consumption pattern."
    rec_text = "\n".join(f"- {rec}" for rec in recommendations)

    explanation = (
        f"Your energy usage is {diff_pct:.1f}% {'higher' if diff_pct > 0 else 'lower'} than similar households.\n\n"
        f"{cluster_desc}\n\n"
        f"Recommendations:\n{rec_text}\n\n"
        "By applying these changes, you could save approx:\n"
        f"- {{kwh_savings:.1f}} kWh per day\n"
        f"- €{{cost_savings:.2f}} per day\n"
        f"- {{co2_savings:.2f}} kg CO₂ per day\n"
    )
    return explanation