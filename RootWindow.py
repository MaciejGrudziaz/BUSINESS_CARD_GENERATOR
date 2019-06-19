from tkinter import*
from MainWindow import MainWindow
from MenuBar import MenuBar
from EntryWindow import EntryWindow
from ConfigFile import ConfigFile
from TemplateFile import TemplateFile

class RootWindow:
	root=None

	def Init():
		RootWindow.root=Tk()
		RootWindow.root.title("Generator wizytówek")
		RootWindow.root.iconbitmap(r"ikona.ico")
		
		MainWindow.Init(RootWindow.root)
		EntryWindow.Init()

		ConfigFile.Read(RootWindow.root)

		if ConfigFile.lastTemplate!="":
			error=TemplateFile.Read(ConfigFile.lastTemplate,RootWindow.root)
			if error==1:
				ConfigFile.lastTemplate=""
			RootWindow.newTemp=0

		MenuBar.Init(RootWindow.root)

		RootWindow.root.config(menu=MenuBar.GetMenu())

		RootWindow.root.protocol("WM_DELETE_WINDOW",RootWindow.Close)



	def Run():
		RootWindow.root.mainloop()

	def Close():
		ConfigFile.Write()
		RootWindow.root.destroy()