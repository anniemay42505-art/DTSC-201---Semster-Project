import subprocess
import sys

while True:
    print("\n=== Municipal Utility Analysis ===")
    print("1. Analyze one building")
    print("2. Compare two buildings")
    print("3. Exit")

    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
        subprocess.run([
            sys.executable,
            "consumption_analysis.py"
        ])

    elif choice == "2":
        subprocess.run([
            sys.executable,
            "comparison_analysis.py"
        ])

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
