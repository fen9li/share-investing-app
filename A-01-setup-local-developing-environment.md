## test yahoo finance API in container

```
docker run -it python:3.8 bash

pip install yahooquery

apt -y update
apt -y install vim

root@f1c67c1d477b:/# vim yahoo.py
root@f1c67c1d477b:/# cat yahoo.py
import yahooquery as yq 

aapl = yq.Ticker('aapl')

print(aapl.asset_profile)
print(aapl.financial_data)
print(aapl.summary_detail)

print(aapl.history('5d'))

root@f1c67c1d477b:/# 

root@f1c67c1d477b:/# python yahoo.py 
{'aapl': {'address1': 'One Apple Park Way', 'city': 'Cupertino', 'state': 'CA', 'zip': '95014', 'country': 'United States', 'phone': '408-996-1010', 'website': 'http://www.apple.com', 'industry': 'Consumer Electronics', 'sector': 'Technology', 'longBusinessSummary': 'Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide. It also sells various related services. The company offers iPhone, a line of smartphones; Mac, a line of personal computers; iPad, a line of multi-purpose tablets; and wearables, home, and accessories comprising AirPods, Apple TV, Apple Watch, Beats products, HomePod, iPod touch, and other Apple-branded and third-party accessories. It also provides digital content stores and streaming services; AppleCare support services; and iCloud, a cloud service, which stores music, photos, contacts, calendars, mail, documents, and others. In addition, the company offers various service, such as Apple Arcade, a game subscription service; Apple Card, a co-branded credit card; Apple News+, a subscription news and magazine service; and Apple Pay, a cashless payment service, as well as licenses its intellectual property, and provides other related services. The company serves consumers, and small and mid-sized businesses; and the education, enterprise, and government markets. It sells and delivers third-party applications for its products through the App Store, Mac App Store, and Watch App Store. The company also sells its products through its retail and online stores, and direct sales force; and third-party cellular network carriers, wholesalers, retailers, and resellers. Apple Inc. has a collaboration with Google to develop COVID-19 tracking system for Android and iOS devices. Apple Inc. was founded in 1977 and is headquartered in Cupertino, California.', 'fullTimeEmployees': 137000, 'companyOfficers': [{'maxAge': 1, 'name': 'Mr. Timothy D. Cook', 'age': 58, 'title': 'CEO & Director', 'yearBorn': 1961, 'fiscalYear': 2019, 'totalPay': 11555466, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Luca  Maestri', 'age': 55, 'title': 'CFO & Sr. VP', 'yearBorn': 1964, 'fiscalYear': 2019, 'totalPay': 3576221, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Jeffrey E. Williams', 'age': 55, 'title': 'Chief Operating Officer', 'yearBorn': 1964, 'fiscalYear': 2019, 'totalPay': 3574503, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Ms. Katherine L. Adams', 'age': 55, 'title': 'Sr. VP, Gen. Counsel & Sec.', 'yearBorn': 1964, 'fiscalYear': 2019, 'totalPay': 3598384, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': "Ms. Deirdre  O'Brien", 'age': 52, 'title': 'Sr. VP of People & Retail', 'yearBorn': 1967, 'fiscalYear': 2019, 'totalPay': 2690253, 'exercisedValue': 0, 'unexercisedValue': 0}], 'auditRisk': 1, 'boardRisk': 1, 'compensationRisk': 3, 'shareHolderRightsRisk': 1, 'overallRisk': 1, 'governanceEpochDate': '2019-12-05 00:00:00', 'compensationAsOfEpochDate': '2019-12-31 00:00:00', 'maxAge': 86400}}
{'aapl': {'maxAge': 86400, 'currentPrice': 289.07, 'targetHighPrice': 370.8, 'targetLowPrice': 207.77, 'targetMeanPrice': 308.91, 'targetMedianPrice': 315.0, 'recommendationMean': 2.0, 'recommendationKey': 'buy', 'numberOfAnalystOpinions': 37, 'totalCash': 94051000320, 'totalCashPerShare': 21.699, 'ebitda': 77305004032, 'totalDebt': 118760996864, 'quickRatio': 1.298, 'currentRatio': 1.496, 'totalRevenue': 267980996608, 'debtToEquity': 151.433, 'revenuePerShare': 60.097, 'returnOnAssets': 0.12377, 'returnOnEquity': 0.62094, 'grossProfits': 98392000000, 'freeCashflow': 45040123904, 'operatingCashflow': 75373002752, 'earningsGrowth': 0.037, 'revenueGrowth': 0.005, 'grossMargins': 0.3811, 'ebitdaMargins': 0.28847, 'operatingMargins': 0.24475999, 'profitMargins': 0.21350001, 'financialCurrency': 'USD'}}
{'aapl': {'maxAge': 1, 'priceHint': 2, 'previousClose': 293.8, 'open': 286.25, 'dayLow': 285.85, 'dayHigh': 299.0, 'regularMarketPreviousClose': 293.8, 'regularMarketOpen': 286.25, 'regularMarketDayLow': 285.85, 'regularMarketDayHigh': 299.0, 'dividendRate': 3.28, 'dividendYield': 0.0113, 'exDividendDate': '2020-05-08 00:00:00', 'payoutRatio': 0.2408, 'fiveYearAvgDividendYield': 1.59, 'beta': 1.173542, 'trailingPE': 22.711346, 'forwardPE': 19.624577, 'volume': 60154175, 'regularMarketVolume': 60154175, 'averageVolume': 50937266, 'averageVolume10days': 38180283, 'averageDailyVolume10Day': 38180283, 'bid': 287.61, 'ask': 287.9, 'bidSize': 1200, 'askSize': 1400, 'marketCap': 1264820027392, 'fiftyTwoWeekLow': 170.27, 'fiftyTwoWeekHigh': 327.85, 'priceToSalesTrailing12Months': 4.7198124, 'fiftyDayAverage': 263.4409, 'twoHundredDayAverage': 279.22528, 'trailingAnnualDividendRate': 3.08, 'trailingAnnualDividendYield': 0.010483322, 'currency': 'USD', 'fromCurrency': None, 'toCurrency': None, 'lastMarket': None, 'algorithm': None, 'tradeable': False}}
                       volume         low  ...       close    adjclose
2020-04-27 13:30:00  29271900  279.950012  ...  283.170013  283.170013
2020-04-28 13:30:00  28001200  278.200012  ...  278.579987  278.579987
2020-04-29 13:30:00  34320200  283.890015  ...  287.730011  287.730011
2020-04-30 13:30:00  45766000  288.350006  ...  293.799988  293.799988
2020-05-01 13:30:00  60095200  285.850006  ...  289.070007  289.070007

[5 rows x 6 columns]
root@f1c67c1d477b:/#  
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

## change `mariadb adminer` container to `phpmyadmin` container

* the default `phpmyadmin` configuration settings

```
[fli@192-168-1-4 share-get-data]$ docker container ls
CONTAINER ID        IMAGE                          COMMAND                  CREATED             STATUS              PORTS                    NAMES
33b15ce109f0        phpmyadmin/phpmyadmin:latest   "/docker-entrypoint.…"   10 minutes ago      Up 10 minutes       0.0.0.0:8080->80/tcp     phpmyadmin
48400b0dd689        share-get-data_get             "sh -c 'sleep infini…"   10 minutes ago      Up 10 minutes                                getdata
2efd730efca8        mariadb:latest                 "docker-entrypoint.s…"   10 minutes ago      Up 10 minutes       0.0.0.0:3306->3306/tcp   mariadb
[fli@192-168-1-4 share-get-data]$ docker exec -it 33b bash
root@33b15ce109f0:/var/www/html# cd /etc/phpmyadmin/
root@33b15ce109f0:/etc/phpmyadmin# ls -l
total 12
-rw-r--r--. 1 root root 4642 Apr 18 16:15 config.inc.php
-rw-r--r--. 1 root root   68 Apr 30 12:33 config.secret.inc.php
-rw-r--r--. 1 root root    0 Apr 30 12:33 config.user.inc.php
root@33b15ce109f0:/etc/phpmyadmin#

