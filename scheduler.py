import schedule
import time
def importdb() :
    print("lala")

schedule.every().day().at("10:30").do(importdb)

while 1:
    schedule.run_pending()
    time.sleep(1)
