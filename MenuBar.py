from tkinter import *
from FileMenu import FileMenu

class MenuBar:
	menu=None
	def Init(rootWindow):
		FileMenu.Init(rootWindow)

		MenuBar.menu=Menu(rootWindow)
		MenuBar.menu.add_cascade(label="Plik",menu=FileMenu.menu)		

	def GetMenu():
		return MenuBar.menu
