
# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Alex Reyes Aranda
# areyesar@uci.edu
# STUDENT ID

from __future__ import annotations
import json
from collections import namedtuple
import socket
import Profile
import time
import ds_client as dsc

class DSPServerError(Exception):
  pass

# the protocol for this project is just successfully parsing what you recieve from server

msg_info = namedtuple('msg_info', ['type','message','token'])

# Request commands:
JOIN = "join" # make account
BIO = "bio" # change bio
POST = "post" # make post

# Response commands:
ERROR = "error" # an error occured
OK = "ok" # Connection was success

    

def extract_json(json_msg:str) -> msg_info:
  '''
  Call the json.loads function on a json string and convert it to a DataTuple object
  
  TODO: replace the pseudo placeholder keys with actual DSP protocol keys
  Input: json_string
  Output: namedtuple with parts of json string

  Process:
  1. converts json_string(str) into json_obj(dictionary)
  2. 

  {"response": {"type": "ok", "message": "Welcome to the ICS 32 Distributed Social!", "token": "2a07b9b4-3016-485d-833c-66e895f98ba9"}}
  {"response":{"type":"ok","entry":"Post Published to DS server"}}
  '''

  try:
    json_obj = json.loads(json_msg)
    vals = list(json_obj["response"].values())
    type = json_obj["response"]["type"]
    message = json_obj["response"]["message"]
    msg_info_1 = msg_info(type, message, "")
    if len(vals) == 3:
      token = json_obj["response"]["token"]
      msg_info_1 = msg_info(type, message, token)

  except json.JSONDecodeError:
    print("Json cannot be decoded.")
  return msg_info_1


def join(server:str, port:int, username:str, password:str, token=""):
  return dsc.send(server=server, port=port, username=username, password=password, message="",bio=None)

  

def post(server:str, port:int, username:str, password:str, message:str):
  message = message.strip()
  if message != "":
    print(f"Your message [{message}] was posted")
    return dsc.send(server=server,port=port,username=username,password=password,message=message)
  else:
    print("You cannot post empty or whitespace only posts. Please Try again.")
    return False



def bio(server:str, port:int, username:str, password:str, bio:str):
  bio = bio.strip()
  if bio != "":
    print(f"Your bio was changed to [{bio}]")
    return dsc.send(server=server, port=port, username=username, password=password,message="",bio=bio)
  else:
    print("You cannot have an empty or only whitespace bio. Please try again.")
    return dsc.send(server=server, port=port, username=username, password=password, message="", bio=bio)


