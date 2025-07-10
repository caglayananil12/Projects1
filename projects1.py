calculationNumber = int(input("How many transactions do you want to make = "))
def calculator():
    for i in range(calculationNumber):
        transaction = int(input("Enter a transaction <<< 0 = summation \n1 = subtraction\n2 = multiplication\n3 = division\n4 = exponentiation\n5 = exit >>> = "))
        number1 = int(input("Enter an integer number = "))
        number2 = int(input("Enter another integer number = "))
        if transaction == 5:
            print("<<<<<<<< EXIT >>>>>>>>")
            break
        if transaction == 0:
            print(number1, "+", number2, "=", number1 + number2)
        elif transaction == 1:
            print(number1, "-", number2, "=", number1 - number2)
        elif transaction == 2:
            print(number1, "*", number2, "=", number1 * number2)
        elif transaction == 3:
            if number2 != 0:
                print(number1, "/", number2, "=", number1 / number2)
            else:
                print("Number2 should not bezero.")
        elif transaction == 4:
            print(number1, "**", number2, "=", number1 ** number2, "(number1 to the power of number2)")
        else:
            print("Invalid transaction. Please give a transaction number between 0 to 5.")
calculator()
    