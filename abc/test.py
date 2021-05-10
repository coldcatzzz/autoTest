import openpyxl as xl

wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet1']

cell_range=['A2','D6']
for cel in cell_range:
    print(cel)

