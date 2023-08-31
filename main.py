import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import sys


def build_visualizer(filename):
    try:
        data = pd.read_excel(filename, sheet_name="Sheet2")
        check_in_date = data["Check In Date"]
        check_in_time = data["Check In Time"]

        # Create a list to store all check-in times
        all_check_ins = []

        # Convert time strings to datetime objects and accumulate all check-in times
        for date, time in zip(check_in_date, check_in_time):
            try:
                parsed_time = datetime.strptime(time, "%I:%M %p")
            except ValueError:
                # Handle the case where "ET" is present in the time string
                cleaned_time = time.replace(" ET", "")
                parsed_time = datetime.strptime(cleaned_time, "%I:%M %p")
            all_check_ins.append(parsed_time)

        # Extract hours from datetime objects
        check_in_hours = [time.hour + time.minute / 60 for time in all_check_ins]

        # Create a histogram to show frequency of check-in times
        plt.figure()
        plt.hist(check_in_hours, bins=12, alpha=0.5, edgecolor="black")

        plt.xlabel("Time (hours)")
        plt.ylabel("Frequency")
        plt.title("Check In Times Frequency")
        plt.show()

    except FileNotFoundError:
        print("File not found. Please try again.")
        sys.exit()


def main():
    print("Welcome to Kaushal's MaCSTC Data Visualizer")
    print("-------------------------------------------")
    print("Please select an option from the menu below:")
    print("1. View a frequency distribution of the data")
    print("2. Exit the program")
    print("-------------------------------------------")
    input_value = input("Please enter your selection: ")

    if input_value == "1":
        input_value = input("Please enter the file name without the .xlsx (E.G Fall2019Week instead of "
                            "Fall2019Week.xlsx): ")
        build_visualizer(f"./data/{input_value}.xlsx")
    elif input_value == "2":
        print("Goodbye!")
        sys.exit(1)


if __name__ == "__main__":
    main()
