try:
    year = 2025
    def calculator():
        while True:
            birth_year = int(input("Enter your birth year: "))
            ages = year - birth_year
            if ages < 18:
                print("below 18 years old")
                break
            else:
                print(ages)
                    
    calculator()
    
except ValueError:
    print("please give only year")


