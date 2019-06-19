from tkinter import*

class MainWindow:
	entryWindow=None
	imagesWindow=None
	canvas=None
	images_raw=None
	images_PI=None
	imageWidth=0
	imageHeight=0

	export_page1=None
	export_page2=None

	def Init(rootWindow):
		MainWindow.entryWindow=Frame(rootWindow)
		MainWindow.entryWindow.grid(row=0,column=0,padx=120)

		imageRatio=1.81
		MainWindow.imageWidth=400
		MainWindow.imageHeight=int(MainWindow.imageWidth/imageRatio)
		

		MainWindow.imagesWindow=Frame(rootWindow)
		MainWindow.imagesWindow.grid(row=1,column=0,pady=5)

		#imagesLabelFrame=Frame(MainWindow.imagesWindow)
		#imagesLabelFrame.grid(row=0,column=0)

		#imagesFrame=Frame(MainWindow.imagesWindow)
		#imagesFrame.grid(row=1,column=0)

		#label=Label(imagesLabelFrame,text="Podgląd:",font=('Arial',12,'bold'))
		#label.grid(row=0,column=0,sticky=S)

		MainWindow.export_page1=Label(MainWindow.imagesWindow)
		MainWindow.export_page1.grid(row=1,column=0)

		MainWindow.export_page2=Label(MainWindow.imagesWindow)
		MainWindow.export_page2.grid(row=1,column=1)

		


		
