from PIL import Image, ImageDraw, ImageFont

class Preview:
	def Generate(pdf_exportFile):
		pdfBasicWidth=255
		multiplier=3

		imageRatio=9.0/5.0
		width=multiplier*pdfBasicWidth
		height=int(width/imageRatio)

		logoRatio=1.41
		logoHeight=int(height/2) #int(logoWidth*logoRatio)
		logoWidth=int(width/4.5)

		arial6=ImageFont.truetype('arial.ttf',size=6*multiplier)
		arial8=ImageFont.truetype('arial.ttf',size=8*multiplier)
		arialBold6=ImageFont.truetype('arial_bold.ttf',size=6*multiplier)
		arialBold8=ImageFont.truetype('arial_bold.ttf',size=8*multiplier)

		logo=Image.open('logo.png').resize(size=(logoWidth,logoHeight))

		img1=Image.new('RGB',(width,height),color=(255,255,255))
		p1=ImageDraw.Draw(img1)
		p1.line((width/2,height/8,width/2,7*height/8),fill=0,width=2)
		img1.paste(logo,((width//2-logoWidth)//2,(height-logoHeight)//2))

		fun2MoveVal = 0.0
		if(pdf_exportFile.function2 == ""):
		   fun2MoveVal = 0.2

		black='rgb(0,0,0)'
		textPosX=int(9.0*width/16.0)
		p1.text((textPosX,int((8.0-6.6-0.4)*height/8.0)),pdf_exportFile.name,fill=black,font=arialBold8)
		p1.text((textPosX,int((8.0-6.1-0.4)*height/8.0)),pdf_exportFile.function1,fill=black,font=arial6)
		p1.text((textPosX,int((8.0-5.7-0.4)*height/8.0)),pdf_exportFile.function2,fill=black,font=arial6)
		p1.text((textPosX,int((8.0-4.6-0.4-fun2MoveVal)*height/8.0)),pdf_exportFile.company,fill=black,font=arialBold8)
		p1.text((textPosX,int((8.0-4.1-0.4-fun2MoveVal)*height/8.0)),pdf_exportFile.postal_city,fill=black,font=arial6)
		p1.text((textPosX,int((8.0-3.7-0.4-fun2MoveVal)*height/8.0)),pdf_exportFile.street,fill=black,font=arial6)
		p1.text((textPosX,int((8.0-2.9-0.4-fun2MoveVal)*height/8.0)),pdf_exportFile.stationary,fill=black,font=arial6)
		p1.text((textPosX,int((8.0-2.5-0.4-fun2MoveVal)*height/8.0)),pdf_exportFile.mobile,fill=black,font=arial6)
		p1.text((textPosX,int((8.0-2.1-0.4-fun2MoveVal)*height/8.0)),pdf_exportFile.mail,fill=black,font=arial6)
		p1.text((textPosX,int((8.0-1.0-0.4)*height/8.0)),pdf_exportFile.web,fill=black,font=arialBold6)

		img2=Image.new('RGB',(width,height),color=(255,255,255))
		p2=ImageDraw.Draw(img2)
		p2.line((width/2,height/8,width/2,7*height/8),fill=0,width=2)
		img2.paste(logo,((width//2-logoWidth)//2,(height-logoHeight)//2))

		maxLinesCount=14
		linesCount=len(pdf_exportFile.description)
		if linesCount>maxLinesCount:
			linesCount=maxLinesCount

		textPos_Y=((maxLinesCount-linesCount)/2+1)*0.4*height/8.0+height/8.0

		for textLine in range(linesCount):
			#textObj=doc.beginText()
			#textObj.setTextOrigin(textPos_X,textPos_Y)

			for style in pdf_exportFile.descriptionStyles[textLine]:
				if style[2]==0:
					p2.text((textPosX,int(textPos_Y)),pdf_exportFile.description[textLine][style[0]:style[1]+1],fill=black,font=arial6)
					#textObj.setFont('Arial',6)
					#textObj.textOut(self.description[textLine][style[0]:style[1]+1])
				else:
					p2.text((textPosX,int(textPos_Y)),pdf_exportFile.description[textLine][style[0]:style[1]+1],fill=black,font=arialBold6)
					#textObj.setFont('ArialBold',6)
					#textObj.textOut(self.description[textLine][style[0]:style[1]+1])

			textPos_Y+=0.4*height/8.0

		return [img1,img2]


