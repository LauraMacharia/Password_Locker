from user import User
from login import Login
import random

def create_user(fname, lname, phone, email, user, pasword):
    """
    Function to create a new user
    """
    new_user = User(fname, lname, phone, email, user, pasword)
    return new_user

def save_user(user):
    """
    Function to save new user
    """
    user.save_user()
    
def del_user(user):
    """
    Function to delete a user
    """
    user.delete_contact()
    
def find_user(number):
    """
    Function that helps find a user by number
    """
    return User.user_exist(number)

def display_user():
    """
    Function that displays all the saved users
    """
    return User.display_user()

def main():
    print("Hello welcome to pasword locker. What is your name?")
    user_name = input()
    
    print(f"Hello {user_name}. What would you like to do?")
    print('/n')
    
    while True:
        print("Use these short codes : nu - create a new user, du - display user, fu - find user, du - delete user ex - exit user")
        
        short_code input = ().lower()
        
        if short_code == "nu":
            print("New user")
            print("_"*10)
            
            print ("First name ...")
            f_name = input
            
             print("Last name ...")
            l_name = input()
            
            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()
            
            print("User name ...")
            user_name = input()
            
            print("pasword ...")
            pasword = input()
            
            save_user(create_user(f_name, l_name,p_number, e_address, user_name, pasword))
            

                           