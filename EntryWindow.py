from MainWindow import MainWindow
from tkinter import *
from PdfExport import PdfExport
from PIL import Image
from PIL import ImageTk
from ConfigFile import ConfigFile
from tkinter import filedialog
import getpass
from GeneratePreview import Preview

class EntryWindow:
	name=""
	surname=""
	function1=""
	function2=""
	company=""
	address1=""
	address2=""
	stationary=""
	mobile=""
	mail=""
	web=""

	description=""
	descriptionBold=0
	descpChangeBoldButton=None
	descriptionBuffer=[]

	generateButton=None
	exportButton=None

	def Init():
		entryValues=Frame(MainWindow.entryWindow)
		entryValues.grid(row=0,column=0)

		entryFrame1=Frame(entryValues)
		entryFrame1.grid(row=0,column=0,sticky=W)

		entryFrame2=Frame(entryValues)
		entryFrame2.grid(row=0,column=1,sticky=W,rowspan=30)

		buttonFrame=Frame(MainWindow.entryWindow)
		buttonFrame.grid(row=1,column=0,pady=20)

		label_name=Label(entryFrame1,text="Imię:")
		label_name.grid(row=0,column=0,padx=30,sticky=W)

		EntryWindow.name=StringVar()
		EntryWindow.name.set("")
		entry_name=Entry(entryFrame1,text=EntryWindow.name,width=40)
		entry_name.grid(row=1,column=0,padx=30,sticky=W)

		label_surname=Label(entryFrame1,text="Nazwisko:")
		label_surname.grid(row=2,column=0,padx=30,sticky=W)

		EntryWindow.surname=StringVar()
		EntryWindow.surname.set("")
		entry_name=Entry(entryFrame1,text=EntryWindow.surname,width=40)
		entry_name.grid(row=3,column=0,padx=30,sticky=W)

		label_function1=Label(entryFrame1,text="Funkcja (pierwsza linia):")
		label_function1.grid(row=4,column=0,padx=30,sticky=W)

		EntryWindow.function1=StringVar()
		EntryWindow.function1.set("")
		entry_function1=Entry(entryFrame1,text=EntryWindow.function1,width=40)
		entry_function1.grid(row=5,column=0,padx=30,sticky=W)

		label_function2=Label(entryFrame1,text="Funkcja (druga linia):")
		label_function2.grid(row=6,column=0,padx=30,sticky=W)

		EntryWindow.function2=StringVar()
		EntryWindow.function2.set("")
		entry_function2=Entry(entryFrame1,text=EntryWindow.function2,width=40)
		entry_function2.grid(row=7,column=0,padx=30,sticky=W)

		label_company=Label(entryFrame1,text="Nazwa firmy:")
		label_company.grid(row=8,column=0,padx=30,sticky=W)

		EntryWindow.company=StringVar()
		EntryWindow.company.set("")
		entry_company=Entry(entryFrame1,text=EntryWindow.company,width=40)
		entry_company.grid(row=9,column=0,padx=30,sticky=W)

		label_address1=Label(entryFrame1,text="Adres (pierwsza linia):")
		label_address1.grid(row=10,column=0,padx=30,sticky=W)

		EntryWindow.address1=StringVar()
		EntryWindow.address1.set("")
		entry_address1=Entry(entryFrame1,text=EntryWindow.address1,width=40)
		entry_address1.grid(row=11,column=0,padx=30,sticky=W)

		label_address2=Label(entryFrame1,text="Adres (druga linia):")
		label_address2.grid(row=12,column=0,padx=30,sticky=W)

		EntryWindow.address2=StringVar()
		EntryWindow.address2.set("")
		entry_address2=Entry(entryFrame1,text=EntryWindow.address2,width=40)
		entry_address2.grid(row=13,column=0,padx=30,sticky=W)

		label_stationary=Label(entryFrame1,text="Numer stacjonarny:")
		label_stationary.grid(row=14,column=0,padx=30,sticky=W)

		EntryWindow.stationary=StringVar()
		EntryWindow.stationary.set("")
		entry_stationary=Entry(entryFrame1,text=EntryWindow.stationary,width=40)
		entry_stationary.grid(row=15,column=0,padx=30,sticky=W)

		label_mobile=Label(entryFrame1,text="Numer komórkowy:")
		label_mobile.grid(row=16,column=0,padx=30,sticky=W)

		EntryWindow.mobile=StringVar()
		EntryWindow.mobile.set("")
		entry_mobile=Entry(entryFrame1,text=EntryWindow.mobile,width=40)
		entry_mobile.grid(row=17,column=0,padx=30,sticky=W)

		label_mail=Label(entryFrame1,text="Adres email:")
		label_mail.grid(row=18,column=0,padx=30,sticky=W)

		EntryWindow.mail=StringVar()
		EntryWindow.mail.set("")
		entry_mail=Entry(entryFrame1,text=EntryWindow.mail,width=40)
		entry_mail.grid(row=19,column=0,padx=30,sticky=W)

		label_web=Label(entryFrame1,text="Adres internetowy:")
		label_web.grid(row=20,column=0,padx=30,sticky=W)

		EntryWindow.web=StringVar()
		EntryWindow.web.set("")
		entry_web=Entry(entryFrame1,text=EntryWindow.web,width=40)
		entry_web.grid(row=21,column=0,padx=30,sticky=W)

		descriptionFrame=Frame(entryFrame2)
		descriptionFrame.grid(row=0,column=0,pady=20,padx=30,sticky=W)

		label_description=Label(descriptionFrame,text="Krótki opis (tył wizytówki):",font=('Arial',10,'bold'))
		label_description.grid(row=0,column=0,sticky=W)

		EntryWindow.description=Text(descriptionFrame,width=30,height=14,font=('Arial',10))
		EntryWindow.description.grid(row=2,column=0,sticky=W)
		EntryWindow.description.tag_configure('normal',font=('Arial',10))
		EntryWindow.description.tag_configure('bold',font=('Arial',10,'bold'))
		EntryWindow.description.tag_add('bold','1.0','1.39')

		textEditFunFrame=Frame(descriptionFrame)
		textEditFunFrame.grid(row=1,column=0,sticky=W)

		EntryWindow.descpChangeBoldButton=Button(textEditFunFrame,text='B',font=('Arial',10,'bold'),command=EntryWindow.ChangeDescriptionBold)
		EntryWindow.descpChangeBoldButton.grid(row=0,column=0,sticky=W,pady=5)

		descpClearButton=Button(textEditFunFrame,text='Wyczyść',font=('Arial',10),command=lambda:EntryWindow.description.delete('1.0',END))
		descpClearButton.grid(row=0,column=1,sticky=W,pady=5,padx=5)

		#buttonsFrame=Frame(entryFrame1)
		#buttonsFrame.grid(row=23,column=0,padx=30,pady=10)

		EntryWindow.generateButton=Button(buttonFrame,width=10,text="Podgląd",command=EntryWindow.Generate)
		EntryWindow.generateButton.grid(row=0,column=0,padx=10)

		EntryWindow.exportButton=Button(buttonFrame,width=10,text="Eksportuj",command=EntryWindow.Export)
		EntryWindow.exportButton.grid(row=0,column=1,padx=10)

	def Generate():
		EntryWindow.generateButton.config(relief='sunken')
		EntryWindow.generateButton.update()

		pdfDescp=EntryWindow.GetDescription()

		export=PdfExport(EntryWindow.name.get()+" "+EntryWindow.surname.get(),EntryWindow.function1.get(),EntryWindow.function2.get(),EntryWindow.company.get(),EntryWindow.address1.get(),EntryWindow.address2.get(),
				   EntryWindow.stationary.get(), EntryWindow.mobile.get(),EntryWindow.mail.get(),EntryWindow.web.get(),pdfDescp[0],pdfDescp[1])

		images_raw=None
		images_raw=Preview.Generate(export)

		if len(images_raw)!=0:
			images_raw[0]=images_raw[0].resize((MainWindow.imageWidth,MainWindow.imageHeight),Image.ANTIALIAS)
			images_raw[1]=images_raw[1].resize((MainWindow.imageWidth,MainWindow.imageHeight),Image.ANTIALIAS)	

			images_PI=[None,None]
			images_PI[0]=ImageTk.PhotoImage(images_raw[0])
			images_PI[1]=ImageTk.PhotoImage(images_raw[1])

			MainWindow.export_page1.config(image=images_PI[0],bg='black')
			MainWindow.export_page1.image=images_PI[0]
			MainWindow.export_page2.config(image=images_PI[1],bg='black')
			MainWindow.export_page2.image=images_PI[1]

		MainWindow.imagesWindow.config(relief=GROOVE,bd=4,bg='black')
		EntryWindow.generateButton.config(relief='raised')
		EntryWindow.generateButton.update()

	def Export():
		EntryWindow.exportButton.config(relief='sunken')
		EntryWindow.exportButton.update()

		dirPath="C:/"
		if ConfigFile.lastExportLoc=="":
			dirPath=EntryWindow.GetStandardPath()
		else:
			dirPath=ConfigFile.lastExportLoc

		filename=filedialog.asksaveasfilename(initialdir=dirPath,title="Eksportuj",defaultextension=".blw",filetypes=(("pdf files","*.pdf"),("all files","*.*")))

		if filename!="":
			idx=filename.rfind('/')
			ConfigFile.lastExportLoc=filename[:idx]

			pdfDescp=EntryWindow.GetDescription()

			export=PdfExport(EntryWindow.name.get()+" "+EntryWindow.surname.get(),EntryWindow.function1.get(),EntryWindow.function2.get(),EntryWindow.company.get(),EntryWindow.address1.get(),EntryWindow.address2.get(),
				   EntryWindow.stationary.get(), EntryWindow.mobile.get(),EntryWindow.mail.get(),EntryWindow.web.get(),pdfDescp[0],pdfDescp[1])

			export.Export(filename)

		EntryWindow.exportButton.config(relief='raised')
		EntryWindow.exportButton.update()


	def GetStandardPath():
		username=getpass.getuser()
		path="C:/Users/"
		path+=username
		path+="/Documents"

		return path

	def GetDescription():
		descpIn=EntryWindow.description.get("1.0",END)
		descpOut=""

		prevIdx=0
		charCount=0
		for idx in range(len(descpIn)):
			charCount+=1
			if descpIn[idx]=='\n' or charCount==31:
				if descpIn[idx]=='\n':
					descpOut+=descpIn[prevIdx:idx]
					prevIdx=idx+1
				else:
					descpOut+=descpIn[prevIdx:idx]
					prevIdx=idx

				descpOut+='\n'

				charCount=0

		while descpOut.rfind('\n')==len(descpOut)-1 and len(descpOut)>0:
			descpOut=descpOut[:-1]

		descpTab=descpOut.split('\n')

		descpStyles=[]
		line_num=0
		for line in descpTab:
			descpStyles.append([[0,0,0]])
			textIdx_line=str(line_num+1)+'.'

			for line_idx in range(len(line)):
				textIdx=textIdx_line+str(line_idx)
				currTag=EntryWindow.description.tag_names(textIdx)

				if 'bold' in currTag:
					if descpStyles[line_num][-1][0]==descpStyles[line_num][-1][1]:
						descpStyles[line_num][-1][1]=line_idx
						descpStyles[line_num][-1][2]=1
					elif descpStyles[line_num][-1][2]==1:
						descpStyles[line_num][-1][1]=line_idx
					else:
						descpStyles[line_num].append([line_idx,line_idx,1])

				else:
					if descpStyles[line_num][-1][0]==descpStyles[line_num][-1][1]:
						descpStyles[line_num][-1][1]=line_idx
						descpStyles[line_num][-1][2]=0
					elif descpStyles[line_num][-1][2]==0:
						descpStyles[line_num][-1][1]=line_idx
					else:
						descpStyles[line_num].append([line_idx,line_idx,0])

			line_num+=1
			
		return [descpTab,descpStyles]

	def LoadDescription(description,descriptionStyles):
		EntryWindow.description.delete('1.0',END)
		for lineIdx in range(len(description)):
			EntryWindow.description.insert(END,description[lineIdx]+'\n')
			
			for style in descriptionStyles[lineIdx]:
				styleBegin=str(lineIdx+1)+"."+str(style[0])
				styleEnd=str(lineIdx+1)+"."+str(style[1]+1)
				if style[2]==0:
					EntryWindow.description.tag_add('normal',styleBegin,styleEnd)
				else:
					EntryWindow.description.tag_add('bold',styleBegin,styleEnd)

	def ChangeDescriptionBold():
		current_tags=EntryWindow.description.tag_names('sel.first')

		if 'bold' in current_tags:
			EntryWindow.description.tag_remove('bold','sel.first','sel.last')
		else:
			EntryWindow.description.tag_add('bold','sel.first','sel.last')

	def ClearAll():
		EntryWindow.name.set("")
		EntryWindow.surname.set("")
		EntryWindow.function1.set("")
		EntryWindow.function2.set("")
		EntryWindow.company.set("")
		EntryWindow.address1.set("")
		EntryWindow.address2.set("")
		EntryWindow.stationary.set("")
		EntryWindow.mobile.set("")
		EntryWindow.mail.set("")
		EntryWindow.web.set("")

		EntryWindow.description.delete('1.0',END)


		
