#DETACHED

import ds_client as dsc
import ds_protocol as dsp
import a3
from ui import *

port = 3021



def run_options(n_profile: Profile, tup:tuple):
    command = tup[0]
    data = tup[1]
    # profile is working alright
    if command == "-post":
        print(dsp.post(server=n_profile.dsuserver, port=port, username=n_profile.username, password=n_profile.password,message=data))
    elif command == "-bio":
        print(dsp.bio(server=n_profile.dsuserver, port=port, username=n_profile.username, password=n_profile.password,bio=data))
    else:
        print("return options failed.")

def parse_input_options(str_input:str) -> list:
    # input: String o_input
    # output: List tuples matching sub with sub input

    #-post hello -bio hi this my new bio

    tpl_list =[]
    allowed_subs = ["-post", "-bio"]

    present_subs = list(filter(lambda d: d in allowed_subs, str_input.split()))
    input_split = str_input.split()
    for i in range(len(input_split)):
        if input_split[i] in allowed_subs:
            input_split[i] = "_"
    input_split = " ".join(input_split)
    input_split = input_split.split("_")[1:]
    input_split = list(map(lambda d:d.strip(), input_split))
    tpl_list = list(map(lambda x,y: (x,y), present_subs, input_split))
    return tpl_list




    
    



