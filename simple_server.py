import socket
from collections import namedtuple
from pathlib import Path
import ds_protocol as dsp # bookmark_connection
import Profile


PORT = 2025
HOST = "127.0.0.1"


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.bind((HOST, PORT))
        srv.listen()

        print("Simple server listening on port", PORT)
        connection, addy = srv.accept()
        with connection:
            print("Client connected")
            while True:
                rec_msg = connection.recv(4096)
                print("echo", rec_msg)
                if not rec_msg:
                    break
                connection.sendall(rec_msg)

            print("Client disconnected")

        