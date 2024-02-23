# dsp_demo.py

import ds_client
server = "168.235.86.101" # replace with actual server ip address
port = 3021 # replace with actual port
ds_client.send(server, port, "noobpro", "pwd123", "Hello World!")