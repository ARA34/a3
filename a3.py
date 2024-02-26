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
import sys

#Would you like to go online or offline? ->

USERNAME = "melonmusk"
PASSWORD = "XA123"
BIO = ""
# C /Users/alexra/Documents/UCI_WINTER_2023/ICS_32/test_folder -n myjournal

SERVER = "168.235.86.101"
PORT = 3021
CURRENT_FOLDER = Path(".").resolve()

OFFLINE_ONLINE = "Hello Welcome to my Journaling program.\nWould you like to continue offline(offline) or online(online)?\n"
OPTIONS1 = "Hello Welcome to Journaling program.\nCreate or log into existing account(join).\n'Q' to quit.\n"
OPTIONS2 = "Now that you've created an account or logged in.\nWould you like to post(-post) or change bio(-bio) or both?\n'Q' to quit.\n"

def convert_online():
    usr_input = input("Would you like to make this information public online(yes or no).\nSaying yes will make everything you type in public:\n").lower()
    while usr_input != ("no" and "yes"):
        print("Incorrect input")
        usr_input = input("Would you like to make this information public online(yes or no):").lower()
    return str(usr_input)


def print_profile(n_profile:Profile):
    print("dsuserver" + n_profile.dsuserver)
    print("username" + n_profile.username)
    print("password" + n_profile.password)
    print("bio" + n_profile.bio)

def main():

    input_1 = print_user_options() # outer user input
    p_input_1 = parse_inputs(input_1)
    command_input = p_input_1[0]

    user_profile = Profile(dsuserver=None, username=None, password=None)
    profile_loaded_online = False

    while command_input != "Q":
        if command_input == "C":
            directory_input = p_input_1[1]
            directory_input = Path(directory_input)
            subs, extra = p_input_1[2:]
            command_c = command_C(directory_input, subs, extra)


            user_profile.username = command_c[1]
            user_profile.password = command_c[2]
            user_profile.bio = command_c[3]
            user_profile.dsuserver = command_c[4] # asking for dsu_server
            print("Reminder: Everything you type is currently local")

            online_question = convert_online()
            if online_question == "yes":
                profile_loaded_online = True
                print("Reminder: Your profile, bio, and posts will now be public")

            input_2 = print_user_options_2() # nested user input
            p_input_2 = parse_inputs(input_2) # this a list of parsed input
            command_input_2 = p_input_2[0]
            tup_list = p_input_2[2]

            if profile_loaded_online:
                allows = ["-addpost", "-bio"]
                valid_tups = list(filter(lambda d:d[0] in allows, tup_list))

            if command_input_2 == "E":
                # E edits username, password, and bio
                directory_input = str(directory_input)
                directory_input += "/" + extra + ".dsu"
                directory_input = Path(directory_input)
                editDSU(tup_list, directory_input, user_profile)

                # online publishing aspect
                if profile_loaded_online:
                    dsp.join(server=user_profile.dsuserver, port=PORT, username=user_profile.username, password=user_profile.password) # creates account
                    dsp.bio(server=user_profile.dsuserver, port=PORT, username=user_profile.username, password=user_profile.password,bio=user_profile.bio) # changes bio

                    if len(valid_tups) >= 1:
                        for tup in valid_tups:
                            # ("-addpost","helloworld")
                            run_options(user_profile, tup, PORT) # published bio and posts
                    else:
                        print("There is nothing to publish online")
            elif command_input_2 == "P":  
                print(command_P(tup_list, user_profile))
            else:
                print("There is no profile loaded. Run commands 'C' or 'O.'")


        elif command_input == "O":
            try:
                directory_input = p_input_1[1]
                directory_input = Path(directory_input)
                user_profile = loadDSU(directory_input) # command_O
                print("Reminder: Everything you type is currently local")
            except:
                raise DsuProfileError
            
            
            online_question = convert_online()
            if online_question == "yes":
                profile_loaded_online = True
                print("Reminder: Your profile, bio, and posts will now be public")

            input_2 = print_user_options_2()
            p_input_2 = parse_inputs(input_2)
            command_input_2 = p_input_2[0]
            tup_list = p_input_2[2] # outside

            if profile_loaded_online:
                allows = ["-addpost", "-bio"]
                valid_tups = list(filter(lambda d:d[0] in allows, tup_list))

            if command_input_2 == "E":
                editDSU(tup_list, directory_input, user_profile)
                
                # online publishing aspect
                if profile_loaded_online:
                    dsp.join(server=user_profile.dsuserver, port=PORT, username=user_profile.username, password=user_profile.password) # creates account
                    dsp.bio(server=user_profile.dsuserver, port=PORT, username=user_profile.username, password=user_profile.password,bio=user_profile.bio) # changes bio

                    if len(valid_tups) >= 1:
                        for tup in valid_tups:
                            # ("-addpost","helloworld")
                            run_options(user_profile, tup, PORT) # published bio and posts
                    else:
                        print("There is nothing to publish online")
            elif command_input_2 == "P":
                print(command_P(tup_list, user_profile))
            else:
                print("There is not profile loaded. Run commands 'C' or 'O.'")
        input_1 = print_user_options()
        p_input_1 = parse_inputs(input_1)

if __name__ == "__main__":
    main()