from openpyxl import Workbook  # Correct import

wb = Workbook()  # Correct way to initialize a new workbook
ws = wb.active

# testdata = [['name', 'city'], ['manish', 'melbourne']]  # Fixed spelling of 'Melbourne'

# for data in testdata:  # Changed loop variable to 'data' (optional improvement)
#     ws.append(data)

# wb.save("demoexcel.xlsx")  # Save after adding all data (outside loop)
# print("Excel file 'demoexcel.xlsx' created successfully!")

for i in range(1,6):
    for j in range(1,6):
        ws.cell(row=i, column=j).value =i+j
wb.save("demoexcel.xlsx")