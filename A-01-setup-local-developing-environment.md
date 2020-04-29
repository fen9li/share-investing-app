## test yahoo finance API in container

```
docker run -it python:3.8 bash

pip install yfinance lxml

root@e6303538de1d:/# pip list
Package         Version   
--------------- ----------
certifi         2020.4.5.1
chardet         3.0.4     
idna            2.9       
multitasking    0.0.9     
numpy           1.18.3    
pandas          1.0.3     
pip             20.0.2    
python-dateutil 2.8.1     
pytz            2020.1    
requests        2.23.0    
setuptools      46.1.3    
six             1.14.0    
urllib3         1.25.9    
wheel           0.34.2    
yfinance        0.1.54    
root@e6303538de1d:/# 

apt -y install
apt -y install vim

root@e6303538de1d:/# vim yahoo.py
root@e6303538de1d:/# cat yahoo.py
import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
print(msft.info)

# get historical market data
hist = msft.history(period="5d")

root@e6303538de1d:/# 

root@e6303538de1d:/# python yahoo.py 
{'zip': '98052', 'sector': 'Technology', 'fullTimeEmployees': 144000, 'longBusinessSummary': 'Microsoft Corporation develops, licenses, and supports software, services, devices, and solutions worldwide. Its Productivity and Business Processes segment offers Office, Exchange, SharePoint, Microsoft Teams, Office 365 Security and Compliance, and Skype for Business, as well as related Client Access Licenses (CAL); and Skype, Outlook.com, and OneDrive. It also provides LinkedIn that includes Talent and marketing solutions, and subscriptions; and Dynamics 365, a set of cloud-based and on-premises business solutions for small and medium businesses, large organizations, and divisions of enterprises. Its Intelligent Cloud segment licenses SQL and Windows Servers, Visual Studio, System Center, and related CALs; GitHub that provides a collaboration platform and code hosting service for developers; and Azure, a cloud platform. It also provides support services and Microsoft consulting services to assist customers in developing, deploying, and managing Microsoft server and desktop solutions; and training and certification to developers and IT professionals on various Microsoft products. Its More Personal Computing segment offers Windows OEM licensing and other non-volume licensing of the Windows operating system; Windows Commercial, such as volume licensing of the Windows operating system, Windows cloud services, and other Windows commercial offerings; patent licensing; Windows Internet of Things; and MSN advertising. It also provides Microsoft Surface, PC accessories, and other intelligent devices; Gaming, including Xbox hardware, and Xbox software and services; video games and third-party video game royalties; and Search, including Bing and Microsoft advertising. It sells its products through distributors and resellers; and directly through digital marketplaces, online stores, and retail stores. It has strategic partnerships with Humana Inc., Nokia, Telkomsel, Swiss Re, and Kubota Corporation. The company was founded in 1975 and is headquartered in Redmond, Washington.', 'city': 'Redmond', 'phone': '425-882-8080', 'state': 'WA', 'country': 'United States', 'companyOfficers': [], 'website': 'http://www.microsoft.com', 'maxAge': 1, 'address1': 'One Microsoft Way', 'fax': '425-706-7329', 'industry': 'Software—Infrastructure', 'previousClose': 174.05, 'regularMarketOpen': 175.59, 'twoHundredDayAverage': 158.27147, 'trailingAnnualDividendYield': 0.011146222, 'payoutRatio': 0.32930002, 'volume24Hr': None, 'regularMarketDayHigh': 175.6672, 'navPrice': None, 'averageDailyVolume10Day': 37969233, 'totalAssets': None, 'regularMarketPreviousClose': 174.05, 'fiftyDayAverage': 158.39658, 'trailingAnnualDividendRate': 1.94, 'open': 175.59, 'toCurrency': None, 'averageVolume10days': 37969233, 'expireDate': None, 'yield': None, 'algorithm': None, 'dividendRate': 2.04, 'exDividendDate': 1589932800, 'beta': 0.962017, 'circulatingSupply': None, 'startDate': None, 'regularMarketDayLow': 169.39, 'priceHint': 2, 'currency': 'USD', 'trailingPE': 29.57847, 'regularMarketVolume': 34392694, 'lastMarket': None, 'maxSupply': None, 'openInterest': None, 'marketCap': 1291583356928, 'volumeAllCurrencies': None, 'strikePrice': None, 'averageVolume': 55443984, 'priceToSalesTrailing12Months': 9.620805, 'dayLow': 169.39, 'ask': 172.38, 'ytdReturn': None, 'askSize': 1200, 'volume': 34392694, 'fiftyTwoWeekHigh': 190.7, 'forwardPE': 27.746733, 'fromCurrency': None, 'fiveYearAvgDividendYield': 1.97, 'fiftyTwoWeekLow': 119.01, 'bid': 172.1, 'tradeable': False, 'dividendYield': 0.0117, 'bidSize': 1100, 'dayHigh': 175.6672, 'exchange': 'NMS', 'shortName': 'Microsoft Corporation', 'longName': 'Microsoft Corporation', 'exchangeTimezoneName': 'America/New_York', 'exchangeTimezoneShortName': 'EDT', 'isEsgPopulated': False, 'gmtOffSetMilliseconds': '-14400000', 'quoteType': 'EQUITY', 'symbol': 'MSFT', 'messageBoardId': 'finmb_21835', 'market': 'us_market', 'annualHoldingsTurnover': None, 'enterpriseToRevenue': 9.51, 'beta3Year': None, 'profitMargins': 0.33016, 'enterpriseToEbitda': 20.84, '52WeekChange': 0.33269525, 'morningStarRiskRating': None, 'forwardEps': 6.12, 'revenueQuarterlyGrowth': None, 'sharesOutstanding': 7606049792, 'fundInceptionDate': None, 'annualReportExpenseRatio': None, 'bookValue': 14.467, 'sharesShort': 53310482, 'sharesPercentSharesOut': 0.0069999998, 'fundFamily': None, 'lastFiscalYearEnd': 1561852800, 'heldPercentInstitutions': 0.74088997, 'netIncomeToCommon': 44323000320, 'trailingEps': 5.741, 'lastDividendValue': None, 'SandP52WeekChange': -0.022862852, 'priceToBook': 11.737748, 'heldPercentInsiders': 0.01421, 'nextFiscalYearEnd': 1625011200, 'mostRecentQuarter': 1577750400, 'shortRatio': 0.82, 'sharesShortPreviousMonthDate': 1584057600, 'floatShares': 7494998724, 'enterpriseValue': 1276748496896, 'threeYearAverageReturn': None, 'lastSplitDate': 1045526400, 'lastSplitFactor': '2:1', 'legalType': None, 'morningStarOverallRating': None, 'earningsQuarterlyGrowth': 0.383, 'dateShortInterest': 1586908800, 'pegRatio': 2.16, 'lastCapGain': None, 'shortPercentOfFloat': 0.0069999998, 'sharesShortPriorMonth': 55155176, 'category': None, 'fiveYearAverageReturn': None, 'regularMarketPrice': 175.59, 'logo_url': 'https://logo.clearbit.com/microsoft.com'}
root@e6303538de1d:/# 
```

