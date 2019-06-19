import getpass

class ConfigFile:
	lastTemplate=""
	lastExportLoc=""

	def Read(rootWindow):
		error=0
		file=None

		username=getpass.getuser()
		configFilename="C:/Users/"+username+"/AppData/Local/Wizytowki/config.cfg"

		try:
			file=open(configFilename,"r")
		except IOError:
			error=1

		if error==0:
			data=file.read()
			data=data.split("\n")

			for line in data:
				if line[:16]=="lastTemplateFile":
					ConfigFile.lastTemplate=ConfigFile.GetValue(16,line)
				elif line[:13]=="lastExportLoc":
					ConfigFile.lastExportLoc=ConfigFile.GetValue(13,line)

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

	def Write():
		username=getpass.getuser()
		configFilename="C:/Users/"+username+"/AppData/Local/Wizytowki/config.cfg"

		file=open(configFilename,"w")
		file.truncate()

		file.write("lastTemplateFile = "+ConfigFile.lastTemplate+"\n")
		file.write("lastExportLoc = "+ConfigFile.lastExportLoc+"\n")

		file.close()


