"""Worked examples for Lecture 2: Basic Python.

Run from this folder with: python basic_python.py
All household amounts are synthetic and measured in EUR per month.
No external packages or data files are needed.
"""

# Inputs, calculations, and labelled output.
income = 1000
consumption = 800
saving = income - consumption
print("Monthly saving (EUR):", saving)

# Recompute derived values after changing an input.
income = 1200
print("Previously calculated saving (EUR):", saving)
saving = income - consumption
print("Recalculated saving (EUR):", saving)

# A share is stored as a fraction; percent formatting handles the display.
saving_share = saving / income
print(f"Saving rate: {saving_share:.1%}")

# Convert numeric text before arithmetic.
income_text = "1200"
bonus = 100
income = float(income_text)
print("Income plus bonus (EUR):", income + bonus)

# Comparisons and Boolean combinations.
income = 1200
household_size = 2
eligible = (income <= 1200) and (household_size >= 2)
print("Meets the invented eligibility rule:", eligible)
income = 1201
eligible = (income <= 1200) and (household_size >= 2)
print("After changing income and recalculating:", eligible)

# Select items, replace one item, and append one new item.
incomes = [1000, 1200, 800]
print("First, last, first two:", incomes[0], incomes[-1], incomes[:2])
incomes[2] = 900
incomes.append(1500)
print("Updated incomes:", incomes)
print("Household count:", len(incomes))
print("Total income (EUR):", sum(incomes))
print("Mean income (EUR):", sum(incomes) / len(incomes))

# Copy a flat list before making independent changes.
original_incomes = [1000, 1200, 800]
separate_incomes = original_incomes.copy()
separate_incomes[0] = 999
print("Original incomes:", original_incomes)
print("Independent copy:", separate_incomes)

# Final classroom task: one readable household report.
household_id = "HH04"
income = 1500
consumption = 1200
household_size = 3

saving = income - consumption
saving_share = saving / income
income_per_person = income / household_size

print(f"{household_id}: saving = {saving:.2f} EUR/month")
print(f"Saving rate = {saving_share:.1%}")
print(f"Income per person = {income_per_person:.2f} EUR/month")
print("Non-negative saving:", saving >= 0)
