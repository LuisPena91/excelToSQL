import mysql.connector
from excel import sheet_number,sheet_names_excel, column_number,read_excel, df_null_values
from sql import connect_to_database,table_name_sql, table_selection, column_selection, column_name_sql
from menu import menu1


def main():
    #start some variables
    dic_update = {}
    sheet_name = ""
    table_selected = ""
    m = 1
    while m > 0:
        m = menu1()
        if m == 0:
            break
        if m == 1: #first option is to select the sql table
            pos_table = 0
            while pos_table == 0:
                #the system check if in sql table was already selected
                if table_selected:
                    print(f"Table {table_selected} already picked, select the excel table")
                    break
                sql_database = str(input("Data base name: "))
                pos_table = table_selection(sql_database)
                if pos_table == -1:break #the option 0 is to return with out pick a table
                table_selected = table_name_sql(sql_database)[pos_table][0]
                print(f"Table selected: {table_selected}.")
                #if the user already select a sql table and excel sheet, the system will navigate to next step
                if table_selected and sheet_name:
                    m = 3
                break
        if m == 2: #second option is to select the excel sheet
            sheet_excel = 0
            while sheet_excel == 0:
                #the system check if an excel sheet was already selected
                if sheet_name:
                    print(f"Sheet {sheet_name} already picked, select the SQL table")
                    break
                else:
                    excel_file_path = str(input("Document to read: "))
                    sheet_excel = sheet_number(excel_file_path)
                if sheet_excel == -1: #the option 0 is to return with out pick a sheet
                    break    
                #Read excel book and page 
                sheet_name = sheet_names_excel(excel_file_path)[sheet_excel]
                df_excel = read_excel(excel_file_path, sheet_name) #create the data frame (using pandas)
                df_excel = df_null_values(df_excel) #Null values control
                print(f"Sheet selected: {sheet_name}")
                #print(df_excel)
                #if the user already select a sql table and excel sheet, the system will navigate to next step
                if table_selected and sheet_name:
                    m = 3
                    break
        if m == 3: #in this part is the "main" program funtion, is to send the data from excel to SQL
            op = True
            while op:
                while len(dic_update) < len(column_name_sql(sql_database,table_selected)): #here the dic_update is empty
                    column_names = column_name_sql(sql_database,table_selected)
                    #update de dic assigning as a key sql columns and as a value excel sheet columns
                    # the dictionary is to have the key and values in the same position for the follow tuples 
                    for j in range(len(column_names)): 
                        print(f"Select an excel column for the SQL column:  {column_names[j][0]}.")
                        column_n = column_number(df_excel.columns)
                        if column_n == -1: #option 0 to start over
                            dic_update = {}
                            break
                        dic_update[column_names[j][0]] = df_excel.columns[column_n]
                    print("Those are the relations:")
                    for key,value in dic_update.items(): print(f"SQL: {key} --> Excel: {value}")
                    con = int(input(" - To Continue press 1 \n - To Change press 2 \n - : "))
                    if con == 1: op = False 
                    else: dic_update={}
            dic_keys = tuple(dic_update.keys())
            dic_values = tuple(dic_update.values())

            #print("Diccionario=")
            #print(dic_keys)
            #print(dic_values)
            #print(table_selected)

            
            try: #db connection
                connection = connect_to_database(sql_database)
                print("Connection success")
            except mysql.connector.Error as err:
                print('CONNECTION ERROR')
                print(f"Error: {err}")
            cursor = connection.cursor()
            end = False
            updateQ = 0
            insertQ = 0
            for index, row in df_excel.iterrows():
                if end: break
                try: #The PK is being treated as a string, if you want to treat it as an integer, use the commented part bellow
                    cursor.execute(f"SELECT * FROM {table_selected} WHERE {dic_keys[0]} = '{row[dic_values[0]]}'")
                except mysql.connector.Error as err:
                    print(f"Error: {err}")
                    end = True
                #try:
                    #cursor.execute(f"SELECT * FROM {table_selected} WHERE {dic_keys[0]} = {row[dic_values[0]]}")
                #except mysql.connector.Error as err:
                    #print(f"Error: {err}")
                result = cursor.fetchone()
                if result:
                    print(f"For {dic_keys[0]}: {row[dic_values[0]]}: ")
                    for i in range(len(dic_keys)-1): #Here the system iterate on all key columns to update all
                        try:
                            cursor.execute(
                                    f"UPDATE {table_selected} SET {dic_keys[i+1]} = '{row[dic_values[i+1]]}' WHERE {dic_keys[0]} = '{row[dic_values[0]]}'")
                            print(f"-  Updated value = {dic_keys[i+1]} -->  whit the value = {row[dic_values[i+1]]}")
                        except mysql.connector.Error as err:
                            print("UPDATE ERROR")
                            print(f"Error: {err}")
                            end = True
                            break
                    updateQ += 1
                else:
                    #In this section I created a tuple 'row_keys' with an especific format
                    #an empty list 'row_values'
                    #and add values in the list in an especific order to convert the list in a tuple
                    #all this allows me to acces to the values in the proper format to execute the INSERT INTO
                    row_keys = f"({', '.join(dic_update.keys())})"
                    row_values = []
                    for i in range(len(dic_keys)):
                        row_values.append(row[dic_values[i]])
                    row_values = tuple(row_values)
                    #print(row_values)
                    try:
                        cursor.execute(
                        f"INSERT INTO {table_selected} {row_keys} VALUES {row_values} "
                        )
                        print(f"\nInserted values = {row_keys} -->  whit the values = {row_values}")
                        insertQ += 1
                    except mysql.connector.Error as err:
                        print("INSET ERROR")
                        print(f"Error: {err}")
                        end = True   
            #commit changes and close the db
            connection.commit()
            cursor.close()
            connection.close()
            break
    print(f' - Total row Updated: {updateQ}')
    print(f' - Total row Inserted: {insertQ}')
    print('End of the program')
if __name__=="__main__":
    main()