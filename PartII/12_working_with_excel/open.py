import openpyxl
wb = openpyxl.load_workbook('example3.xlsx')
print(type(wb))

sheet = wb.get_sheet_by_name('Sheet1')
c = sheet['B1']
print(c.value)
print(tuple(sheet['A1' : 'C3']))


for rowOfCellObjects in sheet['A1' : 'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print("--- END OF ROW ---")