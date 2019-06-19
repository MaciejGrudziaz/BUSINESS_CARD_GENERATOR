from EntryWindow import EntryWindow
from tkinter import *
from ConfigFile import ConfigFile

class TemplateFile:
	def Read(filename,rootWindow):
		file=None
		error=0

		try:
			file=open(filename,"r")
		except IOError:
			error=1

		if error==0:
			ConfigFile.lastTemplate=filename
			rootWindow.title("Generator wizytówek - "+filename)

			data=file.read()
			data=data.split('\n')
			file.close()

			lineIdx=0
			for line in data:
				if line[:4]=="name":
					val=TemplateFile.GetValue(4,line)
					EntryWindow.name.set(val)
				elif line[:7]=="surname":
					val=TemplateFile.GetValue(7,line)
					EntryWindow.surname.set(val)
				elif line[:9]=="function1":
					val=TemplateFile.GetValue(9,line)
					EntryWindow.function1.set(val)
				elif line[:9]=="function2":
					val=TemplateFile.GetValue(9,line)
					EntryWindow.function2.set(val)
				elif line[:7]=="company":
					val=TemplateFile.GetValue(7,line)
					EntryWindow.company.set(val)
				elif line[:8]=="address1":
					val=TemplateFile.GetValue(8,line)
					EntryWindow.address1.set(val)
				elif line[:8]=="address2":
					val=TemplateFile.GetValue(8,line)
					EntryWindow.address2.set(val)
				elif line[:10]=="stationary":
					val=TemplateFile.GetValue(10,line)
					EntryWindow.stationary.set(val)
				elif line[:6]=="mobile":
					val=TemplateFile.GetValue(6,line)
					EntryWindow.mobile.set(val)
				elif line[:4]=="mail":
					val=TemplateFile.GetValue(4,line)
					EntryWindow.mail.set(val)
				elif line[:3]=="web":
					val=TemplateFile.GetValue(3,line)
					EntryWindow.web.set(val)
				elif line[:11]=="description":
					lineIdx+=1
					descp=[]
					descpStyles=[]
					while data[lineIdx][:17]!="descriptionStyles":
						descp.append(data[lineIdx])
						lineIdx+=1

					if data[lineIdx][:17]=="descriptionStyles":
						lineIdx+=1

						while lineIdx<len(data):
							descpStyles.append([])
							styles=data[lineIdx]
							styles=styles.split(' ')

							for i in range(int(len(styles)/3)):
								singleStyle=[int(styles[i*3+0]),int(styles[i*3+1]),int(styles[i*3+2])]
								descpStyles[-1].append(singleStyle)

							lineIdx+=1

					EntryWindow.LoadDescription(descp,descpStyles)

					break

				lineIdx+=1

		else:
			errorWnd=Toplevel(rootWindow)
			errorWnd.iconbitmap(r'ikona.ico')
			errorLabel=Label(errorWnd,text="Błąd! Nie znaleziono pliku!",font=('Arial',10))
			errorLabel.grid(row=0,column=0,padx=30,pady=30)

		return error

		
	def GetValue(currIdx,line):
		val=""
		while currIdx<len(line):
			if line[currIdx]=='=':
				currIdx+=1
				while currIdx<len(line) and line[currIdx]==' ':
					currIdx+=1
				val=line[currIdx:]
				break
			currIdx+=1

		return val

	def Write(filename,rootWindow):
		ConfigFile.lastTemplate=filename
		rootWindow.title("Generator wizytówek - "+filename)

		file=open(filename,'w')
		file.truncate()

		file.write("name = "+EntryWindow.name.get()+"\n")
		file.write("surname = "+EntryWindow.surname.get()+"\n")
		file.write("function1 = "+EntryWindow.function1.get()+"\n")
		file.write("function2 = "+EntryWindow.function2.get()+"\n")
		file.write("company = "+EntryWindow.company.get()+"\n")
		file.write("address1 = "+EntryWindow.address1.get()+"\n")
		file.write("address2 = "+EntryWindow.address2.get()+"\n")
		file.write("stationary = "+EntryWindow.stationary.get()+"\n")
		file.write("mobile = "+EntryWindow.mobile.get()+"\n")
		file.write("mail = "+EntryWindow.mail.get()+"\n")
		file.write("web = "+EntryWindow.web.get()+"\n")
		file.write("description = \n")
		
		entryDescp=EntryWindow.GetDescription()

		for line in entryDescp[0]:
			file.write(line+'\n')

		file.write("descriptionStyles = \n")

		for line in entryDescp[1]:
			styleStr=""
			for style in line:
				styleStr+=str(style[0])+' '+str(style[1])+' '+str(style[2])+' '
				
			file.write(styleStr+'\n')

		file.close()
