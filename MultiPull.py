import xlrd
import csv
paths=raw_input("Enter the path of the file (comma separated, if multiple): ")
pathList=paths.split(",")
for loc in pathList:
	print("File: "+loc)
	parts=loc.split(".")
	ext=parts[len(parts)-1]
	if(ext in ("xls","xlsx")):
		try:
			wbook=xlrd.open_workbook(loc)
		except:
			print("File not found")
			break
		sheet_names=wbook.sheet_names()
		NSheets=len(sheet_names)
		for j in range(NSheets):
			sheet=wbook.sheet_by_index(j)
			print("Sheet name: "+sheet.name)
			print("Column names: ")
			for i in range(sheet.ncols):
				a=sheet.cell_value(0,i)
				if(a!=""):
					print(">"+a)
			print("--------------------")
	elif(ext=="csv"):
		fields=[]
		print("Column names: ")
		try:
			with open(loc,'r') as file:
				read=csv.reader(file)
				fields=next(read)
		except:
			print("File not found")
			break
		for f in fields:
			print(">"+f)
		print("--------------------")
	elif(ext=="txt"):
		try:
			tFile=open(loc,"r")
		except:
			print("File not found")
			break
		csvreader=csv.reader(tFile)
		header=csvreader.next()
		print("Column names: ")
		for item in header:
			print(">"+item)
		print("--------------------")
	else:
		print("Unsupported Format")
		print("--------------------")
