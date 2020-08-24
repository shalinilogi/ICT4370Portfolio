"""
Author: Shalini Logidasan
Date: 8/23/2020
Function: Class to allow User select the JSON file to input. Tkinter library is used. 
"""
from tkinter import *
from tkinter import filedialog

class gui:
	def __init__(self,root):
		
		self.fileName="" #Variable to store the filepath to the JSON file
		
		self.root=root # Variable to store the root window
		
		self.root.title("Load Stock File") #Set the title of the window
		
		self.root.minsize(340,100) #Set the size of the window
		
		# Set the instructions for the User in the User Interface
		caption = StringVar()
		label = Label(self.root,textvariable=caption)
		caption.set('Select the Jason file containing the Stock Details. After verifying the file path, select "Ok" to confirm selection. Select "Exit" to quit.')
		
		#Set button to select the file
		button = Button(self.root, text="Select File", command=lambda:self.file_opener(),font=('bold'))
		button.grid(column=0, row=2,padx=20,pady=20)
		
		#Set button to confrim the selection
		button = Button(self.root, text="Ok", command=lambda:self.close_window(),font=('bold'))
		button.grid(column=0, row=4,padx=10,pady=10)
		
		#Set button to exit the window
		button = Button(self.root, text="Exit", command=lambda:self.exit_window(),font=('bold'))
		button.grid(column=1, row=4,padx=10,pady=10)
		
		
		self.root.mainloop()
		
	def file_opener(self):
		try:
			self.fileName = filedialog.askopenfilename(filetypes=[("text files", "*.json")])
			caption1=StringVar()
			pathLabel = Label(self.root,textvariable=caption1)
			caption1.set(self.fileName)
			pathLabel.grid(column=0, row=3)
		except Exception as ex:
			print('Exception was encoutered '+ex)
	
	def close_window(self):
		try:
			if self.fileName!="":
				self.root.after(0, self.root.destroy)
		except Exception as ex:
			print('Exception was encoutered '+ex)
			
	def exit_window(self):
		try:
			sys.exit(1)
		except Exception as ex:
			print('Exception was encoutered '+ex)
			
if __name__ == '__main__':
    gui()
		
