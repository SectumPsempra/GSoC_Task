# GSoC_Task
Task's Readme Page

The .dat files downloaded from the internet is processed using preProcess.py to generate a DST_DATA.csv file, which contains the data as per the format shown here [a link](http://wdc.kugi.kyoto-u.ac.jp/dstae/format/dstformat.html)

## Step - 1 =>

pip install mysql-connector
pip install pandas

## Step - 2 =>
 
1. Run preProcess.py after modifying the location in which you have kept .dat file downloaded from github in this case or the internet from here [a link](http://wdc.kugi.kyoto-u.ac.jp/dstae/) 

## Step - 3 =>

Code used to convert CSV file's data to a database table in mysql.
1. mysql \[username\] \[password\] or mysql -p -u root

2. Enter the following into mysql console from your local directory i.e., where DST_DATA.csv file is saved => 
CREATE TABLE dstdata (dat LONG not null,mont LONG not null,yea LONG,star VARCHAR(20),quicklook VARCHAR(20),inde VARCHAR(20),versio VARCHAR(20),basevalue VARCHAR(20),hourlyvalue VARCHAR(200), meanvalue VARCHAR(100));

3. Follow up => 
load data local infile  
'DST_DATA.csv'  
INTO TABLE dstdata 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
(dat, mont, yea, star, quicklook, inde, versio, basevalue, hourlyvalue, meanvalue);

## Step - 4 =>

1. Run QueryDST.py file and enter the query you want to run, please take help from the internet if you are not familiar with MySQL database queries, the "Field in DB" column printed in output shows the name of the columns in table "dstdata" which will be used to do queries. 

## Result =>
![alt text](https://github.com/SectumPsempra/GSoC_Task/blob/master/results.png)

Still some changes left to be done. Thank You. 
