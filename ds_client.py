# Starter code for assignment 3 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your
# information.

# Alex Reyes Aranda
# areyesar@uci.edu
# 69754988


import socket
import ds_protocol as dsp
from ui import *
import time
from typing import Callable
from collections import namedtuple


Connection = namedtuple("Connection", ["socket", "send", "recv"])


def init(sock: socket) -> Connection:
    try:
        f_send = sock.makefile("w")
        f_recv = sock.makefile("r")
    except Exception:
        raise dsp.DSPServerError
    return Connection(
        socket=sock,
        send=f_send,
        recv=f_recv
      )


def write_command(_conn: Connection, cmd: str):
    try:
        _conn.send.write(cmd + "\r\n")
        _conn.send.flush()
    except Exception:
        raise dsp.DSPServerError


def read_command(_conn: Connection) -> str:
    cmd = _conn.recv.readline()
    return cmd


def connect_to_server(host: str, port: int) -> socket.socket:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        return sock
    except Exception:
        return None


def send(server: str, port: int, username: str,
         password: str, message: str, bio: str = None):
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
        sock = connect_to_server(server, port)
        if sock is None:
            print("couldn't connect to server")
            return
        _conn = init(sock)
        json_msg = ""
        usr_token = get_token(_conn, username, password)
        if (username and password != "") and (message == "") and bio is None:
            json_msg = {"join":
                        {"username": username,
                         "password": password,
                         "token": ""}}
        elif message != "" and bio is None:
            json_msg = {"token": usr_token,
                        "post": {"entry": message,
                                 "timestamp": str(time.time())}}
        elif message == "" and bio != "":
            json_msg = {"token": usr_token,
                        "bio": {"entry": bio,
                                "timestamp": str(time.time())}}
        else:
            print("something went wrong.")
        json_msg = json.dumps(json_msg)
        write_command(_conn, json_msg)
        response = read_command(_conn)
        parsed_resp = dsp.extract_json(response)
        if parsed_resp.type == dsp.OK:
            return True
        elif parsed_resp.type == dsp.ERROR:
            return False
    except Exception as ex:
        return ("An error occured while sending. ", ex)


def get_token(_conn: Connection, username: str, password: str) -> str:
    join_msg = {"join":
                {"username": username,
                 "password": password,
                 "token": ""}}
    join_msg = json.dumps(join_msg)
    write_command(_conn, join_msg)
    resp = read_command(_conn)
    parsed_resp = dsp.extract_json(resp)
    return str(parsed_resp.token)
