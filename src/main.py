import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from menu import menu
from update_or_insert import users,tasks,checkinout,projects,boxes,productivity
import configparser
#import MySQLdb

#Fun to read the excel book
def read_excel(file_path, sheet_name):
    return pd.read_excel(file_path,sheet_name=sheet_name)

#fun to conect the db
def connect_to_database(host, user, password, database):
    return mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )

#fun to pick a table to update
def switcht_case(pos,cursor, df_excel):
    if pos == 0:
        return users(cursor,df_excel)
    elif pos == 1:
        return tasks(cursor,df_excel)
    elif pos == 2:
        return checkinout(cursor, df_excel)
    elif pos == 3:
        return projects(cursor, df_excel)
    elif pos == 4:
        return boxes(cursor, df_excel)
    elif pos == 5:
        return productivity(cursor, df_excel)

list_excel = [
        'Users',
        'Tasks',
        'CheckInCheckOut',
        'Projects',
        'Boxes',
        'Productivity'
    ]

def main():

    #Read db configutation doc
    #configdb = configparser.ConfigParser()
    #configdb.read('configdb.ini')

    #Db credentials
    db_host = 'localhost'
    db_user = 'root'
    db_password = 'Lfpp0811.*'
    db_name = 'productivity_app'

    pos = 0
    while pos >= 0:
        pos = menu()
        if pos == -1:
            break
        #Read ecxel book and page 
        excel_file_path = 'PRODUCTION_test.xlsx'
        df_excel = pd.read_excel(excel_file_path, sheet_name=list_excel[pos])
        df_excel.fillna(value=0,inplace=True) #add zero on the empty fields
            #print(df_excel)
    
        #db connection
        connection = connect_to_database(db_host,db_user,db_password,db_name)
        cursor = connection.cursor()

        #Update or add table selected
        switcht_case(pos,cursor, df_excel)

        #commint changes and close the db
        connection.commit()
        cursor.close()
        connection.close()

    print('End of the program')
if __name__=="__main__":
    main()