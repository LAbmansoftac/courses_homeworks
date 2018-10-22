import random

#Here we create a list with logins, passwords, random numbers.

login = ['Ivanov', 'Petrov', 'Aseniv', 'korsunov', 'ptashka', 'king23', 'queen231', 'prince231', 'princes3232', 'servialance']
password = ['fdae21', 'fdae22', 'fdae23', 'fdae24', 'fdae25', 'fdae26', 'fdae27', 'fdae28', 'fdae29', 'fdae30']
n = len(password)
rand_numb = random.sample(range(999), n)

#Creating 2 dictionaries

users_data_dict = dict(zip(login, password))
pass_and_numb = dict(zip(password, rand_numb))

#Prints of the users data

print('Dictionary with logins and passwords: \n', users_data_dict)
print("A dictionary with passwords and random numbers: \n", str(pass_and_numb))

#Checking login and password

login_input = input('Enter your login: ')

if login_input in users_data_dict:
    password_input = input('Please, enter your password: ')
    if password_input in pass_and_numb:
        print('All the data is correct. Your random number is ', pass_and_numb[password_input])
    else:
        print('Sorry man, your password is wrong. Try to do it again!')
else:
    print('Your login ' + str(login_input) + ' was not found. \nSo we registered a new login for you with the name you provided above')
    new_pass_input = input('Please enter your password: ')
    login.append(login_input)
    password.append(new_pass_input)
    users_data_dict = dict(zip(login, password))
    pass_and_numb = dict(zip(password, rand_numb))

    print(str(users_data_dict) + '\n' + str(pass_and_numb))



"""

rand_numb = [randint(0, 999) for p in range(0, 9)]

log_pass = dict(zip(login, password))

print(log_pass)
"""