root@33b15ce109f0:/etc/phpmyadmin# cat config.secret.inc.php 
<?php
$cfg['blowfish_secret'] = '%#9Q/>RVYqzTWw7VN_d9p8Jg).l{pDh_';
root@33b15ce109f0:/etc/phpmyadmin# 

root@33b15ce109f0:/etc/phpmyadmin# cat config.user.inc.php 
root@33b15ce109f0:/etc/phpmyadmin# 
```

> Note: [Adding Custom Configuration to phpmyadmin](https://hub.docker.com/r/phpmyadmin/phpmyadmin/)

You can add your own custom `config.inc.php` settings (such as Configuration Storage setup) by creating a file named `config.user.inc.php` with the various user defined settings in it, and then linking it into the container using:

`-v /some/local/directory/config.user.inc.php:/etc/phpmyadmin/config.user.inc.php`

On the `docker run` line like this:

`docker run --name myadmin -d --link mysql_db_server:db -p 8080:80 -v /some/local/directory/config.user.inc.php:/etc/phpmyadmin/config.user.inc.php phpmyadmin/phpmyadmin`

* create `config.user.inc.php` to enable row actions
```
[fli@192-168-1-4 share-get-data]$ cat phpmyadmin/config.user.inc.php 
<?php
$cfg['ActionLinksMode'] = 'both';
[fli@192-168-1-4 share-get-data]$ 
```

* update `docker-compose.yml` to mount `phpmyadmin` to `/etc/phpmyadmin`

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

  get:
    build: ./app
    container_name: getdata
    environment:
      DB_HOST: mariadb
      DB_NAME: shares
      DB_USER: fen9li
      DB_PASS: changeme
    volumes:
      - ${PWD}/app:/app
    networks:
      - backend
    depends_on:
      - mariadb

  phpmyadmin:
    image: phpmyadmin/phpmyadmin:latest
    container_name: phpmyadmin
    networks:
      - backend
    ports:
      - '8080:80'
    volumes:
      - /sessions
      - ${PWD}/phpmyadmin/config.user.inc.php:/etc/phpmyadmin/config.user.inc.php
    environment:
      - PMA_HOST=mariadb
    depends_on:
      - mariadb

  mariadb:
    image: mariadb:latest
    container_name: mariadb
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: changeme
      MYSQL_DATABASE: shares
      MYSQL_USER: fen9li
      MYSQL_PASSWORD: changeme
    networks:
      - backend
    ports:
      - '3306:3306'
    volumes:
      - mariadb_data:/var/lib/mysql
[fli@192-168-1-4 share-get-data]$      
```

