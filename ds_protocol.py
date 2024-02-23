
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

# the protocol for this project is just successfully parsing what you recieve from server

msg_info = namedtuple('msg_info', ['type','message','token'])

# Request commands:
JOIN = "join" # make account
BIO = "bio" # change bio
POST = "post" # make post

# Response commands:
ERROR = 0 # an error occured
OK = 1 # Connection was success


def extract_json(json_msg:str) -> msg_info: # Connection is a namedtuple
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


  