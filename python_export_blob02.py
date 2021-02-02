import mysql.connector
from mysql.connector import Error

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
try:
    connection = mysql.connector.connect(host='192.168.2.5',
                                             database='hos',
                                             user='sa',
                                             password='[hkos,uj')
    cursor = connection.cursor()
    sql_fetch_blob_query = """select dp.icode,d.`name` as drugname,dp.image1
        from drugitems_picture dp
        left outer join drugitems d on d.icode = dp.icode
        where dp.image1 is not null and
        dp.icode in (select icode from drugitems where istatus = 'Y')"""

    cursor.execute(sql_fetch_blob_query)
    record = cursor.fetchall()
    for row in record:
        print("icode = ", row[0], )
        print("drugname = ", row[1])
        drugName = row[1].replace("/", "-")
        drugName = drugName.replace("*", "-")        
        drugPicture = row[2]
        write_file(drugPicture, "[Y]"+row[0]+"-"+drugName+""".jpg""")

except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))        

finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")        
