import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from menu import sheet_number,sheet_names_excel
from update_or_insert import users,tasks,checkinout,projects,boxes,productivity
import configparser
#import MySQLdb

#Func to read the excel book
def read_excel(file_path, sheet_name):
    return pd.read_excel(file_path,sheet_name=sheet_name)

#func to conect the db
def connect_to_database(host, user, password, database):
    return mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )

#func to pick a table to update
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


def main():

    #Db credentials
    db_host = 'localhost'
    db_user = 'root'
    db_password = 'Lfpp0811.*'
    db_name = 'productivity_app'

    sheet_excel = 0
    while sheet_excel >= 0:
        excel_file_path = str(input("Document to read: "))
        sheet_excel = sheet_number(excel_file_path)
        if sheet_excel == -1:
            break
        #Read ecxel book and page 
        
        df_excel = pd.read_excel(excel_file_path, sheet_name = sheet_names_excel(excel_file_path)[sheet_excel])
        df_excel.fillna(value=0,inplace=True) #add zero on the empty fields
            #print(df_excel)
    
        #db connection
        try:
            connection = connect_to_database(db_host,db_user,db_password,db_name)
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        cursor = connection.cursor()

        #Update or add table selected
        switcht_case(sheet_excel,cursor, df_excel)

        #commint changes and close the db
        connection.commit()
        cursor.close()
        connection.close()

    print('End of the program')
if __name__=="__main__":
    main()