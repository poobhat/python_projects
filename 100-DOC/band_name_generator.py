def generate_band_name(*args):
    band_list = []
    for each in args:
        band_list.append(each+' ')
    return " ".join(band_list)

if __name__ == '__main__':
    print("Let us generate a cool band name\n")
    city = input("Where are you from?\n")
    name = input("What is your pet's name?\n")
    print("Here is a band name suggestion - \n")
    print(generate_band_name(city, name))