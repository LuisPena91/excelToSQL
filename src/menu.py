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

