# dsp_demo.py

import ds_client
server = "168.235.86.101" # replace with actual server ip address
port = 3021 # replace with actual port
print(ds_client.send(server, port, "melonmusk", "XA123", "Hello World!"))