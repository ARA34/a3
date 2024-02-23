# a3.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Alex Reyes Aranda
# areyesar@uci.edu
# STUDENT ID
import ds_protocol as dsp
import ds_client as dsc
from ui import * # do not have to import Profile.py because its in ui.py


def main():
    server = "168.235.86.101"
    port = 3021
    dsc.send(server, port, "nsndadasnjkadn", "1234","")



if __name__ == "__main__":
    main()