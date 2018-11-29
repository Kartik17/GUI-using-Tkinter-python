from all_lib import *
from Torsion_spring_code import *

class RecommendMaterial(tk.Frame):
	def __init__(self,parent,controller):
#Parent represents a widget to act as the parent of the current object. 
#All widgets in tkinter except the root window require a parent.
#controller represents some other object that is designed to act as a common point of interaction for several pages of widgets. It is an attempt to decouple the pages. That is to say, each page doesn't need to know about the other pages. 
#If it wants to interact with another page, such as causing it to be visible, it can ask the controller to make it visible.
		tk.Frame.__init__(self,parent)
		self.controller = controller
		self.parent = parent
		self.initialize()
	def initialize(self):
		#self.Tk.geometry('400x200+100+200')
		self.recm_label_frame = ttk.LabelFrame(self, text = 'Material Recommender')
		self.recm_label_frame.grid(row=1, column=0)
		print 'Initialize 2'
		self.recm_label_frame_1 = ttk.LabelFrame(self.recm_label_frame, text='Parameters')
		self.recm_label_frame_1.grid(row=0,column=0)
		self.recm_label_frame_2 = ttk.LabelFrame(self.recm_label_frame, text='Values')
		self.recm_label_frame_2.grid(row=0,column=1)
		self.recm_label_frame_3 = ttk.LabelFrame(self.recm_label_frame, text='Parameters')
		self.recm_label_frame_3.grid(row=0,column=2)
		self.recm_label_frame_4 = ttk.LabelFrame(self.recm_label_frame, text='Values')
		self.recm_label_frame_4.grid(row=0,column=3)
		
		
		
		#self.recm_frame_list = [self.recm_label_frame,self.recm_label_frame_1,self.recm_label_frame_2,self.recm_label_frame_3,self.recm_label_frame_4]
		

		self.diameter = tk.DoubleVar()
		self.length = tk.DoubleVar()
		self.material = tk.StringVar()

		self.rec_diameter = tk.DoubleVar()
		self.rec_length = tk.DoubleVar()

		
		self.input_param()
		#number1 = tk.StringVar()
		
	def input_param(self):	
		self.input_frames = [self.recm_label_frame_1,self.recm_label_frame_2]
		
		
		label_Circular_dia = ttk.Label(self.recm_label_frame_1,text = 'Diameter(mm)')
		label_Circular_dia.grid(row =0, column = 0)
		entry_Circular_dia = ttk.Entry(self.recm_label_frame_2, textvariable = self.diameter)
		entry_Circular_dia.grid(row = 0, column = 0)
		
		label_inner_dia = ttk.Label(self.recm_label_frame_1, text="Length(m)" )
		label_inner_dia.grid(row=1, column=0)
		entry_inner_dia = ttk.Entry(self.recm_label_frame_2, textvariable = self.length)
		entry_inner_dia.grid(row=1, column=0)
		
		label_no_of_turns = ttk.Label(self.recm_label_frame_1,text='Material')
		label_no_of_turns.grid(row = 2, column = 0)
		entry_no_of_turns = ttk.Entry(self.recm_label_frame_2,textvariable= self.material)
		entry_no_of_turns.grid(row=2, column=0)
		
		
		buttonCal = tk.Button(self, text="Calculate", command=self.recm_calc)
		buttonCal.grid(row=20, column=0)
		button_back = tk.Button(self,text='Main Menu',command=lambda: self.controller.show_frame('StartPage'))
		button_back.grid(row = 25, column = 0)

		self.layout_plan(self.input_frames)
		
	def output_param(self):	
		# label_spring_type = ttk.Label(self.torsion_label_frame, text="Spring Type ('T' for Torsion/'C' for Compression)" )
		# label_spring_type.grid(row=1, column=0)
		# entry_spring_type = ttk.Entry(self.torsion_label_frame, textvariable = self.spring_type)
		# entry_spring_type.grid(row=1, column=1,sticky = 'ew'
		self.output_frames = [self.recm_label_frame_3,self.recm_label_frame_4]
		
		label_stress = ttk.Label(self.recm_label_frame_3,text = 'Recommended Diameter')
		label_stress.grid(row =0, column = 0)
		entry_stress = ttk.Entry(self.recm_label_frame_4)
		entry_stress.insert(0,self.rec_diameter)
		entry_stress.grid(row = 0, column = 0,sticky = 'ew')
		
		label_new_wire_dia = ttk.Label(self.recm_label_frame_3,text = 'Recommended Length')
		label_new_wire_dia.grid(row =1, column = 0)
		entry_new_wire_dia = ttk.Entry(self.recm_label_frame_4)
		entry_new_wire_dia.insert(0,self.rec_length)
		entry_new_wire_dia.grid(row = 1, column = 0,sticky = 'ew')
		
		
		self.layout_plan(self.output_frames)	
	
	def recm_calc(self):
		self.rec_diameter,self.rec_length = self.reco_mat()
		self.output_param()
		#round(self.entry.get(), 2)
	def layout_plan(self, frames):
		for child in frames:
			child.grid_configure(padx = 6, pady = 6)
			for children in child.winfo_children():
				children.grid_configure(padx = 6, pady = 6)
	def reco_mat(self):
		df = pd.read_csv('test_material.csv')
		a = df[(df.Diameter >= self.diameter.get())&(df.Length >= self.length.get())].sort('Diameter')
		return list(a['Diameter'])[0],list(a['Length'])[0]
		
		