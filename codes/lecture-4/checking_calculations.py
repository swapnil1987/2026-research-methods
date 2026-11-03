"""Worked checks for Lecture 4; all household amounts are synthetic EUR/month.

Run with: python checking_calculations.py
The deliberate errors shown in the slides are not executed by this script.
"""

from math import isclose


def saving(income, consumption):
    return income - consumption


def saving_share(income, consumption):
    """Use the course contract for numeric, finite monthly input amounts."""
    if income < 0 or consumption < 0:
        raise ValueError("Amounts must be non-negative")
    if income == 0:
        return None
    return (income - consumption) / income


# Hand-worked cases: positive, zero and negative saving are meaningful.
assert saving(1000, 800) == 200
assert saving(1000, 1000) == 0
assert saving(800, 850) == -50
print("Saving amount checks passed")

# A small tolerance accommodates floating-point representation.
assert isclose(0.1 + 0.2, 0.3, rel_tol=1e-9, abs_tol=1e-12)
assert isclose(saving_share(1000, 800), 0.2)
assert isclose(saving_share(800, 850), -0.0625)
assert saving_share(0, 100) is None
print("Saving share checks passed")

# Required input validation belongs in the function, not an assertion.
try:
    saving_share(-100, 50)
except ValueError as error:
    assert str(error) == "Amounts must be non-negative"
    print("Invalid input rejected:", error)
else:
    raise AssertionError("Negative income was not rejected")

income = 1200
consumption = 800
print("Fresh calculation (EUR/month):", saving(income, consumption))
