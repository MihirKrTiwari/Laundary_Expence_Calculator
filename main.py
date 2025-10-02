import csv
import os
from datetime import date

# setting price for the washing clothes per Kg
PRICEPERKG = 75

def Input():

    # Taking input for date and checking if the data input is correct or not and if not correct or data is missing then auto genereate the date
    Date = input("Enter the date (yyyy-mm-dd): ")
    if Date:
        try:
            year, month, day = map(int, Date.split('-'))
            Date = date(year, month, day).isoformat()
        except ValueError:
            print("Invalid date! Using today's date instead.")
            Date = date.today().isoformat()
    else:
        Date = date.today().isoformat()

    # Asking user to input the total weight of the clothes
    weight = float(input("Enter your cloths weight(Kg): "))

    # Asking user to input the quantity of the cloths and types of the cloths
    quantity = int(input("Enter the number of clothes: "))
    clothList = []
    for i in range(quantity):
        cloth_type = input(f"Enter the {i+1} type of cloth: ")
        clothList.append(cloth_type)

    # Calculating total price
    cost = weight * PRICEPERKG

    file_exists = os.path.isfile("Cloth_expence.csv")

    # writing the data in the csv file
    with open("Cloth_expence.csv", 'a', newline="") as f:
        writer = csv.writer(f)

        # Write header only if file is new/empty
        if not file_exists or os.path.getsize("Cloth_expence.csv") == 0:
            writer.writerow(["Date", "Weight(kg)", "Quantity", "Cost", "Cloth Types"])

        writer.writerow([Date, weight, quantity, cost, set(clothList)])
        
    print("Data input successfully...")


def CalMonth():
    totalWeight = 0
    totalCost = 0
    year = input("Enter the year: ")
    month = input("Enter the month: ")

    # Reading the csv file
    with open("Cloth_expence.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)  # ✅ skip header row

        for row in reader:
            y, m, d = row[0].split('-')
            if y == year and m == month:
                print(row, "\n")
                totalWeight += float(row[1])
                totalCost += float(row[3])

        print("Total weight:\t", totalWeight)
        print("Total cost:\t", totalCost)


def CalYear():
    totalWeight = 0
    totalCost = 0
    year = input("Enter the year: ")

    # Reading the csv file
    with open("Cloth_expence.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)  # ✅ skip header row

        for row in reader:
            y, m, d = row[0].split('-')
            if y == year:
                print(row, "\n")
                totalWeight += float(row[1])
                totalCost += float(row[3])

        print("Total weight:\t", totalWeight)
        print("Total cost:\t", totalCost)


def main():
    while True:

        # Staring line
        print("--------------------------------")
        print("Enter exit to exit the program: ")
        print("Enter 1 to add data")
        print("Enter 2 to read monthly cost")
        print("Enter 3 to lear yearly cost: ")
        print("--------------------------------")
        user_input = input("Enter --> ")
        if user_input == "exit":
            break
        elif user_input == "1":
            Input()
        elif user_input == "2":
            CalMonth()
        elif user_input == "3":
            CalYear()
        else:
            print("Invalid input")

        
main()