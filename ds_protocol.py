# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Alex Reyes Aranda
# areyesar@uci.edu
# STUDENT ID

from __future__ import annotations

import json
from collections import namedtuple
import socket


class JournalServerError(Exception):
  pass

# Namedtuple to hold the values retrieved from json messages.
# TODO: update this named tuple to use DSP protocol keys
connection = namedtuple('Connection', ['socket','send','recv'])

class DS_Protocol:
  JOIN = "join" # make account
  BIO = "bio" # change bio
  POST = "post" # make post

  def __init__(self, protocol=None, data=None):
    self.protocol = protocol
    self.data = data

  def format(ds: DS_Protocol) -> str:
    return f"{ds.protocol}|{ds.data}"

  def join(_conn: connection, username: str, password: str):
    print("test")


def extract_json(json_msg:str) -> connection:
  '''
  Call the json.loads function on a json string and convert it to a DataTuple object
  
  TODO: replace the pseudo placeholder keys with actual DSP protocol keys
  '''
  try:
    json_obj = json.loads(json_msg)
    send = json_obj['socket']
    recv = json_obj['send']['recv']
  except json.JSONDecodeError:
    print("Json cannot be decoded.")

  return connection(send, recv)

def init(sock: socket) -> connection:
  try:
    f_send = sock.makefile("w")
    f_recv = sock.makefile("r")
  except:
    raise JournalServerError("Invalid socket connection")
  
  return connection(
    socket = sock,
    send = f_send,
    recv = f_recv
  )

def disconnect(_conn: connection):
  # closes read and writes the file objects
  _conn.send.close()
  _conn.recv.close()

