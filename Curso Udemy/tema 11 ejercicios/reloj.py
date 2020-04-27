import datetime
import os
import time

while True:
    dt = datetime.datetime.now()
    print(dt.strftime("%H:%M:%S"))    
    time.sleep(1)
    os.system ("cls") 
