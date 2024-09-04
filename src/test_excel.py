import pandas as pd

def sheet_names_excel(excel_file_path):
    excel_file = pd.ExcelFile(excel_file_path)
    sheet_names = excel_file.sheet_names
    return sheet_names

def sheet_number(excel_file_path):
    print('----Tables----')
    for i in range(len(sheet_names_excel(excel_file_path))):
        print(f"{i+1}:  {sheet_names_excel(excel_file_path)[i]}")
    print("0.  EXIT")
    sheet_excel = int(input('Select a table to update:'))
    return sheet_excel-1

def column_number(columns):
    print('----Columns----')
    for i in range(len(columns)):
        print(f"{i+1}:  {columns[i]}")
    print("0.  EXIT")
    column = int(input('Select a column: '))
    return column-1

def main():

    sheet_excel = 0
    while sheet_excel >= 0:
        excel_file_path = str(input("Document to read: "))
        sheet_excel = sheet_number(excel_file_path)
        if sheet_excel == -1:
            break
        #Read ecxel book and page 
        
        df_excel = pd.read_excel(excel_file_path, sheet_name = sheet_names_excel(excel_file_path)[sheet_excel])
        df_excel.fillna(value=0,inplace=True) #add zero on the empty fields
        columns = df_excel.columns
        print(f"Column selected: {columns[column_number(columns)]}")



if __name__=="__main__":
    main()