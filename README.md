# BUSINESS CARD GENERATOR
Program for generating business cards made in Python, using **tkinter** for graphical interface and **reportlab** for creating **.pdf**
exports of generated business card.

Program is using fixed pattern of business card and the user can only add specific content in earlier appointed places, by using
graphical user interface. User can preview the card layout during creation and export it when it's done. There is also possibility to save
templates, so the program can automatically load certain fields if needed.

**How to build (Windows):**
- you will need following Python extensions: **reportlab**, **Pillow**, **PyInstaller**
- **appdata.bat** script is creating config file in *AppData/Local* directory
- **installer.ps1** script is used to create **.exe** file for Windows from project files
- **arial.ttf**, **arial_bold.ttf**, **ikona.ico**, **logo.png** files should be placed in the same directory as the **.exe** file
