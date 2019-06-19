from tkinter import *
from EntryWindow import EntryWindow
from TemplateFile import TemplateFile
from tkinter import filedialog
from ConfigFile import ConfigFile
import getpass

class FileMenu:
	menu=None
	root=None
	newTemp=0

	def Init(rootWindow):
		if ConfigFile.lastTemplate=="":
			FileMenu.newTemp=1

		FileMenu.menu=Menu(rootWindow,tearoff=0)
		FileMenu.menu.add_command(label="Nowy",command=FileMenu.ClearWindow)
		FileMenu.menu.add_command(label="Zapisz szablon",command=FileMenu.WriteTemplate)
		FileMenu.menu.add_command(label="Zapisz szablon jako",command=FileMenu.WriteAsTemplate)
		FileMenu.menu.add_command(label="Wczytaj szablon",command=FileMenu.ReadTemplate)

		FileMenu.root=rootWindow


	def WriteTemplate():
		if ConfigFile.lastTemplate!="" and FileMenu.newTemp==0:
			TemplateFile.Write(ConfigFile.lastTemplate,FileMenu.root)
			FileMenu.newTemp=0
		else:
			FileMenu.WriteAsTemplate()

	def WriteAsTemplate():
		dirPath="C:/"
		if ConfigFile.lastTemplate=="":
			dirPath=FileMenu.GetStandardPath()
		else:
			dirPath=ConfigFile.lastTemplate
			idx=dirPath.rfind('/')
			dirPath=dirPath[:idx]

		filename=filedialog.asksaveasfilename(initialdir=dirPath,title="Zapisz szablon",defaultextension=".blw",filetypes=(("blw files","*.blw"),("all files","*.*")))

		if filename!="":
			TemplateFile.Write(filename,FileMenu.root)
			FileMenu.newTemp=0

	def ReadTemplate():
		dirPath="C:/"
		if ConfigFile.lastTemplate=="":
			dirPath=FileMenu.GetStandardPath()
		else:
			dirPath=ConfigFile.lastTemplate
			idx=dirPath.rfind('/')
			dirPath=dirPath[:idx]

		filename=filedialog.askopenfilename(initialdir=dirPath,title="Wybierz szablon",defaultextension=".bls",filetypes=(("blw files","*.blw"),("all files","*.*")))

		if filename!="":
			TemplateFile.Read(filename,FileMenu.root)
			FileMenu.newTemp=0

	def GetStandardPath():
		username=getpass.getuser()
		path="C:/Users/"
		path+=username
		path+="/Documents"

		return path

	def ClearWindow():
		EntryWindow.ClearAll()
		FileMenu.root.title("Generator wizytówek")
		FileMenu.newTemp=1
		

