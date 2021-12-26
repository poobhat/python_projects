def calculate_bmi(hight, weight):
    bmi = weight/hight**2
    if bmi <= 18.4:
        return int(bmi), 'underweight'
    elif bmi > 18.4 and bmi <= 24.9:
        return int(bmi), 'normal range'
    elif bmi >= 24.9 and bmi <= 29.9:
        return int(bmi), 'overweight'
    else:
        return int(bmi), 'obese'

if __name__ == '__main__':
    h = input("Enter your hight in meters\n")
    w = input("Enter your weight in kg\n")
    try:
        if isinstance(float(h), float) and isinstance(float(w), float):
            bmi, assessment = calculate_bmi(float(h), float(w))
            print("Your BMI is {}".format(bmi))
            print("Assessment : {}".format(assessment))
    except Exception as e:
        print("Input datatypes are not valid\nPlease enter correct values for hight and weight\n")
        print(str(e))

