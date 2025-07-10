realUsername = input("Determine your username: ")
realPassword = input("Detrmine your password: ")

if 5 < len(realPassword) < 10:
    print("Succesfull determinations:)")
    count = 0
    limitation = 3

    while count < limitation:
        username = input("Enter your username: ")
        password = input("Enter your pasword: ")
        
        if username == realUsername and password == realPassword:
            print("Welcome your page;)")
            break
        else:
            count+=1
    print("Wait one minutes")
else:
    print("Password should contain between 5 to 10 characters.")      
        
    