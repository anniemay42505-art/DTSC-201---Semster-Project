import pandas as pd
import matplotlib.pyplot as plt
from data_loader import df, utilities, display_options


#available locations
available_locations = sorted(df["location"].dropna().unique())


#numbered menu
def get_choice(options, prompt):
    while True:
        choice = input(prompt)

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(options):
                return options[choice - 1]

        print("Invalid choice. Please enter a number from the menu.")

while True:
    print("\n=== Single Building: Yearly Analysis ===")

    # Choose a building
    print("\nAvailable locations:")
    display_options(available_locations)

    location = get_choice(
        available_locations,
        "Choose a location by number: "
    )

    #utility
    print("\nAvailable utilities:")
    utility_keys = list(utilities.keys())

    for number, key in enumerate(utility_keys, start=1):
        name, column, unit = utilities[key]
        print(f"{number}. {name} ({unit})")

    utility_key = get_choice(
        [str(number) for number in range(1, len(utility_keys) + 1)],
        "Choose a utility by number: "
    )

    utility_key = utility_keys[int(utility_key) - 1]
    utility_name, utility_column, unit = utilities[utility_key]

    #data for selected building
    selected_data = df[
        df["location"] == location
    ].copy()

    selected_data = selected_data.dropna(
        subset=["date", utility_column]
    )

    if selected_data.empty:
        print("No usable data found for this location.")
        continue

    #negative consumption values
    negative_values = selected_data[
        selected_data[utility_column] < 0
    ]

    if not negative_values.empty:
        print(
            "\nWARNING: Found",
            len(negative_values),
            "records with negative consumption."
        )

    #consumption by year
    selected_data["year"] = selected_data["date"].dt.year

    yearly_totals = (
        selected_data.groupby("year")[utility_column]
        .sum(min_count=1)
    )

    #max and min for individual records
    max_row = selected_data.loc[
        selected_data[utility_column].idxmax()
    ]

    min_row = selected_data.loc[
        selected_data[utility_column].idxmin()
    ]

    print("\nHighest individual consumption record:")
    print(f"Value: {max_row[utility_column]:,.2f} {unit}")
    print(f"Date: {max_row['date'].date()}")

    print("\nLowest individual consumption record:")
    print(f"Value: {min_row[utility_column]:,.2f} {unit}")
    print(f"Date: {min_row['date'].date()}")

    all_years = list(
        range(
            int(df["date"].dt.year.min()),
            int(df["date"].dt.year.max()) + 1
        )
    )

    yearly_totals = yearly_totals.reindex(all_years)

    print(f"\nLocation: {location}")
    print(f"Utility: {utility_name} ({unit})")
    print("\nAnnual consumption totals:")

    for year, total in yearly_totals.items():
        if pd.isna(total):
            print(f"{year}: No data")
        else:
            print(f"{year}: {total:,.2f} {unit}")

    #latest year may be incomplete
    latest_year = int(df["date"].dt.year.max())

    if latest_year in yearly_totals.index:
        latest_dates = df.loc[
            (df["location"] == location)
            & (df["date"].dt.year == latest_year),
            "date"
        ]

        if not latest_dates.empty:
            latest_month = latest_dates.dt.month.max()

            if latest_month < 12:
                print(
                    f"\nNote: {latest_year} may be incomplete. "
                    f"Data for this location ends in month {latest_month}."
                )

    #yearly bar chart
    plt.figure(figsize=(10, 6))

    plt.bar(
        yearly_totals.index,
        yearly_totals.values
    )

    plt.title(
        f"Yearly {utility_name} Consumption\n{location}"
    )
    plt.xlabel("Year")
    plt.ylabel(f"Total Consumption ({unit})")
    plt.xticks(all_years, rotation=45)
    plt.tight_layout()
    plt.show()

    #user want another analysis?
    again = input(
        "\nWould you like to analyze another building? (yes/no): "
    ).strip().lower()

    if again not in ["yes", "y"]:
        print("Yearly analysis finished.")
        break
