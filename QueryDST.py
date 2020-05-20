import mysql.connector as conn

cnx = conn.connect(user='####', password='####',
                   host='####', database='####')
cursor = cnx.cursor(buffered=True)

#--------------------------------------------------------------------------------#
print('+-------------+--------------+')
print('| Field in DB | Actual Name  |')
print('+-------------+--------------+')
print('| dat         | DATE         |')
print('| mont        | MONTH        |')
print('| yea         | YEAR         |')
print('| star        | STAR         |')
print('| quicklook   | QUICK LOOK   |')
print('| inde        | INDEX        |')
print('| versio      | VERSION      |')
print('| basevalue   | BASEVALUE    |')
print('| hourlyvalue | HOURLY VALUE |')
print('| meanvalue   | MEAN VALUE   |')
print('+-------------+--------------+')
#--------------------------------------------------------------------------------#


print('Please enter the query you want on the DST database - "dstdata"')

query = ''

while True:
    query = input('Enter your query else press "n" or "N" to exit - \n')

    if query == 'n' or query == 'N':
        print('Exiting...........Have a Nice Day')
        break

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print(result, '\n\n')

    except conn.errors.ProgrammingError as err:
        print('The query you entered is wrong - \n', err, '\n\n')
        continue


cnx.commit()

cursor.close()
cnx.close()
