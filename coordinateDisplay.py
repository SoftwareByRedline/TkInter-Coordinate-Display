from tkinter import *

mainWindow = Tk()
drawLine = False
dots = 0
lastDotX = 0
lastDotY = 0

mainWindow.title("Coordinate Display for TkInter")

def openCredits():
	credits = Toplevel(mainWindow)
	creditLbl = Label(credits, text = "Made on January 31st by Redline Software, a Redline Network company. Open source software. Free to use, distribute (non-commercially) or modify with proper attribution.")
	creditLbl.pack()


def changeDrawLine():
	#Changes the state of drawLine variable with each button press.
	global drawLine
	if drawLine:
		drawLine = False
	else:
		drawLine = True

def draw_coordinate(eventorigin):
	#draws a cross in the place of each mouse click and writes its coordinates.
	global dots, lastDotX, lastDotY
	pad.create_line(eventorigin.x - 5, eventorigin.y -5, eventorigin.x + 5, eventorigin.y + 5)
	pad.create_line(eventorigin.x +5, eventorigin.y -5, eventorigin.x - 5, eventorigin.y + 5)
	if eventorigin.y < padHeight -20:
		pad.create_text(eventorigin.x, eventorigin.y +10, text = str(eventorigin.x) + " ; " +  str(eventorigin.y), font = "Arial")
	else:
		pad.create_text(eventorigin.x, eventorigin.y -10, text = str(eventorigin.x) + " ; " +  str(eventorigin.y), font = "Arial")
	#This check is here to prevent the text from being out of the canvas.
	

	if drawLine and dots >= 1:
		pad.create_line(lastDotX, lastDotY, eventorigin.x, eventorigin.y)

	lastDotX = eventorigin.x
	lastDotY = eventorigin.y
	dots += 1

	mainWindow.update()

def clearPad():
	global dots
	pad.delete("all")
	dots = 0
	mainWindow.update()

def changeDimensions():
	global padHeight, padWidth
	padHeight = int(heightEntry.get())
	padWidth = int(widthEntry.get())
	pad.config(height = padHeight, width = padWidth)


padHeight = 400
padWidth = 500



pad = Canvas(mainWindow, height = padHeight, width = padWidth, borderwidth = 5, relief = "raised")
pad.pack()

optionBar = Menu(mainWindow)
optionBar.add_command(label = "Draw Line", command = changeDrawLine)
optionBar.add_command(label = "Clear", command = clearPad)
optionBar.add_command(label = "Credits", command = openCredits)

mainWindow.config(menu = optionBar)

widthEntry = Entry(mainWindow)
heightEntry = Entry(mainWindow)
changeBtn = Button(mainWindow, text = "Change", command = changeDimensions)

widthLbl = Label(mainWindow, text = "Width")
heightLbl = Label(mainWindow, text = "Height")

widthLbl.pack()
widthEntry.pack()
heightLbl.pack()
heightEntry.pack()
changeBtn.pack()

pad.bind("<ButtonPress>", draw_coordinate)


mainloop()

