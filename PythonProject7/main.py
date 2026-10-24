import pandas as pd
import matplotlib.pyplot as plt
import seaborn

df = pd.read_csv("Data.csv")
df["date"] = pd.to_datetime(df["date"])
dfsort = df.sort_values("date")


df2026 = dfsort[dfsort["date"].dt.year == 2026]
df2025 = dfsort[dfsort["date"].dt.year == 2025]
df2024 = dfsort[dfsort["date"].dt.year == 2024]
df2023 = dfsort[dfsort["date"].dt.year == 2023]
df2022 = dfsort[dfsort["date"].dt.year == 2022]
df2021 = dfsort[dfsort["date"].dt.year == 2021]
df2020 = dfsort[dfsort["date"].dt.year == 2020]
df2019 = dfsort[dfsort["date"].dt.year == 2019]
df2018 = dfsort[dfsort["date"].dt.year == 2018]
df2017 = dfsort[dfsort["date"].dt.year == 2017]
df2016 = dfsort[dfsort["date"].dt.year == 2016]
#Part 1 of Code Allegheny County Medical Examiner Stats
print("Press E to see overview of past decade Allegheny County Medical Examiner total energy cost")

if input("") == "E":
    bulidname = "Allegheny County Medical Examiner"
    locationname = "ACMEO Parking Lot"
    df2026fit = df2026[
    (df2026["bldg_grp"] == bulidname) &
    (df2026["location"] == locationname) & df2026["total_energy_cost"] > 0]
    print(df2026fit[["date", "bldg_grp", "location", "total_energy_cost"]])
    df2025fit = df2025[
    (df2025["bldg_grp"] == bulidname) &
    (df2025["location"] == locationname) & df2025["total_energy_cost"] > 0]
    print(df2025fit[["date", "bldg_grp", "location", "total_energy_cost"]])
    df2024fit = df2024[
    (df2024["bldg_grp"] == bulidname) &
    (df2024["location"] == locationname) & df2024["total_energy_cost"] > 0]
    print(df2024fit[["date", "bldg_grp", "location", "total_energy_cost"]])
    df2023fit = df2023[
    (df2023["bldg_grp"] == bulidname) &
    (df2023["location"] == locationname) & df2023["total_energy_cost"] > 0]
    print(df2023fit[["date", "bldg_grp", "location", "total_energy_cost"]])
    df2022fit = df2022[
    (df2022["bldg_grp"] == bulidname) &
    (df2022["location"] == locationname) & df2022["total_energy_cost"] > 0]
    print(df2022fit[["date", "bldg_grp", "location", "total_energy_cost"]])
    df2021fit = df2021[
    (df2021["bldg_grp"] == bulidname) &
    (df2021["location"] == locationname) & df2021["total_energy_cost"] > 0]
    print(df2023fit[["date", "bldg_grp", "location", "total_energy_cost"]])
    df2020fit = df2020[
    (df2020["bldg_grp"] == bulidname) &
    (df2020["location"] == locationname) & df2020["total_energy_cost"]]
    print(df2020fit[["date", "bldg_grp", "location", "total_energy_cost"]])
    df2019fit = df2019[
    (df2019["bldg_grp"] == bulidname) &
    (df2016["location"] == locationname) & df2019["total_energy_cost"] > 0]
    print(df2019fit[["date", "bldg_grp", "location", "total_energy_cost"]])
    df2018fit = df2018[
    (df2018["bldg_grp"] == bulidname) &
    (df2018["location"] == locationname) & df2018["total_energy_cost"] > 0]
    print(df2018fit[["date", "bldg_grp", "location", "total_energy_cost"]])
    df2017fit = df2017[
    (df2017["bldg_grp"] == bulidname) &
    (df2017["location"] == locationname) & df2017["total_energy_cost"] > 0]
    print(df2017fit[["date", "bldg_grp", "location", "total_energy_cost"]])
    df2016fit = df2016[
    (df2016["bldg_grp"] == bulidname) &
    (df2016["location"] == locationname) & df2016["total_energy_cost"] > 0]
    print(df2016fit[["date", "bldg_grp", "location", "total_energy_cost"]])

    plt.plot(df2026fit["date"], df2026fit["total_energy_cost"], marker="o", label = "2026")
    plt.plot(df2025fit["date"], df2025fit["total_energy_cost"], marker="o", label = "2025")
    plt.plot(df2024fit["date"], df2024fit["total_energy_cost"], marker="o", label = "2024")
    plt.plot(df2023fit["date"], df2023fit["total_energy_cost"], marker="o", label = "2023")
    plt.plot(df2022fit["date"], df2022fit["total_energy_cost"], marker="o", label = "2022")
    plt.plot(df2021fit["date"], df2021fit["total_energy_cost"], marker="o", label = "2021")
    plt.plot(df2020fit["date"], df2020fit["total_energy_cost"], marker="o", label = "2020")
    plt.plot(df2019fit["date"], df2019fit["total_energy_cost"], marker="o", label = "2019")
    plt.plot(df2018fit["date"], df2018fit["total_energy_cost"], marker="o", label = "2018")
    plt.plot(df2017fit["date"], df2017fit["total_energy_cost"], marker="o", label = "2017")
    plt.plot(df2016fit["date"], df2016fit["total_energy_cost"], marker="o", label = "2016")
    plt.xlabel("Year")
    plt.ylabel("Total Energy Cost")
    plt.title("Energy Cost Trend Numbers Overview of Last Decade\nAllegheny County Medical Examiner")
    plt.legend(loc="upper right", fontsize="6")
    plt.show()
else:
    print("Move on")

def graph_building(year, building, stat, dfsort):

    data = dfsort[
        (dfsort["date"].dt.year == year) &
        (dfsort["bldg_grp"] == building) &
        (dfsort[stat] > 0)
    ]

    if data.empty:
        print("No data found.")
        return

    max_row = data.loc[data[stat].idxmax()]
    min_row = data.loc[data[stat].idxmin()]

    print("\nMaximum", stat)
    print(max_row[stat], "on", max_row["date"])

    print("\nMinimum", stat)
    print(min_row[stat], "on", min_row["date"])

    plt.plot(data["date"], data[stat], marker="o")
    plt.xlabel("Date")
    plt.ylabel(stat)
    plt.title(f"{building} - {stat} ({year})")
    plt.show()


while True:

    year = input("Enter year 2016-2026 but not 2019 or 2020, (or Leave): ")

    if year.lower() == "leave":
        break

    building = input("Enter building, options are: Allegheny County Medical Examiner,Boyce Park,Deer Lakes,Downtown Facilities,Allegheny County Jail  : ")

    if building.lower() == "leave":
        break

    stat = input(
        "Enter statistic (total_energy_cost total_tons_co2,toal_energy_use_mmbtu,water_use_kgal,wastewater_use_kgal,elec_cost,nat_gas_cost,steam_cost,water_cost,wastewater_cost,total_utility_cost,elec_tons_co2,nat_gas_tons_co2,steam_tons_co2 ): "
    )

    if stat.lower() == "leave":
        break

    graph_building(
        int(year),
        building,
        stat,
        dfsort
    )

print("Move on")

