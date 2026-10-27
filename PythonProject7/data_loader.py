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