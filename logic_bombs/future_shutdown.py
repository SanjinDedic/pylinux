#Linux script that shuts down the computer at a given date and time
import os

import schedule
import time

def job():
    os.system("shutdown /s /t 1")
    return schedule.CancelJob

schedule.every(1).hours.until("2022-12-21 3:10").do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)
