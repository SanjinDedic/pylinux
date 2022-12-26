#Linux script that shuts down the computer at a given date and time
import os

import schedule
import time

def job():
    os.system("shutdown /s /t 1")

schedule.every(1).second.until("2022-12-21 3:16:00").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)

#every hour check the current time is greater than the given time
