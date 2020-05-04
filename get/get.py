import yahooquery as yq 
import os, pandas  
import pymysql.cursors

config = {
  'host': os.environ['DB_HOST'],
  'db': os.environ['DB_NAME'],
  'user': os.environ['DB_USER'],
  'password': os.environ['DB_PASS']
}

# get database connection
def get_db_connection(dbconfdic):
    try:
        connection = pymysql.connect(dbconfdic['host'],dbconfdic['user'],dbconfdic['password'],dbconfdic['db'])
    except Exception as e:
        syslog.syslog(syslog.LOG_ERR, e)
    return connection

# get stock symbol
def get_ticker(str):
    return str.strip().split(",")[0]

# get connection to database `shares`
connection = get_db_connection(config)

with open("us-ticker-list.csv","r+") as file: 
    for line in file:
        if ('NEW' in line):
            # get the ticker symbol
            ticker = get_ticker(line)
    
            # get stock basic information
            stockobj = yq.Ticker(ticker)
            
            sctr = stockobj.asset_profile[ticker]['sector']
            ndstr = stockobj.asset_profile[ticker]['industry']
            lngBsnssSmmry = stockobj.asset_profile[ticker]['longBusinessSummary']
            wbst = stockobj.asset_profile[ticker]['website']
            cntry = stockobj.asset_profile[ticker]['country']
            fllTmmplys = stockobj.asset_profile[ticker]['fullTimeEmployees']
    
            # INSERT stock basic information into table `ushareInfo`
            cursor = connection.cursor()
            
            # Create new record 
            sql = "INSERT INTO `ushareInfo` (`symbol`, `sector`, `industry`, `longBusinessSummary`, `website`, `country`,`fullTimeEmployees`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    
            cursor.execute(sql, (ticker, sctr, ndstr, lngBsnssSmmry, wbst, cntry, fllTmmplys))

            # get stock historial price
            historyprice = stockobj.history('max')
            index = historyprice.index
            for i in range(len(index)):
                iopen = historyprice.at[index[i],'open']
                iclose = historyprice.at[index[i],'close']
                ihigh = historyprice.at[index[i],'high']
                ilow = historyprice.at[index[i],'low']
                ivolume = historyprice.at[index[i],'volume']
                idate = index[i].date()
                # Create new record 
                sql = "INSERT INTO `usharePrices` (`symbol`, `date`, `open`, `close`, `high`, `low`,`volume`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (ticker, idate, float(iopen), float(iclose), float(ihigh), float(ilow), int(ivolume)))

        elif ('ADDED' in line):
            # get the ticker symbol
            ticker = get_ticker(line)
    
            # get stock basic information
            stockobj = yq.Ticker(ticker)
            
            # get cursor table `usharePrices`
            cursor = connection.cursor()
            
            # get stock historial price
            historyprice = stockobj.history('1d')
            index = historyprice.index
            topen = historyprice.at[index[0],'open']
            tclose = historyprice.at[index[0],'close']
            thigh = historyprice.at[index[0],'high']
            tlow = historyprice.at[index[0],'low']
            tvolume = historyprice.at[index[0],'volume']
            tdate = index[0].date()
            # Create new record 
            sql = "INSERT INTO `usharePrices` (`symbol`, `date`, `open`, `close`, `high`, `low`,`volume`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (ticker, tdate, float(topen), float(tclose), float(thigh), float(tlow), int(tvolume)))

        else:
            pass

# connection is not autocommit by default. So you must commit to save your changes.
connection.commit()
connection.close()

# update ticker records 'NEW' to 'ADDED'
new_file_content = ""
with open("us-ticker-list.csv","r+") as file: 
    for line in file:
      stripped_line = line.strip()
      new_line = stripped_line.replace("NEW", "ADDED")
      new_file_content += new_line +"\n"

with open("us-ticker-list.csv","w") as file: 
    file.write(new_file_content)
