# Pre process the .dat file and create a sql database file
import pandas as pd

# Initialize DST
DST = ['DST']

# use list() rather than [], to ensure referencing doesn't happen
# so when we change value of one list another's content doesn't change
YEAR = []
MONTH = []
STAR = []
DATE = []
QUICK_LOOK = []
INDEX = []
VERSION = []
BASE_VALUE = []
HOURLY_VALUE = []
DAILY_MEAN_VALUE = []

# input the .dat file
data = '/../../../DST Files/Jan57-Feb18.dat'

# Open the data file and access the contents
# assign rows content to specific list variables
# so that they can be stored in .csv file
# before saving into a .db file
with open(data, "r") as File:
    lines = File.readlines()
    for line in lines:

        if line[14:16] == '  ':
            YEAR.append('19' + line[3:5])
        else:
            YEAR.append(line[14:16] + line[3:5])

        MONTH.append(line[5:7])
        STAR.append(line[7])
        DATE.append(line[8:10])

        if line[10:12] == '  ':
            QUICK_LOOK.append('EMPTY')
        else:
            QUICK_LOOK.append(line[10:12])

        INDEX.append(line[12])
        VERSION.append(line[13])
        BASE_VALUE.append(line[16:20])

        if line[20:116] == '9'*96:
            HOURLY_VALUE.append('EMPTY')
        else:
            HOURLY_VALUE.append(line[20:116])

        if line[116:120] == '9999':
            DAILY_MEAN_VALUE.append('EMPTY')
        else:
            DAILY_MEAN_VALUE.append(line[116:120])
"""
print(YEAR[:10])
print(DATE[:10])
print(QUICK_LOOK[:10])
print(INDEX[:10])
print(VERSION[:10])
print(BASE_VALUE[:10])
print(HOURLY_VALUE[:10])
"""


def create_csv(file_name):
    column = ["DATE", "MONTH", "YEAR", "STAR", "QUICK_LOOK", "INDEX", "VERSION",
              "BASE_VALUE", "HOURLY_VALUE", "DAILY_MEAN_VALUE"]
    list_content = list(zip(DATE, MONTH, YEAR, STAR, QUICK_LOOK, INDEX, VERSION, BASE_VALUE,
                            HOURLY_VALUE, DAILY_MEAN_VALUE))
    #print(list_content.shape)
    dataframe = pd.DataFrame(data=list_content, columns=column)
    # Only uncomment to generate dataset
    dataframe.to_csv(file_name, sep=',', index=False)
    print("File generation successful, file %s is generated in your local "
          "directory" % file_name)


fileName = 'DST_DATA.csv'
create_csv(fileName)
