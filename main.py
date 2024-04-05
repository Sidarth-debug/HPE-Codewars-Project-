import csv
admin_pwd = 'qwerty'
user_type = input("Enter user type. (u for user, a for admin): ").lower()
username = input("Enter user name: ")
password = input("Enter password: ")
if user_type == 'a':
    app_pwd = input("Enter admin password: ")
    if app_pwd == admin_pwd:
        user_type = 'admin'
    else:
        user_type = 'user'
user = [username,password,user_type]
# Adding user to users.csv
with open('users.csv','a') as user_csv:
    user_writer = csv.writer(user_csv)
    user_writer.writerow(user)
    user_csv.close()


