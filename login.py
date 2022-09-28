import json
import pathlib
from login_page import password_generator as gpd

with open('user_info.json', 'r') as f:
    file = json.loads(f.read())

def get_path():
    path = pathlib.Path('user_info.json')
    path.touch(exist_ok=True)

    return path

def get_or_create_user_info():
    path = get_path()
    users = []
    with path.open(mode='r', encoding='utf-8') as file:
        try:
            users = json.load(file)
        except json.decoder.JSONDecodeError:
            pass

    return users

def save_user(user):
    path = get_path()

    users = get_or_create_user_info()
    users.append(user)

    with path.open(mode='w', encoding='utf-8') as file:
        json.dump(users, file, indent=2)

def create_user():
    print("Create account.")
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name')
    email_address = input("Enter your email address: ")
    username = input('Enter username: ')

    password = input("Enter your password: ")
    confirm_password = input("Confirm you password")

    while password.lower() != confirm_password.lower():
        print("Your password must match")
        password = input("Enter your password: ")
        confirm_password = input("Confirm you password")
        continue


    user = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email_address,
        'username': username,
        'password': password,
        'gdn': gpd.generate_password()
    }

    save_user(user)
    print(user['gdn'])
    return activate_account()

def activate_account():
    print("A one time password has been generated for you, use it to activate your account.")
    activate_acct = input("Enter activation account: ")
    print("Account Activated.")

    while activate_acct == ['gdn']:
        print("Activation code must match")
        activate_acct = input("Enter activation account: ")
        continue

    return login()

def login():

    print("You can now login.")
    log_username = input('Enter your user name: ')
    log_password = input('Enter your password: ')

    if log_username == log_username and log_password == log_password:
        print(f"Welcome {log_username}")
    else:
        print("Wrong credentials")
    return login()

print(create_user())
print(activate_account())
print(login())







# print(gpd.generate_password())
# def create_account():
#     print("Create account.")
#     first_name = input('Enter your first name: ')
#     last_name = input('Enter your last name')
#     email_address = input("Enter your email address: ")
#     username = input('Enter username: ')
#
#     password = input("Enter your password: ")
#     confirm_password = input("Confirm you password")
#
#     while password.lower() != confirm_password.lower():
#         print("Your password must match")
#         password = input("Enter your password: ")
#         confirm_password = input("Confirm you password")
#         continue
#     print()
#     print("Account Created successfully")
#     print("A One time password has been generated for you. use it to activate your account")
#     generated_pwd = []
#
#
#
#     user_info = {
#         'first_name': first_name,
#         'last_name': last_name,
#         'email': email_address,
#         'username': username,
#         'password': password,
#         'gdn': gpd.generate_password()
#     }
#
#     filename = 'user_info.json'
#     with open(filename, 'w') as f:
#         json.dump(user_info, f)
#         print()
#
#     activate_acct = input("Enter activation account: ")
#     while activate_acct == user_info['gdn'] :
#         print("Activation code must match")
#         activate_acct = input("Enter activation account: ")
#         continue
#
#
#     print("Account Activated ")
#     print("Enter your username and password to login")
#     log_username = input('Enter your user name: ')
#     log_password = input('Enter your password: ')
#
#     while log_username == user_info['username'] and log_password == user_info['password']:
#         print(f"Welcome {first_name} {last_name}")
#         if log_username != user_info['username'] and log_password != user_info['password']:
#             print("Wrong credentials")

# # create_account()