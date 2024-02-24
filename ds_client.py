# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Alex Reyes Aranda
# areyesar@uci.edu
# STUDENT ID


import socket
import ds_protocol as dsp
from ui import *
import time
from typing import Callable
from collections import namedtuple


Connection = namedtuple("Connection",["socket","send","recv"])

def init(sock:socket) -> Connection:
  try:
    f_send = sock.makefile("w")
    f_recv = sock.makefile("r")
  except:
    raise dsp.DSPServerError
  return Connection(
    socket = sock,
    send = f_send,
    recv = f_recv
  )

def write_command(_conn: Connection, cmd:str):
    try:
        _conn.send.write(cmd + "\r\n")
        _conn.send.flush()
    except:
        raise dsp.DSPServerError
    
def read_command(_conn: Connection) -> str:
    cmd = _conn.recv.readline()
    return cmd


def connect_to_server(host:str, port:int) ->socket.socket:
    try:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.connect((host,port))
      return sock
    except:
        return None

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
  try:

    sock = connect_to_server(server,port)
    if sock ==None:
        print("couldn't connect to server")
        return
    _conn = init(sock)


    json_msg = ""
    usr_token = get_token(_conn, username, password)
    if (username and password !="") and (message == ""): # joining
        json_msg = {"join": {"username": username,"password": password, "token":""}}
    elif message != "" and bio == None:
        json_msg = {"token":usr_token,"post":{"entry":message, "timestamp":str(time.time())}}
        # json_msg = dsp.post(message)
        # msg_type = dsp.POST
    elif message == "" and bio != "":
        # json_msg = dsp.bio(bio)
        # msg_type = dsp.BIO
        json_msg = {"token":usr_token, "bio":{"entry":bio,"timestamp":str(time.time())}}
    else:
        print("something went wrong when assigning json_msg")

    json_msg = json.dumps(json_msg)
    write_command(_conn, json_msg)
    response = read_command(_conn)
    print(response)
    # return True
    return True
  





  #TODO: return either True or False depending on results of required operation
  # join_msg = {"join": {"username": username,"password": password, "token":""}}
  # join_msg = json.dumps(join_msg)

  # post_msg = {"token":"","post":{"entry":message, "timestamp":""}}
  # post_msg = json.dumps(post_msg)

  # bio_msg = {"token":"", "bio":{"entry":"","timestamp":""}}
  # bio_msg = json.dumps(bio_msg)



  # json_msg = ""
  # msg_type = ""

  # if (username and password !="") and (message and bio == ""):
  #     json_msg = dsp.join(username, password)
  #     msg_type = dsp.JOIN
  # elif message != "" and bio == "":
  #     json_msg = dsp.post(message)
  #     msg_type = dsp.POST
  # elif message == "" and bio != "":
  #     json_msg = dsp.bio(bio)
  #     msg_type = dsp.BIO
  # else:
  #     print("something went wrong when assigning json_msg")
  
  # try:
  #     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
  #       client.connect((server, port))
  #       send = client.makefile("w")
  #       recv = client.makefile("r")

  #       send.write(json_msg + "\r\n") # json_msg is assigned above
  #       send.flush()
  #       resp = recv.readline()


  #       print(resp) # printing the response(only error and ok formats)

  #       parsed_resp = dsp.extract_json(resp)
  #       p_type = parsed_resp.type
  #       p_message = parsed_resp.message
  #       p_token = parsed_resp.token

  #       if p_type == dsp.OK:
  #           # no error
  #           # load the profile that has corresponding username and password
  #           # save the token in the profile somehow might be wrong
            
  #           # at this point, the user's token is already loaded
  #           pass

  #       elif p_type == dsp.ERROR:
  #           print("Error Message: " + p_message)

    # return True  # twas successful

  except:
      return False # twas not successful


def get_token(_conn:Connection, username:str, password:str) -> str:
    join_msg = {"join": {"username": username,"password": password, "token":""}}
    join_msg = json.dumps(join_msg)
    write_command(_conn,join_msg)
    resp = read_command(_conn)
    parsed_resp = dsp.extract_json(resp)
    return str(parsed_resp.token)

   
    
    


