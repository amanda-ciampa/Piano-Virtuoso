import Tkinter
import tkMessageBox
from PIL import ImageTk, Image

class MainWindow():
	def __init__(self):
		self.window = Tkinter.Tk() # Creates instance of tkinter GUI
		self.window.wm_title("Piano Virtuoso") # Displays a string in title bar
		self.window.iconbitmap("PVicon.ico") # Displays icon in title bar

		self.img = ImageTk.PhotoImage(Image.open("pixelpiano.png")) # Reads in image file
		self.panel = Tkinter.Label(self.window, image = self.img, bg="black") # Creates a new panel with image

		self.start = Tkinter.Button(self.window, text="Start Game", command=self.helloCallBack) # Uses instance of Tkinter created. Creates a button with text 'hello'. When pressed, performs the helloCallBack func.

		self.panel.pack()
		self.start.pack()

	def helloCallBack(self):
		tkMessageBox.showinfo("Hello Python", "Hello World") 
		self.panel.destroy()
		self.start.destroy()

	def hideTitlePicture(self):
		pass

if __name__ == '__main__':

	mw = MainWindow()

	

	
	#mw.panel.pack() # Displays panel with image
	#mw.start.pack() 

	#panel.pack(side = "bottom", fill = "both", expand = "yes")


	mw.window.mainloop()