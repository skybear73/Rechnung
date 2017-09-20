import csv
with open("Einleseshit.csv", "r", encoding = "utf8") as varibale_Einleseshit:		#Systemebene - Öffnen der Datei 
	csvreader = csv.reader(varibale_Einleseshit, delimiter = ";") 					#Editorebene - Erstellung eines Reader


	
	for i in [0,2,4,6,8,10]:
		print(i)

	for i in csvreader:
		print(i)

