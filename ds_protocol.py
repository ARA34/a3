
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


# exp--protocol


class DSPProtocol:
  ERROR = "error"
  OK = "ok"

  JOIN = "join" # make account
  BIO = "bio" # change bio
  POST = "post" # make post
  
  def __init__(self, protocol=None, data=None) -> None:
    self.protocol = protocol
    self.data = data
  
  def format(dsp:DSPProtocol) -> str:
    """
    Takes a DSP object and formats it into a string
    """
    return f"{dsp.protocol}|{dsp.data}"
  
  def open(cmd:str) -> DSPProtocol:
    """
    Takes a string and converts to a DSP object if applicable
    """

    parts = cmd.split("|")
    if len(parts) > 1:
      return DSPProtocol(parts[0],parts[1])
    else:
      # not applicable
      return DSPProtocol(DSPProtocol.ERROR) # returns dsp error object
    


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
  '''
  try:
    json_obj = json.loads(json_msg)
    type = json_obj["response"]["type"]
    message = json_obj["response"]["message"]
    token = json_obj["response"]["token"]

  except json.JSONDecodeError:
    print("Json cannot be decoded.")
  return msg_info(type, message, token)


def join(server:str, port:int, username:str, password:str, token=""):
  dsc.send(server=server, port=port, username=username, password=password, message="",bio=None)
  print("Logged in!")

  

def post(server:str, port:int, username:str, password:str, message:str):
  message = message.strip()
  if message != "":
    dsc.send(server=server,port=port,username=username,password=password,message=message)
    print(f"Your message [{message}] was posted")
  else:
    print("You cannot post empty or whitespace only posts. Please Try again.")



def bio(server:str, port:int, username:str, password:str, bio:str):
  bio = bio.strip()
  if bio != "":
    dsc.send(server=server, port=port, username=username, password=password,message="",bio=bio)
    print(f"Your bio was changed to [{bio}]")
  else:
    print("You cannot have an empty or only whitespace bio. Please try again.")


