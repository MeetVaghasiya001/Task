import schedule
import time as tm 
from datetime import datetime

def main():
    print('run in 5 second')

schedule.every(5).seconds.do(main)

while True:
    schedule.run_pending()
    tm.sleep(1)