## build up mariadb container

* create `docker-compose.yml`
```
[fli@192-168-1-4 share-get-data]$ cat docker-compose.yml 
version: '3'

volumes: 
  mariadb_data:
    driver: local

networks:
  backend:
    driver: bridge

services:
  mariadb:
    image: mariadb:latest
    container_name: mariadb
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: changeme
      MYSQL_DATABASE: mybb
      MYSQL_USER: mybb
      MYSQL_PASSWORD: changeme
    networks:
      - backend
    ports:
      - '3306:3306'
    volumes:
      - mariadb_data:/var/lib/mysql
[fli@192-168-1-4 share-get-data]$ 
```

* spin up mariadb container and check its volume and network

```
docker-compose up -d

[fli@192-168-1-4 share-get-data]$ docker container ls --all
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
98bb65e6792e        mariadb:latest      "docker-entrypoint.s…"   2 hours ago         Up 2 hours          0.0.0.0:3306->3306/tcp   share-get-data_mariadb_1
[fli@192-168-1-4 share-get-data]$ 

[fli@192-168-1-4 share-get-data]$ docker container inspect 98b --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'
172.18.0.2
[fli@192-168-1-4 share-get-data]$ 

[fli@192-168-1-4 share-get-data]$ docker volume ls
DRIVER              VOLUME NAME
local               share-get-data_mariadb_data
[fli@192-168-1-4 share-get-data]$

[fli@192-168-1-4 share-get-data]$ docker network ls
NETWORK ID          NAME                     DRIVER              SCOPE
c99303b1d5b2        bridge                   bridge              local
3998d62e2b3f        host                     host                local
7747599528aa        none                     null                local
33cbae2bb7a9        share-get-data_backend   bridge              local
[fli@192-168-1-4 share-get-data]$ 
```

