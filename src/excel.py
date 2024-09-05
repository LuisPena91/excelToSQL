import pandas as pd
#func to list the sheets in the excel book
def sheet_names_excel(excel_file_path):
    excel_file = pd.ExcelFile(excel_file_path)
    sheet_names = excel_file.sheet_names
    return sheet_names
#func to select a sheet
def sheet_number(excel_file_path):
    print('----Excel Tables----')
    for i in range(len(sheet_names_excel(excel_file_path))):
        print(f"{i+1}:  {sheet_names_excel(excel_file_path)[i]}")
    print("0.  Return")
    sheet_excel = int(input('Select a table to update:'))
    return sheet_excel-1
#fun to select a column from the sheet
def column_number(columns):
    print('----Excel Columns----')
    for i in range(len(columns)):
        print(f"{i+1}:  {columns[i]}")
    column = int(input('Select a column: '))
    return column-1