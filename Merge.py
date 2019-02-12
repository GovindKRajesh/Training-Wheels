import pandas as pd
import sys
prev=pd.DataFrame()
prevLoc=""

def MergeFrame(frame,prev,location):
	iterOn=""
	global prevLoc
	if(prev.empty):
		prev=frame
		frame=None
		prevLoc=location
		return prev
	else:
		for i in list(prev):
			for j in list(frame):
				if(i==j):
					iterOn=i
					break
			if(iterOn!=""):
				break
		try:
			prev=pd.merge(prev,frame,on=iterOn)
			print("Merge Successful for "+prevLoc+" and "+location)
			frame=None
			prevLoc=location
			return prev
		except:
			print("Merge Unsuccessful for "+prevLoc+" and "+location)
			if(iterOn==""):
				print("Reason: Lack of common column to merge on.")
			sys.exit()


paths=raw_input("Enter the paths of two or more files (comma separated): ")
pathList=paths.split(",")
if(len(pathList)<2):
	print("Minimum 2 frames are needed to merge.")
else:
	for location in pathList:
		print("File: "+location)
		parts=location.split(".")
		ext=parts[len(parts)-1]
		if(ext in ("xls","xlsx")):
			try:
				xFile=pd.ExcelFile(location)
				if(len(xFile.sheet_names)>1):
					choice=raw_input("Y -> All sheets, Anything else -> First sheet only: ")
				if(choice=="Y"):
					for x in xFile.sheet_names:
						frame=xFile.parse(x)
						print("Frame built")
						#print(frame)
						prev=MergeFrame(frame,prev,location)
				else:
					frame=pd.read_excel(location)
					print("Frame built")
					#print(frame)
					prev=MergeFrame(frame,prev,location)
			except:
				print("File not found")
				break
		elif(ext in ("csv","txt")):
			try:
				frame=pd.read_csv(location)
				print("Frame built")
				#print(frame)
			except:
				print("File not found")
				break
			prev=MergeFrame(frame,prev,location)
		else:
			print("Unsupported Format")
			break		
	print("The first 10 values of the Merged table are as follows: ")
	print(prev.head(n=10))