> Note 1: map ports for `phpmyadmin - 8080:80` - this maps inner port `80` from inside the container, to port `8000` on docker host machine.    
> Note 2: environment variable `PMA_ARBITRARY=1` can be set to add 'server' input field to phpmyadmin login page.

* spin up containers

```
docker-compose up -d


[fli@192-168-1-4 share-get-data]$ docker container ls
CONTAINER ID        IMAGE                          COMMAND                  CREATED             STATUS              PORTS                    NAMES
6df7518cf67b        phpmyadmin/phpmyadmin:latest   "/docker-entrypoint.…"   29 seconds ago      Up 25 seconds       0.0.0.0:8080->80/tcp     phpmyadmin
3ad47e8647ec        share-get-data_get             "sh -c 'sleep infini…"   29 seconds ago      Up 26 seconds                                getdata
547f64199b2d        mariadb:latest                 "docker-entrypoint.s…"   30 seconds ago      Up 28 seconds       0.0.0.0:3306->3306/tcp   mariadb
[fli@192-168-1-4 share-get-data]$ docker volume ls
DRIVER              VOLUME NAME
local               0a326b229de917464f10fe71681c8b28594870840880fb47a2b1708d2fb87298
local               share-get-data_mariadb_data
[fli@192-168-1-4 share-get-data]$ docker network ls
NETWORK ID          NAME                     DRIVER              SCOPE
2ab7425f6078        bridge                   bridge              local
3998d62e2b3f        host                     host                local
7747599528aa        none                     null                local
2c8a8fa93640        share-get-data_backend   bridge              local
[fli@192-168-1-4 share-get-data]$ 

[fli@192-168-1-4 share-get-data]$ docker container inspect 547 --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'
192.168.144.2
[fli@192-168-1-4 share-get-data]$     
```

* access `phpmyadmin` container from browser by user `root`

![db-phpmyadmin-01](images/db-phpmyadmin-01.png)

![db-phpmyadmin-02](images/db-phpmyadmin-02.png)

## create `ushare-info` table in mariadb

* create/update `mariadb/shares.sql`

