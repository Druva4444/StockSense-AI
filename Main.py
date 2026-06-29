import schedule
import time
from Pipeline import job
from Scrapper import writeDB
from DB import get_connection
stocks=["HDFC BANK","SBI "]
conn =get_connection()
cur = conn.cursor()
cur.execute("delete from article")
conn.commit()
def Mainjob():
    for stock in stocks:
        writeDB(stock)# fetch aand push to db
        job() #  gets flagged by finance llm and passes to main llm
        cur.execute('delete from article')
        conn.commit()

schedule.every(1).minutes.do(Mainjob)
while True:
    schedule.run_pending()
    time.sleep(1)

