from all_lib import *
#from Torsion_spring import *
class StartPage(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		self.controller = controller
		self.parent = parent
		self.initialize()
	def initialize(self):
		self.top_label_frame = ttk.LabelFrame(self, text = 'Torsion Spring')
		self.top_label_frame.grid(row=1, column=0)
		
		self.mid_label_frame = ttk.LabelFrame(self, text='Menu')
		self.mid_label_frame.grid(row=2,column=2, sticky = 'ew')
		
		self.bottom_label_frame = ttk.LabelFrame(self, text='Values')
		self.bottom_label_frame.grid(row=3,column=0)
		
		buttonCal = tk.Button(self.mid_label_frame, text="Torsion Spring", command=lambda : self.controller.show_frame('TorsionPage'))
		buttonCal.grid(row=0, column=2,padx = 20,pady = 10)
		
		buttonCal_2 = tk.Button(self.mid_label_frame, text="Material Recommender", command=lambda : self.controller.show_frame('RecommendMaterial'))
		buttonCal_2.grid(row=3, column=2,padx = 20,pady = 10)

