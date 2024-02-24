# a3.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Alex Reyes Aranda
# areyesar@uci.edu
# STUDENT ID
import ds_protocol as dsp
import ds_client as dsc
from ui import * # do not have to import Profile.py because its in ui.py
from pathlib import Path



def main():
    OPTIONS1 = "Hello Welcome to Journaling program.\nCreate or log into existing account(join).\n'Q' to quit.\n"
    OPTIONS2 = "Now that you've created an account or logged in.\nWould you like to post(post) or change bio(bio)?\n'Q' to quit."
    currfolder = Path(".").resolve()

    server = "168.235.86.101"
    port = 3021
    dsc.send(server, port, "nsndadasnjkadn", "1234","")




    # creating an account twice doesnt do anything different, just returns token

    # usr_input = input(OPTIONS1)
    # n_profile = Profile(dsuserver=None, username=None, password=None)
    # while usr_input != "Q":
    #     if usr_input == "join": # joins a user or loads a user
    #         username = input("Enter username:")
    #         password = input("Enter password:")
    #         bio = input("Enter bio:")
    #         n_profile.dsuserver = server
    #         n_profile.username = username
    #         n_profile.password = password
    #         n_profile.bio = bio

    #         userfile = str(currfolder) + username
    #         userpath = Path(userfile)
    #         try:
    #             n_profile.save_profile(userpath)
    #         except DsuFileError:
    #             print("There was an error saving user profile to a file")

    #         dsc.send(server=n_profile.dsuserver, port=port, username=n_profile.username, password=n_profile.password) # creates an account




        





if __name__ == "__main__":
    main()