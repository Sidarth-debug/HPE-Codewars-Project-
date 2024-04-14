import csv
import pandas as pd

def checking():
    category = int(input("What would you like to check?\n1.Change status for crimes\n2.View suggestions\n3.Take decisions about protests\n4.Update or remove users\n5.Add users: "))


def add_user():
    user_type = input("Enter user type. (u for user, a for admin): ").lower()
    username = input("Enter user name: ")
    password = input("Enter password: ")
    user = [username,password,user_type]
    # Adding user to users.csv
    with open('users.csv','a') as user_csv:
        user_writer = csv.writer(user_csv)
        user_writer.writerow(user)
        user_csv.close()

def update_user():
    with open('users.csv','r') as user_csv:
        user_reader = csv.reader(user_csv)
        next(user_reader,None)
        c=0
        print(user_reader)
        for line in user_reader:
            print(line)

def view_suggestions():
    c=1
    with open('suggestions.csv','r') as suggestions:
        
        suggestions_reader = csv.reader(suggestions)
        next(suggestions_reader,None)
        for line in suggestions_reader:
            for suggestion in line:
                print(f"{c}. {suggestion}")
            c+=1

def crime_status():
    print("Crimes: ")
    with open('crimes.csv','r') as crimes:
        crimes_reader = csv.reader(crimes)
        next(crimes_reader,None)
        for line in crimes_reader:
            print(line)
        crimes.close()
    e = input("Would you like to change the status of a crime? y/n: ").lower()
    if e=='y':
        L=[]
        with open('crimes.csv','r') as crimes:
            crimes_reader = csv.reader(crimes)
            L = list(crimes_reader)
            #for line in players_reader:
            # L.append(line)
            c=0
            for i in range(1,len(L)+1):
                print(f"{i} \t : ",str(L[c]))
                c+=1
            print(L)
            row = int(input("Enter crime number to change status of: "))
            new = input("Enter new crime status: ")
            L[row][3] = new
            
        with open('crimes.csv','w+') as crimes:
            crimes_reader = csv.writer(crimes)
            for i in range(len(L)):
                crimes_reader.writerow(L[i])


                    


        
