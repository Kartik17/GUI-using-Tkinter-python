from all_lib import *
from start_page import *
from Torsion_spring import *
from Recommend_Mat import *

#fig, axis = plt.subplots(1,1, figsize =(8,4))

def _msgBox():
	mBox.showinfo('Torsion Spring Calculator', 'A Python Torsion spring calculator GUI created using tkinter:\nBy Kartik.')

class Spring_Tool(tk.Tk):
	def __init__(self,*args,**kwargs):
		tk.Tk.__init__(self,*args,**kwargs)
		tk.Tk.wm_title(self,'SMG ToolBox')
		self.initialize()
	
	def menu_bar(self):
		menubar = Menu(self)
		self.config(menu = menubar)
		filemenu = Menu(menubar,tearoff =0)
		filemenu.add_command(label = 'New')
		filemenu.add_command(label = 'Exit')
		menubar.add_cascade(label = 'File', menu = filemenu)
		
		helpMenu = Menu(menubar, tearoff = 0)
		helpMenu.add_command(label='About', command = _msgBox)
		menubar.add_cascade(label = 'Help',menu = helpMenu)

	def initialize(self):
		container = ttk.Frame(self)
		container.pack(side="top", fill="both", expand = True)
		container.grid_rowconfigure(1, weight=10)
		container.grid_columnconfigure(1, weight=10)
		self.geometry('800x600')
		self.menu_bar()
		self.frames = {}
		all_frame = (StartPage,TorsionPage, RecommendMaterial)
		for F in all_frame:
			pagename = F.__name__
			frame = F(container,self)
			self.frames[pagename] = frame
			frame.grid(row=0, column = 0, sticky="nsew")
		self.show_frame('StartPage')

	def show_frame(self,cont):
		frame = self.frames[cont]
		frame.tkraise()


		
if __name__ == '__main__':		
	app = Spring_Tool()
	app.mainloop()
	app.resizable(width = False, height = False)

#round(self.entry.get(), 2)