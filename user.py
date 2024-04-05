import csv

def pwd():
    usrname = input("Enter username: ")
    new_pwd = ""
    with open("users.csv",'r') as users_csv:
        users_reader = csv.DictReader(users_csv)
        for line in users_reader:
            if usrname==line[0][1]:
                new_pwd = input("Enter new password: ")
                line[0][1] = new_pwd

def crime():
    STATUS = "No action taken"
    person = input("Enter name of person or the appearance of the person: ")
    location = input("Enter location of crime: ")
    time = input("Enter date and time of the crime: ")
    _crime = [person,location,time,STATUS]
    with open('crimes.csv', 'w') as crimes:
        crimes_writer = csv.writer(crimes)
        crimes_writer.writerow(_crime)

def complaints():
    STATUS = "No action taken"
    complaint = input("Enter complaint: ")
    _complaint = [complaint,STATUS]
    with open('complaints.csv', 'w') as complaints:
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
    with open('protests.csv', 'w') as protests:
        protests_writer = csv.writer(protests)
        protests_writer.writerow(_protest)
        


