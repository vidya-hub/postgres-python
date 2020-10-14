import os
import psycopg2


# create new table
def create_new_table():
   print("vidya")

   create_table_query=''' CREATE TABLE vidya
   (ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   PRICE         REAL
   );
   '''
   cursor.execute(create_table_query)
   connection.commit()
   print("table created sucessfully")


# insert data into the table
def insert_data(id,name,price):
   insert_query='''
      INSERT INTO vidya (ID,NAME,PRICE) VALUES (%s,%s,%s)
   '''
   insert_data=(id,name,price) 

   cursor.execute(insert_query,insert_data)
   connection.commit()
   print(cursor.rowcount)
   print("sucessfully saved")

# get data by using id 

def get_table_data(id):
   previous_data_query='''
      select * from vidya where id = %s
   '''
   cursor.execute(previous_data_query,(id,))
   print(cursor.fetchone())



# update data into the table by using id
def update_table(id,name):
   get_data_query='''
      select * from vidya where id = %s
   '''
   cursor.execute(get_data_query,(id,))
   print("previous data")
   print(cursor.fetchone())
   update_data_query='''
      update vidya set NAME= %s where ID = %s
   '''
   cursor.execute(update_data_query,(name,id))
   connection.commit()
   cursor.execute(get_data_query,(id,))
   print("updated data")
   print(cursor.fetchone())


# update data into the table by using id
def delete_table(id):
   get_data_query='''
      select * from vidya
   '''
   cursor.execute(get_data_query)
   print("previous data")
   print(cursor.fetchall())

   delete_data_query='''
      Delete from vidya where ID = %s
   '''
   cursor.execute(delete_data_query,[(id,)])
   cursor.execute(get_data_query)
   connection.commit()
   print("present data")
   print(cursor.fetchall())


# insert multiple rows
def insert_multiple(parameter_list):
   insert_query = '''
      INSERT into vidya (id,name,price) VALUES (%s,%s,%s)
   '''
   cursor.executemany(insert_query,parameter_list)
   connection.commit()
   print(cursor.rowcount)

# update multiple records
def delete_multiple_rows(records):
   get_data_query='''
      select * from vidya
      Order by id
   '''
   cursor.execute(get_data_query)
   print("previous data")
   print(cursor.fetchall())

   delete_data_query='''
      Delete from vidya where ID = %s
   '''
   cursor.executemany(delete_data_query,records)
   cursor.execute(get_data_query)
   connection.commit()
   print("present data")
   print(cursor.fetchall())

# update multiple records
def update_multiple_rows(records):
   get_data_query='''
      select * from vidya
   '''
   cursor.execute(get_data_query)
   print("previous data")
   print(cursor.fetchall())

   update_data_query='''
      update vidya set NAME= %s where ID = %s
   '''
   cursor.executemany(update_data_query,records)
   
   connection.commit()
   print(cursor.rowcount)
   get_data_query='''
      select * from vidya
   '''
   cursor.execute(get_data_query)
   print("present data")
   print(cursor.fetchall())

try:
   connection = psycopg2.connect(user="postgres",
                                    password="mav12345",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")
   cursor=connection.cursor()
   # create_new()
   # insert_data(5,"VidyaNew",30000)
   # update_table(2,"motorola")
   # print(create_table_query)
   # print(connection.get_dsn_parameters())
   # cursor.execute("SELECT version();")
   # print(cursor.fetchone())
   # delete_table(3)
   # update_multiple_rows([("apple",1),("nokia",5),("oneplus",3),("motorola",4),])
   # delete_multiple_rows([(1,),(4,)])
   # insert_multiple([(1,"apple",100000),(3,"poco",10000),(4,"motorola",1000),(6,"realme",100),])



except (Exception, psycopg2.Error) as error :
    if(connection):
      print("Failed to open the database", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