* import `mariadb/shares.sql` to mariadb

```
[fli@192-168-1-4 share-get-data]$ pwd
/home/fli/share-get-data
[fli@192-168-1-4 share-get-data]$ ls mariadb/
shares.sql
[fli@192-168-1-4 share-get-data]$ docker exec -i mariadb mysql -uroot -pchangeme shares < mariadb/shares.sql
[fli@192-168-1-4 share-get-data]$ 
```

![db-create-table-01](images/db-create-table-01.png)

![db-create-table-02](images/db-create-table-02.png)

## create/update `app/get.py`
```
[fli@192-168-1-4 share-get-data]$ cat app/get.py 
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
    sql = "INSERT INTO `ushare-info` (`symbol`, `sector`, `industry`, `longBusinessSummary`, `website`, `country`, `currency`, `fullTimeEmployees`, `forwardPE`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, ('MSFT', 'Technology', 'Software—Infrastructure', 'Microsoft Corporation develops, licenses, and supports software, services, devices, and solutions worldwide. Its Productivity and Business Processes segment offers Office, Exchange, SharePoint, Microsoft Teams, Office 365 Security and Compliance, and Skype for Business, as well as related Client Access Licenses (CAL); and Skype, Outlook.com, and OneDrive.', 'http://www.microsoft.com', 'United States', 'US', 144000, 27.746733 ))
 
    # connection is not autocommit by default. So you must commit to save
    # your changes.
  connection.commit()
 
  with connection.cursor() as cursor:
    # Read a single record
    sql = "SELECT `symbol`, `sector` FROM `ushare-info` WHERE `symbol`=%s"
    cursor.execute(sql, ('MSFT',))
    result = cursor.fetchone()
    print(result)
finally:
  connection.close()

msft = yf.Ticker("MSFT")
stockinfo = msft.info

while True:
  time.sleep(1)
[fli@192-168-1-4 share-get-data]$ 
```

## Process to build up from scratch

```
git clone -b develop git@github.com:fen9li/share-investing-app.git

docker-compose up -d

[fli@192-168-1-4 share-investing-app]$ mysql -h 127.0.0.1 -u root -p shares < mariadb/shares.sql 
Enter password: changeme
[fli@192-168-1-4 share-investing-app]$ 
```

## Appendix A: Test connecting to mariadb container from inside `getdata` container

