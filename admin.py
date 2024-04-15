import csv
import pandas as pd

def add_user():
    type = ""
    user_type = input("Enter user type. (u for user, a for admin): ").lower()
    if user_type == 'u':
        type = "user"
    else:
        type = "admin"
    username = input("Enter user name: ")
    password = input("Enter password: ")
    user = [username,password,user_type]
    # Adding user to users.csv
    with open('users.csv','a') as user_csv:
        user_writer = csv.writer(user_csv)
        user_writer.writerow(user)
        user_csv.close()

def update_user():
    c1=0
    c=0
    with open('users.csv','r') as users:
        
        users_reader = csv.reader(users)
        

        for line in users_reader:
            if c1!=0:
                print(f"{c}.",end="")
            for user in line:
                if c1==0:
                    print(f"\t{user}",end="")
                    c1=1
                    
                else:
                    print(f" {user}",end="")
            c+=1
            print()
    
    
    L=[]
    with open('users.csv','r') as users:
        users_reader = csv.reader(users)
        L = list(users_reader)
            #for line in players_reader:
            # L.append(line)
            
        row = int(input("Enter user number to change type of: "))
        new = input("Enter new type (user/admin): ")
        L[row][2] = new
            
    with open('users.csv','w+') as users:
        users_reader = csv.writer(users)
        for i in range(len(L)):
            users_reader.writerow(L[i])   


def crime_status():
    print("Crimes: ")
    c1=0
    c=0
    with open('crimes.csv','r') as crimes:
        
        crimes_reader = csv.reader(crimes)
        

        for line in crimes_reader:
            if c1!=0:
                print(f"{c}.",end="")
            for crime in line:
                if c1==0:
                    print(f"\t{crime}",end="")
                    c1=1
                    
                else:
                    print(f" {crime}",end="")
            c+=1
            print()
    e = input("Would you like to change the status of a crime? y/n: ").lower()
    if e=='y':
        L=[]
        with open('crimes.csv','r') as crimes:
            crimes_reader = csv.reader(crimes)
            L = list(crimes_reader)
            #for line in players_reader:
            # L.append(line)
            
            row = int(input("Enter crime number to change status of: "))
            new = input("Enter new crime status: ")
            L[row][-1] = new
            
        with open('crimes.csv','w+') as crimes:
            crimes_reader = csv.writer(crimes)
            for i in range(len(L)):
                crimes_reader.writerow(L[i])

def protest_approval():
    c1=0
    c=0
    with open('protests.csv','r') as protests:
        
        protests_reader = csv.reader(protests)
        

        for line in protests_reader:
            if c1!=0:
                print(f"{c}.",end="")
            for protest in line:
                if c1==0:
                    print(f"\t{protest}",end="")
                    c1=1
                    
                else:
                    print(f" {protest}",end="")
            c+=1
            print()
    e = input("Would you like to change the status of a protest? y/n: ").lower()
    if e=='y':
        L=[]
        with open('protests.csv','r') as protests:
            protests_reader = csv.reader(protests)
            L = list(protests_reader)
            #for line in players_reader:
            # L.append(line)
            
            row = int(input("Enter protest number to change status of: "))
            new = input("Enter new protest status: ")
            L[row][-1] = new
            
        with open('protests.csv','w+') as protests:
            protests_reader = csv.writer(protests)
            for i in range(len(L)):
                protests_reader.writerow(L[i])

def view_suggestions():
    c=1
    with open('suggestions.csv','r') as suggestions:
        
        suggestions_reader = csv.reader(suggestions)
        next(suggestions_reader,None)
        for line in suggestions_reader:
            print(f"{c}.",end="")
            print(line[1])
            c+=1
                    
def remove_user():
    c1=0
    c=0
    with open('users.csv','r') as users:
        
        users_reader = csv.reader(users)
        

        for line in users_reader:
            if c1!=0:
                print(f"{c}.",end="")
            for user in line:
                if c1==0:
                    print(f"\t{user}",end="")
                    c1=1
                    
                else:
                    print(f" {user}",end="")
            c+=1
            print()
    user = input("Enter username of user to be removed: ")
    df = pd.read_csv('users.csv',index_col='username')
    df = df.drop(user)
    df.to_csv('users.csv')
        
