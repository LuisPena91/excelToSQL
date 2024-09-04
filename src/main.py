import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from excel import sheet_number,sheet_names_excel, column_number
from update_or_insert import users,tasks,checkinout,projects,boxes,productivity
from sql import connect_to_database,table_name_sql, table_selection, column_selection, column_name_sql
from menu import menu1
import numpy as np
import configparser
#import MySQLdb

#Func to read the excel book
def read_excel(file_path, sheet_name):
    return pd.read_excel(file_path,sheet_name=sheet_name)

#func to conect the db
#def connect_to_database(host, user, password, database):
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
    dic_update = {}
    sheet_name = ""
    table_selected = ""
    m = 1
    while m > 0:
        m = menu1()
        if m == 0:
            break
        if m == 1:
            pos_table = 0
            while pos_table == 0:
                if table_selected:
                    print(f"Table {table_selected} already picked, select the excel table")
                    break
                sql_database = 'productivity_app' #str(input("Data base name: "))
                pos_table = table_selection(sql_database)
                if pos_table == -1:
                    break
                table_selected = table_name_sql(sql_database)[pos_table][0]
                print(f"Table selected: {table_selected}.")
                if table_selected and sheet_name:
                    m = 3
                break
        if m == 2:
            sheet_excel = 0
            while sheet_excel == 0:
                if sheet_name:
                    print(f"Sheet {sheet_name} already picked, select the SQL table")
                    break
                excel_file_path = "PRODUCTION_test.xlsx" #str(input("Document to read: "))
                sheet_excel = sheet_number(excel_file_path)
                if sheet_excel == -1:
                    break    
                #Read ecxel book and page 
                sheet_name = sheet_names_excel(excel_file_path)[sheet_excel]
                df_excel = pd.read_excel(excel_file_path, sheet_name = sheet_name )
                df_excel.fillna(value=0,inplace=True) #add zero on the empty fields
                print(f"Sheet selected: {sheet_name}")
                    #print(df_excel)
                if table_selected and sheet_name:
                    m = 3
        if m == 3:

            while len(dic_update) < len(column_name_sql(sql_database,table_selected)): 
                pos_column = column_selection(sql_database,table_selected)
                column_selected = column_name_sql(sql_database,table_selected)[pos_column][0]

                columns_excel = df_excel.columns
                excel_column_selected = columns_excel[column_number(columns_excel)]

                if column_selected not in dic_update:
                    dic_update[column_selected] = excel_column_selected
                else:
                    print(f"{column_selected} already asigned to {dic_update[column_selected]}")
            print(dic_update)
            values = list(dic_update.values())
    
            #db connection
            try:
                connection = connect_to_database(sql_database)
            except mysql.connector.Error as err:
                print(f"Error: {err}")

            cursor = connection.cursor()

            #Update or add table selected
            #switcht_case(sheet_excel,cursor, df_excel)
            for index, row in df_excel.iterrows():
                cursor.execute(f"SELECT * FROM {table_selected} WHERE {values[0]} = {row[dic_update[values[0]]]}")
                result = cursor.fetchone()

                if result:
                    print("------*****AQUI VOY*****------")
            #commint changes and close the db
            connection.commit()
            cursor.close()
            connection.close()
            break

    print('End of the program')
if __name__=="__main__":
    main()