```
[fli@192-168-1-4 share-get-data]$ cat Dockerfile
FROM python:3.8.2-slim

COPY requirements.txt /
RUN pip install -r /requirements.txt

VOLUME /app
WORKDIR /app

CMD ["sh", "-c", "sleep infinity"]
[fli@192-168-1-4 share-get-data]$ 

[fli@192-168-1-4 share-get-data]$ docker images
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
mariadb                 latest              b6184b68d1fd        5 days ago          357MB
python                  3.8.2-slim          e8ad3533cb52        6 days ago          194MB
phpmyadmin/phpmyadmin   latest              f257b784d16f        11 days ago         468MB
[fli@192-168-1-4 share-get-data]$ 

docker-compose up -d

[fli@192-168-1-4 ~]$ docker container ls
CONTAINER ID        IMAGE                          COMMAND                  CREATED             STATUS              PORTS                    NAMES
6df7518cf67b        phpmyadmin/phpmyadmin:latest   "/docker-entrypoint.…"   12 minutes ago      Up 12 minutes       0.0.0.0:8080->80/tcp     phpmyadmin
3ad47e8647ec        share-get-data_get             "sh -c 'sleep infini…"   12 minutes ago      Up 12 minutes                                getdata
547f64199b2d        mariadb:latest                 "docker-entrypoint.s…"   12 minutes ago      Up 12 minutes       0.0.0.0:3306->3306/tcp   mariadb
[fli@192-168-1-4 ~]$ 

[fli@192-168-1-4 ~]$ docker container exec -it 3ad bash
root@3ad47e8647ec:/app# ls -l
total 12
-rw-rw-r--. 1 1000 1000  148 Apr 30 13:45 Dockerfile
-rw-rw-r--. 1 1000 1000 1564 Apr 30 13:44 get.py
-rw-rw-r--. 1 1000 1000   45 Apr 30 07:32 requirements.txt
root@3ad47e8647ec:/app# 

root@3ad47e8647ec:/app# env
HOSTNAME=3ad47e8647ec
PYTHON_VERSION=3.8.2
PWD=/app
DB_USER=fen9li
HOME=/root
LANG=C.UTF-8
GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568
TERM=xterm
DB_HOST=mariadb
SHLVL=1
PYTHON_PIP_VERSION=20.0.2
DB_NAME=shares
PYTHON_GET_PIP_SHA256=421ac1d44c0cf9730a088e337867d974b91bdce4ea2636099275071878cc189e
PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/d59197a3c169cef378a22428a3fa99d33e080a5d/get-pip.py
PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
DB_PASS=changeme
_=/usr/bin/env
root@3ad47e8647ec:/app# 

apt -y update
apt -y install vim iputils-ping

root@3ad47e8647ec:/app# ping -c4 ${DB_HOST}
PING mariadb (192.168.144.2) 56(84) bytes of data.
64 bytes from mariadb.share-get-data_backend (192.168.144.2): icmp_seq=1 ttl=64 time=0.199 ms
64 bytes from mariadb.share-get-data_backend (192.168.144.2): icmp_seq=2 ttl=64 time=0.154 ms
64 bytes from mariadb.share-get-data_backend (192.168.144.2): icmp_seq=3 ttl=64 time=0.197 ms
64 bytes from mariadb.share-get-data_backend (192.168.144.2): icmp_seq=4 ttl=64 time=0.160 ms

--- mariadb ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3ms
rtt min/avg/max/mdev = 0.154/0.177/0.199/0.024 ms
root@3ad47e8647ec:/app# 

root@5f85d4728481:/app# vim get.py 
root@3ad47e8647ec:/app# cat get.py 
import yfinance as yf
import os, json
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
    sql = "INSERT INTO `ushare-info` (`symbol`, `sector`, `industry`, `longBusinessSummary`, `website`, `country`, `currency`, `fullTimeEmployees`, `forwardPE`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, ('MSFT', 'Technology', 'Software—Infrastructure', 'Microsoft Corporation develops, licenses, and supports software, services, devices, and solutions worldwide. Its Productivity and Business Processes segment offers Office, Exchange, SharePoint, Microsoft Teams, Office 365 Security and Compliance, and Skype for Business, as well as related Client Access Licenses (CAL); and Skype, Outlook.com, and OneDrive.', 'http://www.microsoft.com', 'United States', 'US', 144000, 27.746733 ))
 
    # connection is not autocommit by default. So you must commit to save your changes.
  connection.commit()
 
  with connection.cursor() as cursor:
    # Read a single record
    sql = "SELECT `symbol`, `sector` FROM `ushare-info` WHERE `symbol`=%s"
    cursor.execute(sql, ('MSFT',))
    result = cursor.fetchone()
    print(result)
finally:
  connection.close()

msft = yf.Ticker("MSFT")
stockinfo = msft.info
root@3ad47e8647ec:/app# 
```

## Appendix B: command line to access mariadb 

```
[fli@192-168-1-4 ~]$ mysql -h 127.0.0.1 -u root -p
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 29
Server version: 10.4.12-MariaDB-1:10.4.12+maria~bionic mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> use shares;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [shares]>

MariaDB [shares]> select * from `ushare-prices` where date='2012-05-18';
+------+--------+------------+-------+-------+-------+-------+-----------+
| Id   | symbol | date       | open  | close | high  | low   | volume    |
+------+--------+------------+-------+-------+-------+-------+-----------+
|   71 | FB     | 2012-05-18 | 42.05 | 38.23 |    45 |    38 | 573576400 |
| 8678 | MSFT   | 2012-05-18 | 29.79 | 29.27 | 29.81 | 29.17 |  56205300 |
+------+--------+------------+-------+-------+-------+-------+-----------+
2 rows in set (0.01 sec)

MariaDB [shares]> 

MariaDB [shares]> exit
Bye
[fli@192-168-1-4 ~]$ 
```

> reference [Yahooquery](https://github.com/dpguthrie/yahooquer)

~~reference [Yahoo API for python](https://github.com/ranaroussi/yfinance)~~    
~~reference [Reliably download historical market data from Yahoo! Finance with Python](https://aroussi.com/post/python-yahoo-finance~~    
~~reference [Build minimum docker image](https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3)~~    

