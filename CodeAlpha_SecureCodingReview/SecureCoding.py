username = input("Enter Username: ")
password = input("Enter Password: ")

if len(username) < 3:
    print("Invalid Username")

elif len(password) < 6:
    print("Password must be at least 6 characters")

elif username == "admin" and password == "1234hs":
    print("Login Successful")

else:
    print("Login Failed")