from all_lib import *
#from Torsion_spring import *
class StartPage(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		self.controller = controller
		self.parent = parent
		self.initialize()
	def initialize(self):
		buttonCal = tk.Button(self, text="Torsion Spring", command=lambda : self.controller.show_frame('TorsionPage'))
		buttonCal.grid(row=20, column=0)

