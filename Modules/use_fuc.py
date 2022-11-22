import random

cm_in_meter=100
meter_in_km=1000
pink_floyd=["roguers waters","david gilmour"]


def get_file_extention(file_name):

    return file_name[file_name.index(".")+1:]

def roll_dice(num ):
    return random.randint(1,num)