* login new mariadb container database

> Note: `mysql -h localhost -u root -p` wont work. MySQL connects over TCP/IP when using IP address (127.0.0.1), and uses socket file when using localhost. In this situation, the `mysql.sock` is not available at `/var/lib/mysql/` by default. 

```
[fli@192-168-1-4 ~]$ mysql -h localhost -u root -p
Enter password: 
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/lib/mysql/mysql.sock' (2)
[fli@192-168-1-4 ~]$

[fli@192-168-1-4 ~]$ which mysql
/usr/bin/mysql
[fli@192-168-1-4 ~]$ mysql -h 127.0.0.1 -u root -p
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 8
Server version: 10.4.12-MariaDB-1:10.4.12+maria~bionic mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mybb               |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.00 sec)

MariaDB [(none)]> select host,user from mysql.user;
+-----------+------+
| Host      | User |
+-----------+------+
| %         | mybb |
| %         | root |
| localhost | root |
+-----------+------+
3 rows in set (0.00 sec)

MariaDB [(none)]> show grants for 'mybb'@'%';
+-----------------------------------------------------------------------------------------------------+
| Grants for mybb@%                                                                                   |
+-----------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'mybb'@'%' IDENTIFIED BY PASSWORD '*7ACE763ED393514FE0C162B93996ECD195FFC4F5' |
| GRANT ALL PRIVILEGES ON `mybb`.* TO 'mybb'@'%'                                                      |
+-----------------------------------------------------------------------------------------------------+
2 rows in set (0.00 sec)

MariaDB [(none)]> exit
Bye
[fli@192-168-1-4 ~]$ 
```

## add mariadb adminer container

* update `docker-compose.yml`

```
[fli@192-168-1-4 share-get-data]$ cat docker-compose.yml 
version: '3'

volumes: 
  mariadb_data:
    driver: local

networks:
  backend:
    driver: bridge

services:
  mariadb:
    image: mariadb:latest
    container_name: mariadb
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: changeme
      MYSQL_DATABASE: mybb
      MYSQL_USER: mybb
      MYSQL_PASSWORD: changeme
    networks:
      - backend
    ports:
      - '3306:3306'
    volumes:
      - mariadb_data:/var/lib/mysql
  
  adminer:
    image: adminer
    container_name: adminer
    restart: always
    networks:
      - backend
    ports:
      - 8080:8080
[fli@192-168-1-4 share-get-data]$ 
```

* spin up containers

```
docker-compose up -d

[fli@192-168-1-4 share-get-data]$ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
4612b503eafd        adminer             "entrypoint.sh docke…"   15 minutes ago      Up 15 minutes       0.0.0.0:8080->8080/tcp   adminer
3fe495805afe        mariadb:latest      "docker-entrypoint.s…"   15 minutes ago      Up 15 minutes       0.0.0.0:3306->3306/tcp   mariadb
[fli@192-168-1-4 share-get-data]$ docker container inspect 3fe --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'
172.19.0.2
[fli@192-168-1-4 share-get-data]$  
```

* access `adminer` from browser by user `root`

![db-adminer-01](images/db-adminer-01.png)

![db-adminer-02](images/db-adminer-02.png)

![db-adminer-03](images/db-adminer-03.png)

* access `adminer` from browser by user `mybb`

![db-adminer-04](images/db-adminer-04.png)

![db-adminer-05](images/db-adminer-05.png)


> reference [Yahoo API for python](https://github.com/ranaroussi/yfinance)     
> reference [Reliably download historical market data from Yahoo! Finance with Python](https://aroussi.com/post/python-yahoo-finance)    
> reference [Build minimum docker image](https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3)    

