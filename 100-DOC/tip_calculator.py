def tip_calculator(bill, tip, people):
    total_amount = bill + (bill * tip / 100)
    individual_amount = total_amount/people
    return round(individual_amount, 2)

if __name__ == '__main__':
    print("Welcome to the tip calculator\n")
    bill = input("What was the total bill?\n$")
    tip = input("What percentage tip would you like to give?\n10, 12, or 15?\n")
    people = input("How many people would like to split the bill?\n")

    try:
        bill = float(bill)
        if int(tip) not in [10, 12, 15]:
            print("Choose from 10, 12, or 15% tip\n")
            tip = input("What percentage tip would you like to give?\n10, 12, or 15?\n")
        tip = int(tip)
        people = int(people)
        individual_amount = tip_calculator(bill, tip, people)
        print(f"Each person should pay : {individual_amount}")
    except Exception as e:
        print("Invalid input. Please try again!\n")
        print(str(e))


