import time
from threading import Thread

from datetime import datetime

def start(number):
	time.sleep(1) 
	print(f'information {number}') 

for i in range(5): 
	start(i + 1)

t1 = datetime.now()
threads = [Thread(target = start, args = (i+1,)) for i in range(5)] 
for t in threads:
    t.start()
for t in threads:
    t.join()

print('time ', (datetime.now() - t1).microseconds)