# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Alex Reyes Aranda
# areyesar@uci.edu
# STUDENT ID


import socket
import ds_protocol as dsp
from ui import *


def send(server:str, port:int, username:str, password:str, message:str, bio:str=None): # equivalent of run() function
  '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''
  join_msg = {"join": {"username": username,"password": password, "token":""}}
  join_msg = json.dumps(join_msg)

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
      client.connect((server, port))
     
      send = client.makefile("w")
      recv = client.makefile("r")

      send.write(join_msg + "\r\n")
      send.flush()
      resp = recv.readline()
      print(resp)

      parsed_resp = dsp.extract_json(resp)
      p_type = parsed_resp.type
      p_message = parsed_resp.message
      p_token = parsed_resp.token

      









OPTIONS1 = "Hello Welcome to Journaling program.\nCreate or log into existing account(join).\n'Q' to quit.\n"
OPTIONS2 = "Now that you've created an account or logged in.\nWould you like to post(post) or change bio(bio)?\n'Q' to quit."

def run():
  usr_input = input(OPTIONS1)
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
          n_profile.save_profile() # missing path for saving

          join_msg = "{'join': {'username':" + str(n_profile.username) + ",'password':"+ str(n_profile.password) + ", 'token':''" + "}" + "}"

          # fomart all the information recieved into a json string(join_msg)
          send(dsu_server=None, username = n_profile.username, password= n_profile.password, message="")

          # send the information to the server
          # recieve a token
          #print(User created with token: {token})

          # now ask if they want to post or change bio
          
          usr_input_2 = input(OPTIONS2)
          information = {}
          while usr_input_2 != "Q":
              if usr_input_2 == "post":
                  post = input("What would you like to post:\n")
              elif usr_input_2 == "bio":
                  new_bio = input("New bio: \n")
                  n_profile.bio = new_bio
              else:
                  print("ERROR: Inner loop.")
              out = send(dsu_server=None, username=n_profile.username, password = n_profile.password, message = None, bio = n_profile.bio)
              usr_input_2 = input(OPTIONS2)

      else:
          print("ERROR: Outer loop.")
      out = send(dsu_server=None, username=n_profile.username, password = n_profile.password, message = None, bio = n_profile.bio)
      out = dsp.extract_json(out)

      usr_input = input(OPTIONS1)
