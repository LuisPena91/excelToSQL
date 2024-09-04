import mysql.connector

def connect_to_database(sql_database):
    return mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Lfpp0811.*',
        database = sql_database
    )

def table_name_sql(sql_database):
    connection = connect_to_database(sql_database)
    cursor = connection.cursor()
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'productivity_app'")
    tables_names = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()
    return tables_names

def table_selection(sql_database):
    print("Data base Tables: ") 
    for j in range(len(table_name_sql(sql_database))):
        print(f"{j+1}:  {table_name_sql(sql_database)[j][0]}")
    pos_sql = int(input('Select a SQL table to update: '))
    return pos_sql -1

def column_name_sql(sql_database,table_selected):
    connection = connect_to_database(sql_database)
    cursor = connection.cursor()
    cursor.execute(f"""SHOW COLUMNS FROM {table_selected};""")
    column_names = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()
    return column_names

def column_selection(sql_database,table_selected):
    print(f"Columns in the table {table_selected}: ")
    for j in range(len(column_name_sql(sql_database,table_selected))):
        print(f"{j+1}:  {column_name_sql(sql_database,table_selected)[j][0]}")
    pos_column = int(input('Select a column to update: '))
    return pos_column-1


def main():

    dic_update={}
    sql_database = 'timesheet_app' #str(input("Data base name: "))
    pos_sql = table_selection(sql_database)
    table_selected=table_name_sql(sql_database)[pos_sql][0]
    print(f"Table selected: {table_selected}")
    pos_column = column_selection(sql_database,table_selected)
    column_selected = column_name_sql(sql_database,table_selected)[pos_column][0]
    print(f"Column selected: {column_selected}")
    dic_update[column_selected] = "excel selection"
    print(dic_update)

if __name__=="__main__":
   main()
