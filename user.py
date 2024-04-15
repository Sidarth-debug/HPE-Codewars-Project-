import csv

def change_pwd():
    usrname = input("Enter username: ")
    users_data = []
    
    with open('users.csv','r') as users:
        user_valid = False
        users_reader = csv.reader(users)
        users_data = list(users_reader)
        for user in users_data:
            if user[0] == usrname:
                new_pwd = input("Enter new password: ")
                user[1] = new_pwd
                user_valid = True
        if user_valid == False:
            print("Invalid username")
        with open('users.csv','w+') as users:
            users_reader = csv.writer(users)
            for i in range(len(users_data)):
                users_reader.writerow(users_data[i])


def crime(usrname): 
    choice = int(input("1.View the status of your reported crimes\n2.Submit crime: "))
    if choice==2:

        STATUS = "No action taken"
        person = input("Enter name of person or the appearance of the person: ")
        location = input("Enter location of crime: ")
        time = input("Enter date and time of the crime: ")
        accusation = input("Enter accusation: ")
        _crime = [usrname,person,location,time,accusation,STATUS]
        with open('crimes.csv', 'a') as crimes:
            crimes_writer = csv.writer(crimes)
            crimes_writer.writerow(_crime)
    else:
        crimes_data = []
        is_valid = False
        with open('crimes.csv','r') as crimes:
            crimes_reader = csv.reader(crimes)
            crimes_data = list(crimes_reader)
            for crime in crimes_data:
                if crime[0] == usrname:
                    print(crime[2],crime[3],crime[4])
                    is_valid = True
            if is_valid==False:
                print("No crime reports found")

def complaints(usrname):
    choice = int(input("1.View the status of your reported complaints\n2.Submit complaint: "))
    if choice==2:
        STATUS = "No action taken"
        complaint = input("Enter complaint: ")
        _complaint = [complaint,STATUS]
        with open('complaints.csv', 'a') as complaints:
            complaints_writer = csv.writer(complaints)
            complaints_writer.writerow(_complaint)
    else:
        complaints_data = []
        is_valid = False
        with open('complaints.csv','r') as complaints:
            complaints_reader = csv.reader(complaints)
            complaints_data = list(complaints_reader)
            for complaint in complaints_data:
                if complaint[0] == usrname:
                    print(complaint[1],complaint[2])    
                    is_valid = True
        if is_valid == False:
            print("No complaints submitted")  

def protest(usrname):
    choice = int(input("1.View the status of your requested protests\n2.Submit protest request: "))
    if choice==2:
        STATUS = "Not approved"
        reason = input("Enter reason of protest: ")
        members = input("Enter number of members: ")
        date = input("Enter date of protest: ")
        start_time = input("Enter start time of protest: ")
        end_time = input("Enter end time of protest: ")
        disclaimer = input("Enter disclaimer message: ")
        _protest = [reason,members,date,start_time,end_time,disclaimer,STATUS]
        with open('protests.csv', 'a') as protests:
            protests_writer = csv.writer(protests)
            protests_writer.writerow(_protest)
    else:
        protests_data = []
        is_valid = False
        with open('protests.csv','r') as protests:
            protests_reader = csv.reader(protests)
            protests_data = list(protests_reader)
            for protest in protests_data:
                if protest[0] == usrname:
                    print(protest[1],protest[2]) 
                    is_valid = True
            if is_valid == False:
                print("No protest requests submitted")       
        
def suggest(usrname):
    choice = int(input("1.View your suggestions\n2.Submit suggestion: "))
    if choice==2:
            
        suggestion = input("Enter suggestion: ")
        
        _suggestion = [usrname,suggestion]
        with open('suggestions.csv', 'a') as suggestions:
            suggestion_writer = csv.writer(suggestions)
            suggestion_writer.writerow(_suggestion)
    else:
        suggestions_data = []
        is_valid = False
        with open('suggestions.csv','r') as suggestions:
            suggestions_reader = csv.reader(suggestions)
            suggestions_data = list(suggestions_reader)
            for suggest in suggestions_data:
                if suggest[0] == usrname:
                    print(suggest[1])
                    is_valid = True
            if is_valid == False:
                print("No suggestions submitted")

'''def taxes(username):
    income = int(input("Enter income per annum in Rs: "))
    tax = 15/100 * income 
    _taxes = [username,tax]
    with open('taxes.csv', 'a') as taxes:
        taxes_writer = csv.writer(taxes)
        taxes_writer.writerow(_taxes)'''


