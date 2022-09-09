from csv import *
from datetime import datetime
time = datetime.now()

def register():
    email = input("Please enter your eamil: ")
    password = input("Please enter your password: ")
    password2 = input("Please re-enter your password: ")
    if password == password2:
        info = [email,password]
        with open('accountdatabase.csv', 'a') as file:
            writer_object = writer(file)
            writer_object.writerow(info)
            file.close()
        info = [time, "register",email,password]
        with open('logs.csv', 'a') as file:
            writer_object = writer(file)
            writer_object.writerow(info)
            file.close()
        print("Your account is now registered")

def login():
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    info = [email,password]
    with open('accountdatabase.csv', 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if row == info:
                info = [time, "login",email,password]
                with open('logs.csv', 'a') as file:
                    writer_object = writer(file)
                    writer_object.writerow(info)
                    file.close()
                def actions():
                    print("What action do you want to perform?")
                    print("1. Put your option here!")
                    print("2. Log out")
                    print("3. Remove Account")
                    action = input("")
                    if action == "1":
                        print("Code that runs after someone selects this options here!")
                        actions()
                    elif action == "2":
                        print("Logging you out now")
                        input("Press ENTER to log out")
                        info = [time, "logout",email,password]
                        with open('logs.csv', 'a') as file:
                            writer_object = writer(file)
                            writer_object.writerow(info)
                            file.close()
                        quit()
                    elif action == "3":
                        info = [email,password]
                        with open("accountdatabase.csv", "r") as file:
                            lines = file.readlines()
                        with open("accountdatabase.csv", "w") as file:
                            for line in lines:
                                if line == info:
                                    file.write("")
                        print("Account Successfuly Deleted!")
                        input("Press ENTER to exit")
                        info = [time, "remove account",email,password]
                        with open('logs.csv', 'a') as file:
                            writer_object = writer(file)
                            writer_object.writerow(info)
                            file.close()
                        quit()
                    else:
                        print("There was an error when trying to perform that request please try again!")
                        actions()
                actions()
while True:
    option = input("Do you want to login or register? ")
    if option == "login":
        login()
    elif option == "register":
        register()
    else:print("Error please try again")