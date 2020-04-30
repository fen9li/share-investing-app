import yfinance as yf
import os, json, time 
import pymysql.cursors

config = {
  'host': os.environ['DB_HOST'],
  'db': os.environ['DB_NAME'],
  'user': os.environ['DB_USER'],
  'password': os.environ['DB_PASS'],
  'charset': 'utf8mb4',
  'cursorclass': pymysql.cursors.DictCursor
}

connection = pymysql.connect(**config)

try:
  with connection.cursor() as cursor:
    # Create a new record
    sql = "INSERT INTO `us-share-info` (`symbol`, `sector`, `industry`, `longBusinessSummary`, `website`, `country`, `currency`, `fullTimeEmployees`, `forwardPE`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, ('MSFT', 'Technology', 'Software—Infrastructure', 'Microsoft Corporation develops, licenses, and supports software, services, devices, and solutions worldwide. Its Productivity and Business Processes segment offers Office, Exchange, SharePoint, Microsoft Teams, Office 365 Security and Compliance, and Skype for Business, as well as related Client Access Licenses (CAL); and Skype, Outlook.com, and OneDrive.', 'http://www.microsoft.com', 'United States', 'US', 144000, 27.746733 ))
 
    # connection is not autocommit by default. So you must commit to save
    # your changes.
  connection.commit()
 
  with connection.cursor() as cursor:
    # Read a single record
    sql = "SELECT `symbol`, `sector` FROM `us-share-info` WHERE `symbol`=%s"
    cursor.execute(sql, ('MSFT',))
    result = cursor.fetchone()
    print(result)
finally:
  connection.close()

msft = yf.Ticker("MSFT")
stockinfo = msft.info

while True:
  time.sleep(1)
