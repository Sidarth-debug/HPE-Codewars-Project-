import csv
import datetime

def pwd():
    # Bugged (idk what to do)
    usrname = input("Enter username: ")
    
    L = []
    with open("users.csv",'r') as users:
        users_reader = csv.reader(users)
        L = list(users_reader)
        new_pwd = input("Enter new password: ")
    
        



def crime(usrname):        
    STATUS = "No action taken"
    person = input("Enter name of person or the appearance of the person: ")
    location = input("Enter location of crime: ")
    time = input("Enter date and time of the crime: ")
    _crime = [usrname,person,location,time,STATUS]
    with open('crimes.csv', 'a') as crimes:
        crimes_writer = csv.writer(crimes)
        crimes_writer.writerow(_crime)

def complaints():
    STATUS = "No action taken"
    complaint = input("Enter complaint: ")
    _complaint = [complaint,STATUS]
    with open('complaints.csv', 'a') as complaints:
        complaints_writer = csv.writer(complaints)
        complaints_writer.writerow(_complaint)

def protest():
    STATUS = "Not approved"
    reason = input("Enter reason of protest: ")
    members = input("Enter number of members: ")
    date = input("Enter date of protest")
    start_time = input("Enter start time of protest: ")
    end_time = input("Enter end time of protest: ")
    disclaimer = input("Enter disclaimer message: ")
    _protest = [reason,members,date,start_time,end_time,disclaimer,STATUS]
    with open('protests.csv', 'a') as protests:
        protests_writer = csv.writer(protests)
        protests_writer.writerow(_protest)
        
def suggest():
    suggestion = input("Enter suggestion: ")
    d = datetime.date.now()
    date = d.date
    _suggestion = [suggestion,date]
    with open('suggestions.csv', 'a') as suggestions:
        suggestion_writer = csv.writer(suggestions)
        suggestion_writer.writerow(_suggestion)


def taxes(username):
    income = int(input("Enter income per annum in Rs: "))
    tax = 15/100 * income 
    _taxes = [username,tax]
    with open('taxes.csv', 'a') as taxes:
        taxes_writer = csv.writer(taxes)
        taxes_writer.writerow(_taxes)


