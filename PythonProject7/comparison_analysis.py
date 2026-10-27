import pandas as pd
import matplotlib.pyplot as plt
from data_loader import df, utilities


#get avalilable years and locations
available_years = sorted(df["date"].dropna().dt.year.unique())

available_locations = sorted(
    df["location"].dropna().unique()
)


#display menu and user selection
def get_choice(options, prompt):
    while True:
        choice = input(prompt)

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(options):
                return options[choice - 1]

        print("Invalid choice. Please enter a number from the menu.")


#list of options
def display_options(options):
    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")


#compare two locations
while True:
    print("\n--- Municipal Utility Comparison ---")

    #year
    print("\nAvailable years:")
    display_options(available_years)

    year = get_choice(
        available_years,
        "Choose a year by number: "
    )

    #utility
    print("\nAvailable utilities:")
    utility_choices = list(utilities.keys())

    for number, key in enumerate(utility_choices, start=1):
        name, column, unit = utilities[key]
        print(f"{number}. {name} ({unit})")

    utility_number = get_choice(
        [str(number) for number in range(1, len(utility_choices) + 1)],
        "Choose a utility by number: "
    )

    utility_key = utility_choices[int(utility_number) - 1]
    utility_name, utility_column, unit = utilities[utility_key]

    #location 1
    print("\nAvailable locations:")
    display_options(available_locations)

    location1 = get_choice(
        available_locations,
        "Choose the FIRST location by number: "
    )

    #location 2
    location2_options = [
        location for location in available_locations
        if location != location1
    ]

    print("\nChoose a second, different location:")
    display_options(location2_options)

    location2 = get_choice(
        location2_options,
        "Choose the SECOND location by number: "
    )

    #filter dataset with selected year and locations
    selected_data = df[
        (df["date"].dt.year == year)
        & (df["location"].isin([location1, location2]))
    ].copy()

    #stop if neither location has records for the chosen year
    if selected_data.empty:
        print("No records found for that year.")
        continue

    #monthly total for each location
    selected_data["month"] = selected_data["date"].dt.month

    monthly_totals = {}

    for location in [location1, location2]:
        location_data = selected_data[
            selected_data["location"] == location
        ]

        monthly_totals[location] = (
            location_data.groupby("month")[utility_column]
            .sum(min_count=1)
            .reindex(range(1, 13))
        )

    #check both locations have consumption data
    if all(
        totals.isna().all()
        for totals in monthly_totals.values()
    ):
        print("No consumption data is available for either location.")
        continue

    #missing months for each location
    month_names = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    for location, totals in monthly_totals.items():
        missing_months = [
            month_names[index - 1]
            for index, value in totals.items()
            if pd.isna(value)
        ]

        if missing_months:
            print(f"\nMonths without data for {location}:")
            print(", ".join(missing_months))
        else:
            print(f"\nAll months have data for {location}.")

    #either location has zero consumption for every month
    for location, totals in monthly_totals.items():
        if (totals.fillna(0) == 0).all():
            print(
                f"\nWARNING: {location} has zero recorded "
                f"consumption for every month."
            )

    #grouped bar chart
    months = list(range(1, 13))
    bar_width = 0.4

    plt.figure(figsize=(12, 6))

    plt.bar(
        [month - bar_width / 2 for month in months],
        monthly_totals[location1].values,
        bar_width,
        label=location1
    )

    plt.bar(
        [month + bar_width / 2 for month in months],
        monthly_totals[location2].values,
        bar_width,
        label=location2
    )

    plt.title(
        f"{utility_name} Comparison: {location1} vs. {location2} ({year})"
    )
    plt.xlabel("Month")
    plt.ylabel(f"Consumption ({unit})")
    plt.xticks(months, month_names, rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.show()

    #user wants another comparison?
    again = input(
        "\nWould you like to make another comparison? (yes/no): "
    ).strip().lower()

    if again not in ["yes", "y"]:
        print("Comparison program finished.")
        break
