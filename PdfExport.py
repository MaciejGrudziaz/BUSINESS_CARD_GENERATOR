import unicodedata
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Image
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont  
from reportlab.pdfbase.pdfmetrics import stringWidth 

class PdfExport:
	def __init__(self,name,function1,function2,company,address1,address2,stationary,mobile,mail,web,description,descriptionStyles):
		self.name=name
		self.function1=function1
		self.function2=function2
		self.company=company
		self.postal_city=address1
		self.street=address2
		self.stationary=stationary
		self.mobile=mobile
		self.mail=mail
		self.web=web
		self.description=description
		self.descriptionStyles=descriptionStyles

	def Export(self,filename):
		pageWidth=9.0*cm
		pageHeight=5.0*cm

		doc=canvas.Canvas(filename,pagesize=(pageWidth,pageHeight))

		pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
		pdfmetrics.registerFont(TTFont('ArialBold',"arial_bold.ttf"))

		imageRatio=1.41
		imageHeight=pageHeight/2.0 #imageWidth*imageRatio
		imageWidth=pageWidth/4.5

		im=Image("logo.png",imageWidth,imageHeight)
		im.wrapOn(doc,0,0)
		im.drawOn(doc,(pageWidth/2.0-imageWidth)/2.0,(pageHeight-imageHeight)/2.0)

		line=doc.beginPath()
		line.moveTo(pageWidth/2.0,pageHeight/8.0)
		line.lineTo(pageWidth/2.0,7.0*pageHeight/8.0)
		line.close()
		doc.drawPath(line)

		textPos_X=9.0*pageWidth/16.0

		function2MoveVal = 0.0
		if(self.function2 == ""):
			function2MoveVal = 0.2

		textObj=doc.beginText()
		textObj.setTextOrigin(textPos_X,6.6*pageHeight/8.0)
		textObj.setFont("ArialBold",8)
		textObj.textOut(self.name)
		doc.drawText(textObj)

		textObj=doc.beginText()
		textObj.setTextOrigin(textPos_X,6.2*pageHeight/8.0)
		textObj.setFont("Arial",6)
		textObj.textOut(self.function1)
		doc.drawText(textObj)

		textObj=doc.beginText()
		textObj.setTextOrigin(textPos_X,5.8*pageHeight/8.0)
		textObj.setFont("Arial",6)
		textObj.textOut(self.function2)
		doc.drawText(textObj)

		textObj=doc.beginText()
		textObj.setTextOrigin(textPos_X,(4.6+function2MoveVal)*pageHeight/8.0)
		textObj.setFont("ArialBold",8)
		textObj.textOut(self.company)
		doc.drawText(textObj)

		textObj=doc.beginText()
		textObj.setTextOrigin(textPos_X,(4.2+function2MoveVal)*pageHeight/8.0)
		textObj.setFont("Arial",6)
		textObj.textOut(self.postal_city)
		doc.drawText(textObj)

		textObj=doc.beginText()
		textObj.setTextOrigin(textPos_X,(3.8+function2MoveVal)*pageHeight/8.0)
		textObj.setFont("Arial",6)
		textObj.textOut(self.street)
		doc.drawText(textObj)

		textObj=doc.beginText()
		textObj.setTextOrigin(textPos_X,(3.0+function2MoveVal)*pageHeight/8.0)
		textObj.setFont("Arial",6)
		textObj.textOut(self.stationary)
		doc.drawText(textObj)

		textObj=doc.beginText()
		textObj.setTextOrigin(textPos_X,(2.6+function2MoveVal)*pageHeight/8.0)
		textObj.setFont("Arial",6)
		textObj.textOut(self.mobile)
		doc.drawText(textObj)

		textObj=doc.beginText()
		textObj.setTextOrigin(textPos_X,(2.2+function2MoveVal)*pageHeight/8.0)
		textObj.setFont("Arial",6)
		textObj.textOut(self.mail)
		doc.drawText(textObj)

		textObj=doc.beginText()
		textObj.setTextOrigin(textPos_X,1.0*pageHeight/8.0)
		textObj.setFont("ArialBold",6)
		textObj.textOut(self.web)
		doc.drawText(textObj)

		doc.showPage()

		im=Image("logo.png",imageWidth,imageHeight)
		im.wrapOn(doc,0,0)
		im.drawOn(doc,(pageWidth/2.0-imageWidth)/2.0,(pageHeight-imageHeight)/2.0)

		line=doc.beginPath()
		line.moveTo(pageWidth/2.0,pageHeight/8.0)
		line.lineTo(pageWidth/2.0,7.0*pageHeight/8.0)
		line.close()
		doc.drawPath(line)

		maxLinesCount=14
		linesCount=len(self.description)
		if linesCount>maxLinesCount:
			linesCount=maxLinesCount

		textPos_Y=((maxLinesCount-linesCount)/2+linesCount)*0.4*pageHeight/8.0+pageHeight/8.0

		for textLine in range(linesCount):
			textObj=doc.beginText()
			textObj.setTextOrigin(textPos_X,textPos_Y)

			for style in self.descriptionStyles[textLine]:
				if style[2]==0:
					textObj.setFont('Arial',6)
					textObj.textOut(self.description[textLine][style[0]:style[1]+1])
				else:
					textObj.setFont('ArialBold',6)
					textObj.textOut(self.description[textLine][style[0]:style[1]+1])

			#if self.description[textLine][1]==0:
			#   textObj.setFont("Arial",6)
			#elif self.description[textLine][1]==1:
			#	textObj.setFont("ArialBold",6)
			#textObj.textOut(self.description[textLine][0])
			doc.drawText(textObj)

			textPos_Y-=0.4*pageHeight/8.0

		doc.save()

		return doc


