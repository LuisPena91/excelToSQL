import mysql.connector
from menu import menu2

#db credentials
def connect_to_database(sql_database):
    return mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = sql_database
    )
#func to look for the tables who belong to the DB
def table_name_sql(sql_database):
    try:
        connection = connect_to_database(sql_database)
    except mysql.connector.Error as err:
        print('CONNECTION ERROR')
        print(f"Error: {err}")    
    cursor = connection.cursor()
    cursor.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{sql_database}'")
    tables_names = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return tables_names
#func to select a table to update
def table_selection(sql_database):
    print("----Data base Tables----") 
    for j in range(len(table_name_sql(sql_database))):
        print(f" - {j+1}:  {table_name_sql(sql_database)[j][0]}")
    print(" - 0:  Return")
    pos_sql = menu2(j+1)
    return pos_sql -1
#func to look for the columns who belong to the table selected
def column_name_sql(sql_database,table_selected):
    try:
        connection = connect_to_database(sql_database)
    except mysql.connector.Error as err:
        print('CONNECTION ERROR')
        print(f"Error: {err}")
    cursor = connection.cursor()
    cursor.execute(f"""SHOW COLUMNS FROM {table_selected};""")
    column_names = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return column_names
#func to select a calumn to update
def column_selection(sql_database,table_selected):
    print(f"Columns in the SQL table {table_selected}: ")
    for j in range(len(column_name_sql(sql_database,table_selected))):
        print(f"{j+1}:  {column_name_sql(sql_database,table_selected)[j][0]}")
    pos_column = int(input(f'Select a SQL column from {table_selected} to update: '))
    return pos_column-1

