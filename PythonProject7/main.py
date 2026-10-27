import subprocess
import sys

while True:
    print("\n=== Municipal Utility Analysis ===")
    print("1. Analyze one building")
    print("2. Yearly Analysis of one building")
    print("3. Compare two buildings")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        subprocess.run([
            sys.executable,
            "consumption_analysis.py"
        ])
    elif choice == "2":
        subprocess.run([
            sys.executable,
            "yearly_analysis.py"
        ])
    elif choice == "3":
        subprocess.run([
            sys.executable,
            "comparison_analysis.py"
        ])

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
