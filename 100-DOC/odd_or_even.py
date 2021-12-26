def odd_or_even(number):
    return 'Even' if number%2 == 0 else 'Odd'

number = int(input("Which number do you want to check? "))
so = odd_or_even(number)
print(f"The entered number is an {so} number")