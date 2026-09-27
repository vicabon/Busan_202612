import openpyxl

file_path = "韓國釜山2026年12月住宿評比與比價總表.xlsx"
wb = openpyxl.load_workbook(file_path)

for sname in wb.sheetnames:
    ws = wb[sname]
    # Freeze row 1: frozen row is above row 2
    ws.freeze_panes = 'A2'
    print(f"Sheet {sname}: freeze_panes set to A2")

wb.save(file_path)
print("Excel freeze_panes successfully saved!")
