import mysql.connector

def table_name_sql(sql_database):
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Lfpp0811.*',
        database = sql_database
    )
    cursor = connection.cursor()
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'productivity_app'")
    tables_names = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()
    return tables_names

def menu_sql(sql_database):
    print("Data base Tables: ") 
    for j in range(len(table_name_sql(sql_database))):
        print(f"{j+1}:  {table_name_sql(sql_database)[j][0]}")
    pos_sql = int(input('Select a SQL table to update: '))
    return pos_sql -1

def main():

    sql_database = str(input("Data base name: "))
    pos_sql = menu_sql(sql_database)
    print(f"Table selected: {table_name_sql(sql_database)[pos_sql][0]}")


if __name__=="__main__":
   main()
