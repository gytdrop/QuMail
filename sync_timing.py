import time 
from datetime import datetime

# this file ensure the sender and the reciever are in synchronous using the isro NavIC
#it returns a current time based unique sync ID 
def get_navic_timestamp():
    now = datetime.now()
    return f'ISRO-NAVIC-{now.strftime("%Y%m%d%H%M")}'

