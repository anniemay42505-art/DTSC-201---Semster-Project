import matplotlib.pyplot as plt
from data_loader import df, utilities

#print available locations
locations = sorted(df["location"].dropna().unique())

print("AVAILABLE LOCATIONS")
for location in locations:
    print(location)

#print available years
years = sorted(df["date"].dropna().dt.year.unique())

print("\nAVAILABLE YEARS")
for year in years:
    print(year)

#print available utilities
print("\nAVAILABLE UTILITIES")
for number, utility in utilities.items():
    print(number + ".", utility[0])


# user selections

while True:

    print("\nSELECT A LOCATION")
    for number, location in enumerate(locations, start=1):
        print(f"{number}. {location}")

    location_choice = int(input("\nEnter the number of your location: "))

    if location_choice < 1 or location_choice > len(locations):
        print("Invalid location selection.")
    else:
        selected_location = locations[location_choice - 1]

        print("\nSELECT A YEAR")
        for number, year in enumerate(years, start=1):
            print(f"{number}. {year}")

        year_choice = int(input("\nEnter the number of your year: "))

        if year_choice < 1 or year_choice > len(years):
            print("Invalid year selection.")
        else:
            selected_year = years[year_choice - 1]

            print("\nSELECT A UTILITY")
            for number, utility in utilities.items():
                print(f"{number}. {utility[0]}")

            utility_choice = input("\nEnter the utility number: ")

            if utility_choice not in utilities:
                print("Invalid utility selection.")
            else:
                utility_name, utility_column, utility_unit = utilities[utility_choice]

                #filter
                selected_data = df[
                    (df["location"] == selected_location) &
                    (df["date"].dt.year == selected_year)
                ].copy()

                print("\n--- YOUR SELECTION ---")
                print("Location:", selected_location)
                print("Year:", selected_year)
                print("Utility:", utility_name)
                print("Unit:", utility_unit)
                print("Records found:", len(selected_data))

                if selected_data.empty:
                    print("No records were found for this selection.")
                else:
                    #selected utility consumption values
                    consumption = selected_data[utility_column].dropna()
                    #check for negatives
                    negative_values = consumption[consumption < 0]

                    if not negative_values.empty:
                        print("\nWARNING: Negative consumption values were found.")
                        print("Number of negative records:", len(negative_values))
                        print("These records should be investigated.")
                    else:
                        print("\nData quality check: No negative consumption values found.")

                    if consumption.empty:
                        print("No consumption data is available for this selection.")
                    else:
                        #monthly consumption totals
                        selected_data["month"] = selected_data["date"].dt.month

                        monthly_totals = (
                            selected_data.groupby("month")[utility_column]
                            .sum(min_count=1)
                            .reindex(range(1, 13))
                        )

                        valid_months = monthly_totals.dropna()

                        #print statistics
                        print("\n--- CONSUMPTION STATISTICS ---")
                        print("Location:", selected_location)
                        print("Year:", selected_year)
                        print("Utility:", utility_name)
                        print("Unit:", utility_unit)

                        print(f"Total consumption: {consumption.sum():,.2f}")
                        print(
                            "Average monthly consumption:",
                            f"{valid_months.mean():,.2f}"
                        )

                        print(
                            "Highest-consumption month:",
                            valid_months.idxmax(),
                            f"({valid_months.max():,.2f})"
                        )

                        print(
                            "Lowest-consumption month:",
                            valid_months.idxmin(),
                            f"({valid_months.min():,.2f})"
                        )

                        print(f"Maximum individual record: {consumption.max():,.2f}")
                        print(f"Minimum individual record: {consumption.min():,.2f}")
                        print(f"Standard deviation: {consumption.std():,.2f}")

                        #missing months
                        missing_months = monthly_totals[monthly_totals.isna()].index.tolist()

                        print(f"Months with data: {len(valid_months)} out of 12")

                        month_names = [
                            "January", "February", "March", "April",
                            "May", "June", "July", "August",
                            "September", "October", "November", "December"
                        ]
                        if missing_months:
                            missing_names = [
                                month_names[month - 1]
                                for month in missing_months
                            ]
                            print("Missing months:", ", ".join(missing_names))
                        else:
                            print("Missing months: None")

                        #monthly totals for graphing
                        #keep missing months remain visible
                        graph_data = monthly_totals.copy()

                        graph_data.index = month_names

                        #bar chart
                        graph_data.plot(
                            kind="bar",
                            title=f"{utility_name} Consumption by Month\n"
                                f"{selected_location} - {selected_year}",
                            xlabel="Month",
                            ylabel=f"Consumption ({utility_unit})",
                            figsize=(10, 5)
                        )

                        plt.xticks(rotation=45, ha="right")
                        plt.tight_layout()
                        plt.show()

                        #line graph
                        graph_data.plot(
                            kind="line",
                            marker="o",
                            title=f"{utility_name} Consumption Trend\n"
                                f"{selected_location} - {selected_year}",
                            xlabel="Month",
                            ylabel=f"Consumption ({utility_unit})",
                            figsize=(10, 5)
                        )

                        plt.xticks(rotation=45, ha="right")
                        plt.tight_layout()
                        plt.show()

                        #user wants another analysis
                        again = input("\nWould you like to analyze another selection? (y/n): ")

                        if again.lower() != "y":
                            print("Thank you for using the consumption analysis program!")
                            break