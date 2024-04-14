import csv
import datetime
import pandas as pd
# TODO : Only login 
'''def update_user():
    with open('users.csv','r') as user_csv:
        user_reader = csv.reader(user_csv)
        L=[]
        c=0

        
        while c==0:
            for line in user_reader:
                for item in line:
                    print(f"\t{item}",end='')
                    c+=1
                break   
            print()
        
        c=1
        for line in user_reader:
            print(f"{c}\t",end="")
            for item in line:
                print(item,end="\t")
            print()
            c+=1
    
        
        
        L = list(user_reader)
            #for line in players_reader:
            # L.append(line)
        c1=0
        for i in range(1,len(L)+1):
            print(f"{i} \t : ",str(L[c1]))
            c1+=1
        print(L)
        row = int(input("Enter user number to change type of: "))
        new = input("Enter new type: ")
        L[row][2] = new  
        with open('users.csv','w+') as users:
            users_reader = csv.writer(users)
            for i in range(len(L)):
                users_reader.writerow(L[i])      
            
update_user()'''


