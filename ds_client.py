# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Alex Reyes Aranda
# areyesar@uci.edu
# STUDENT ID


import socket
from typing import Callable
import ds_protocol as dsp

HOST = ""
PORT = ""


def call(func: Callable, conn: dsp.connection, param: any):
  result = None
  try:
    result = func(conn, param)
  except Exception as ex:
    print(ex)
  return result

def connect_to_server(host:str, port:int) -> socket.socket:
  try:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    return sock
  except:
    return None
  
def create_json_str():
  


def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
  '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''
  sock = connect_to_server(server, port)

  _conn = dsp.init(sock)


  try:
    resp = input()
    while resp != "Q":
      if resp == "join":
        result = call(dsp.join, _conn, input("Add some input"))
        if result.protocol == dsp.DS_Protocol.JOIN:
          print("Success")
        else:
          print("Not Success, the protocol is: ", {result.protocol})

    sent = True
  except:

    sent = False


  #TODO: return either True or False depending on results of required operation
  return sent
