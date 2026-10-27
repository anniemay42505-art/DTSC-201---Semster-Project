import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Data.csv")
df["date"] = pd.to_datetime(df["date"])
dfsort = df.sort_values("date")


def graphallyears(building, stat, dfsort):

    data = dfsort[
        (dfsort["bldg_grp"] == building) &
        (dfsort[stat] > 0)
    ]

    if data.empty:
        print("No data found.")
        return

    max_row = data.loc[data[stat].idxmax()]
    min_row = data.loc[data[stat].idxmin()]

    print("Maximum", stat)
    print(max_row[stat], "on", max_row["date"])

    print("\nMinimum", stat)
    print(min_row[stat], "on", min_row["date"])

    for year in sorted(data["date"].dt.year.unique()):

        year_data = data[data["date"].dt.year == year]

        plt.bar(
            year_data["date"],
            year_data[stat],
            label=str(year)
        )

        plt.xlabel("Date")
        plt.ylabel(stat)
        plt.title(f"{building} - All Years")
        plt.legend()
    plt.show()


print("Press e for overview graph")

if input().lower() == "e":

    while True:

        building = input(
            "Enter building, options are: Allegheny County Medical Examiner,Boyce Park,Deer Lakes,Downtown Facilities,Allegheny County Jail  : ")

        if building.lower() == "leave":
            break

        stat = input(
            "Enter statistic (total_energy_cost,total_tons_co2,toal_energy_use_mmbtu,water_use_kgal,wastewater_use_kgal,elec_cost,nat_gas_cost,steam_cost,water_cost,wastewater_cost,total_utility_cost,elec_tons_co2,nat_gas_tons_co2,steam_tons_co2 ): "
        )

        if stat.lower() == "leave":
            break

        graphallyears(
            building,
            stat,
            dfsort
        )

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
print("press a to select building by year")
if input().lower() == "a":
    while True:

        year = input("Enter year 2016-2026, (or Leave): ")

        if year.lower() == "leave":
            break

        building = input("Enter building, options are: Allegheny County Medical Examiner,Boyce Park,Deer Lakes,Downtown Facilities,Allegheny County Jail  : ")

        if building.lower() == "leave":
            break

        stat = input(
            "Enter statistic (total_energy_cost,total_tons_co2,toal_energy_use_mmbtu,water_use_kgal,wastewater_use_kgal,elec_cost,nat_gas_cost,steam_cost,water_cost,wastewater_cost,total_utility_cost,elec_tons_co2,nat_gas_tons_co2,steam_tons_co2 ): "
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


def graph_compare(year, building1, building2, stat, dfsort):
    fig, (ax1, ax2) = plt.subplots(2, 1)
    data1 = dfsort[(dfsort["bldg_grp"] == building1) &
                   (dfsort["date"].dt.year == year)]

    data2 = dfsort[(dfsort["bldg_grp"] == building2) &
                   (dfsort["date"].dt.year == year)]


    ax1.plot(data1["date"], data1[stat])
    ax1.set_title(building1)
    ax1.set_ylabel(stat)

    ax2.plot(data2["date"], data2[stat])
    ax2.set_title(building2)
    ax2.set_ylabel(stat)
    ax2.set_xlabel("Date")

    plt.tight_layout()

    plt.show()
print("Press w to compare two buildings with same stat and year (Type leave at any time to exi ")
while True:
    if input().lower() == "w":
        year = int(input("Enter a year: "))
        if year == "leave":
            break
        building1 = input("Enter building, options are: Allegheny County Medical Examiner,Boyce Park,Deer Lakes,Downtown Facilities,Allegheny County Jail  : ")

        if building1.lower() == "leave":
            break
        building2 = input("Enter building, options are: Allegheny County Medical Examiner,Boyce Park,Deer Lakes,Downtown Facilities,Allegheny County Jail  : ")

        if building2.lower() == "leave":
            break
        stat = input(
            "Enter statistic (total_energy_cost,total_tons_co2,toal_energy_use_mmbtu,water_use_kgal,wastewater_use_kgal,elec_cost,nat_gas_cost,steam_cost,water_cost,wastewater_cost,total_utility_cost,elec_tons_co2,nat_gas_tons_co2,steam_tons_co2 ): "
        )

        if stat.lower() == "leave":
            break

        graph_compare(year, building1, building2, stat, dfsort)

        again = input("Graph another? (yes/no): ").lower()

        if again == "no":
            break

