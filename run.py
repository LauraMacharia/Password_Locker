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
        
        short_code = input().lower()
        
        if short_code == "nu":
            while True:
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
                
                print('/n')
                print(f"New User {f_name} {l_name} created")
                print ('/n')
                
        elif  short_code == 'du':
            if display_user():
                print("Here is a list of all the users")
                print ('/n')
                for user in display_user():
                        
                        print(f"{user.f_name} {user.l_name} .....{user.p_number}")
                        
                        print('/n')
                else:
                    print('/n')
                    print("you do not have any user saved yet")
                    
        elif short_code == 'fu':
                print("Enter the phone number you want to search for")
                search_number = input()
                if check_existing _user(search_number):
                    search_user = find_user(search_number)
                    print(f"{search_user.f_name} {search_user.l_name}")
                    print("_"*20)
                    print(f"Phone number .....{search_user.p_number}")
                    
                    print(f"Email address .....{search_user.email}")
                
                    print(f"Username .....{search_user.username}")
                    
                    print(f"Pasword .....{search_user.pasword}")
                    
                else:
                    print("The user does not exist")
                    
        elif short_code == 'ex':
                print("Bye .....")
                break
            else:
                print("I really dont get that.U se short codes")   } 
                        


if __name__ == '__main__':
     main()