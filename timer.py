import schedule
import time
import sms

#Send message every 30 seconds
def job():
    sms.sendMessage()

#Schedule to send every 30 seconds
schedule.every(30).seconds.do(job)

#Loop endlessly, running the job
while True:
    schedule.run_pending()
    time.sleep(1)
    