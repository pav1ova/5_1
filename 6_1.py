import time
from threading import Thread

def start(number):
	time.sleep(1) 
	print(f'information {number}') 
for i in range(5): 
	start(i + 1)
