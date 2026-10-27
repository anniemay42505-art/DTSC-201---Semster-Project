import pandas as pd

#load dataset
df = pd.read_csv("Data.csv")

#date column into dates
df["date"] = pd.to_datetime(df["date"], errors="coerce")

#utility columns with units
utilities = {
    "1": ("Electricity", "elec_use_kwh", "kWh"),
    "2": ("Natural Gas", "nat_gas_use_mcf", "MCF"),
    "3": ("Steam", "steam_use_klbs", "thousand pounds"),
    "4": ("Water", "water_use_kgal", "thousand gallons"),
    "5": ("Wastewater", "wastewater_use_kgal", "thousand gallons")
}
#month names for graphs
month_names = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
def display_options(options, columns=3):
    #how many rows needed
    rows = (len(options) + columns - 1) // columns

    # Find the width needed for each column
    width = max(len(option) for option in options) + 8

    #options down each column
    for row in range(rows):
        for col in range(columns):
            index = row + col * rows

            if index < len(options):
                number = index + 1
                print(
                    f"{number}. {options[index]:<{width - 5}}",
                    end=""
                )

        print()
