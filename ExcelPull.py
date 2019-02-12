import xlrd
import csv
#loc='Downloads/example.xls'
loc=raw_input("Enter the path of the file: ")
parts=loc.split(".")
ext=parts[len(parts)-1]
if(ext in ("xls","xlsx")):
	wbook=xlrd.open_workbook(loc)
	sheet_names=wbook.sheet_names()
	NSheets=len(sheet_names)
	for j in range(NSheets):
		sheet=wbook.sheet_by_index(j)
		print("Sheet name: "+sheet.name)
		print("Column names: ")
		for i in range(sheet.ncols):
			a=sheet.cell_value(0,i)
			if(a!=""):
				print(a)
		print("--------------------")
elif(ext=="csv"):
	fields=[]
	print("Column names: ")
	with open(loc,'r') as file:
		read=csv.reader(file)
		fields=next(read)
	for f in fields:
		print(f)
elif(ext=="txt"):
	tFile=open(loc,"r")
	csvreader=csv.reader(tFile)
	header=csvreader.next()
	print("Column names: ")
	for item in header:
		print(item)
else:
	print("Unsupported Format")
