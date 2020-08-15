import openpyxl

wb = openpyxl.Workbook()

sheet  = wb.active

sheet.title = "Test_Data_01"

sheet['A1'] = "First_Name"
sheet['B1'] = "Last_Name"

sheet['A2'] = "Gopinath"
sheet['B2'] = "Jayakumar"

wb.save("TestData.xlsx")