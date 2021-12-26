def add_digits(num):
    result = 0
    for i in str(num):
        result += int(i)
    return result

if __name__ == "__main__":
    num = input("Enter an integer\n")
    try:
        print(add_digits(int(num)))
    except Exception as e:
        print("This is not an integer. Exiting!\n" + str(e))
