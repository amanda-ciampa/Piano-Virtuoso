import Tkinter
import tkMessageBox
from PIL import ImageTk, Image

class MainWindow():
	def __init__(self):
		self.window = Tkinter.Tk() # Creates instance of tkinter GUI
		self.window.wm_title("Piano Virtuoso") # Displays a string in title bar
		self.window.iconbitmap("PVicon.ico") # Displays icon in title bar

		#self.mainFrame = Tkinter.Frame(self.window, height = 600, width = 600)

		self.img = ImageTk.PhotoImage(Image.open("pixelpiano2.png")) # Reads in image file
		self.titlePanel = Tkinter.Label(self.window, image = self.img, height = 420, width = 450) # Creates a new panel with image

		self.start = Tkinter.Button(self.window, text="Start", command=self.close_title_panel, bd=5, height=1, fg="red", bg="black", width=8) # Uses instance of Tkinter created. Creates a button with text 'hello'. When pressed, performs the close_title_panel func.
		self.exit = Tkinter.Button(self.window, text="Exit", command=self.exit_game, bd=5, fg="red", bg="black", height=1, width=8)

		# self.text = Tkinter.Label(self.window, text="testing!!") # To add text to GUI
		# self.text.pack()

		#self.mainFrame.pack()
		self.titlePanel.pack()
		self.start.pack(padx=5, pady=5)

		self.exit.pack(padx=5, pady=5)

	def close_title_panel(self):
		#tkMessageBox.showinfo("Hello Python", "Hello World") 
		self.titlePanel.destroy()
		self.start.destroy()
		self.exit.destroy()

		self.img2 = ImageTk.PhotoImage(Image.open("dugtrio.png"))
		self.main_menu_panel = Tkinter.Label(self.window, image= self.img2, bg="black",  height = 420, width = 450)
		self.main_menu_panel.pack()

	def exit_game(self):
		exit()
	

if __name__ == '__main__':

	mw = MainWindow()

	#mw.panel.pack() # Displays panel with image
	#mw.start.pack() 

	#panel.pack(side = "bottom", fill = "both", expand = "yes")


	mw.window.mainloop()