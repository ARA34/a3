# a3.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Alex Reyes Aranda
# areyesar@uci.edu
# STUDENT ID
import ds_protocol as dsp
import ds_client as dsc
from ui import * # do not have to import Profile.py because its in ui.py



OPTIONS = "Hello Welcome to Journaling program.\nCreate or log into existing account(join).\n'Q' to quit.\n"

def main():
    usr_input = input(OPTIONS)
    n_profile = Profile(dsuserver=None,username=None,password=None)
    while usr_input != "Q":
        if usr_input == "join":
            username = input("Enter username:")
            password = input("Enter password: ")
            bio = input("Enter bio")
            n_profile.dsuserver = None # find this
            n_profile.username = username
            n_profile.password = password
            n_profile.bio = bio
            # fomart all the information recieved into a json string
            # send the information to the server
            # recieve a token
            #print(User created with token: {token})

        elif usr_input == "post":
            pass
        elif usr_input == "bio":
            pass

        usr_input = input(OPTIONS)



    


if __name__ == "__main__":
    main()