import schedule
import time
import sms

#Send message every 30 seconds
def job():
    sms.sendMessage()

#Schedule to send every 30 seconds
schedule.every().day.at("07:00").do(job)

#Loop endlessly, running the job
while True:
    schedule.run_pending()
    time.sleep(1) 