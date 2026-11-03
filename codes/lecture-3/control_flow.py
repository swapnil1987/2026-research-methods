"""Worked functions and examples for Lecture 3.

All amounts are synthetic EUR per month. These introductory functions assume
numeric, finite inputs. The saving-share contract rejects negative income or
consumption, returns None for zero income, and permits negative saving.
"""


def saving_amount(income, consumption):
    """Return income minus consumption for supplied numeric amounts."""
    return income - consumption


def income_per_person(income, household_size):
    """Return income per person; require non-negative income and positive size."""
    if income < 0:
        raise ValueError("Income must be non-negative")
    if household_size <= 0:
        raise ValueError("Household size must be positive")
    return income / household_size


def saving_share(income, consumption):
    """Return a fractional saving share, or None when income is zero.

    Preconditions: income and consumption are numeric, finite amounts. The
    classroom specification rejects negative inputs, including negative
    consumption when income is zero. It does not reject negative saving.
    """
    if income < 0 or consumption < 0:
        raise ValueError("Amounts must be non-negative")
    if income == 0:
        return None
    return (income - consumption) / income


def run_examples():
    """Run the hand-checkable examples without changing any files."""
    print("Saving amounts:")
    incomes = [1000, 1200, 800]
    consumptions = [800, 900, 850]
    if len(incomes) != len(consumptions):
        raise ValueError("Input lists must have matching lengths")
    for income, consumption in zip(incomes, consumptions):
        print(saving_amount(income, consumption))

    print("Positive saving count and total:")
    positive_count = 0
    positive_total = 0
    for saving in [200, 0, -50, 300]:
        if saving > 0:
            positive_count = positive_count + 1
            positive_total = positive_total + saving
    print(positive_count, positive_total)

    print("Income per person:")
    print(income_per_person(1200, 3))
    print(income_per_person(1000, 2))

    print("Saving shares:")
    incomes = [1000, 0, 2000]
    consumptions = [800, 100, 1500]
    for income, consumption in zip(incomes, consumptions):
        share = saving_share(income, consumption)
        if share is None:
            print("Rate: undefined")
        else:
            print(f"Rate: {share:.1%}")


# Run demonstrations when executing this file; importing it only defines tools.
if __name__ == "__main__":
    run_examples()
