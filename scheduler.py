import schedule
import time
from subprocess import call
def importdb() :
    call("python","MainScript.py")

schedule.every().day().at("12:01").do(importdb)

while 1:
    schedule.run_pending()
    time.sleep(1)
