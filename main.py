import csv
import pandas as pd
from admin import add_user,update_user,protest_approval,view_suggestions,remove_user,crime_status
from user import change_pwd,crime,complaints,protest,suggest

# TODO : Only login
is_valid_login = False
username = ""
password = ""
user_type = ""
while is_valid_login == False: 
    usr = input("Enter username: ")
    pwd = input("Enter password: ")
    with open('users.csv','r') as users:
        valid_user = False
        users_reader = csv.reader(users)
        users_data = list(users_reader)
        for user in users_data:
            if user[0] == usr and user[1] == pwd:
                valid_user = True
                username=usr
                password=pwd
                user_type = user[2]
                is_valid_login = True
        if valid_user == False:
            print("Incorrect username or password. Please try again")
if user_type=="admin":
    while True:
        print("What would you like to do?")
        admin_choice = int(input("1.Update the status of crime reports\n2.Update the status for protest requests\n3.View suggestions\n4.Add users\n5.Update users\n6.Remove users: "))
        if admin_choice == 1:
            crime_status()
        elif admin_choice == 2:
            protest_approval()
        elif admin_choice == 3:
            view_suggestions()
        elif admin_choice == 4:
            add_user()
        elif admin_choice == 5:
            update_user()
        elif admin_choice == 6:
            remove_user()
        else:
            print("Invalid input")
        continue_usage = input("Would you like to continue using the program? y/n: ")
        if continue_usage == 'n':
            break
else:
    while True:
        print("What would you like to do?")
        user_choice = int(input("1.Change your password\n2.Report a crime/View the status of reported crimes\n3.Submit a protest request/View the status of your protest requests\n4.Submit a complaint/View the status of your complaints\n5.Submit a suggestion/View your suggestions: "))
        if user_choice == 1:
            change_pwd()
        elif user_choice == 2:
            crime(username)
        elif user_choice == 3:
            protest(username)
        elif user_choice == 4:
            complaints(username)
        elif user_choice == 5:
            suggest(username)
        else:
            print("Invalid input")
        continue_usage = input("Would you like to continue using the program? y/n: ")
        if continue_usage == 'n':
            break      



