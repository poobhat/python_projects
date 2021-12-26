
def life_in_weeks(age):
    years = (90-age)
    months = years * 12
    weeks = months * 4
    days = weeks * 7
    return int(months), int(weeks), int(days)

if __name__ == '__main__':
    age = input("Enter your age in years\n")
    try:
        if isinstance(int(age), int):
            m,w,d = life_in_weeks(int(age))
            print(f"If you were to live to the ripe old age of 90, you have {d} days, {w} weeks,"
                  f"and {m} months left")
    except Exception as e:
        print("Invalid input\nPlease try again!")
        print(str(e))