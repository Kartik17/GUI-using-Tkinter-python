from all_lib import *
from Torsion_spring_code import *

class TorsionPage(tk.Frame):
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
		self.torsion_label_frame = ttk.LabelFrame(self, text = 'Torsion Spring')
		self.torsion_label_frame.grid(row=1, column=0)
		
		self.torsion_label_frame_1 = ttk.LabelFrame(self.torsion_label_frame, text='Parameters')
		self.torsion_label_frame_1.grid(row=0,column=0)
		self.torsion_label_frame_2 = ttk.LabelFrame(self.torsion_label_frame, text='Values')
		self.torsion_label_frame_2.grid(row=0,column=1)
		self.torsion_label_frame_3 = ttk.LabelFrame(self.torsion_label_frame, text='Parameters')
		self.torsion_label_frame_3.grid(row=0,column=2)
		self.torsion_label_frame_4 = ttk.LabelFrame(self.torsion_label_frame, text='Values')
		self.torsion_label_frame_4.grid(row=0,column=3)
		
		
		
		self.torsion_frame_list = [self.torsion_label_frame,self.torsion_label_frame_1,self.torsion_label_frame_2,self.torsion_label_frame_3,self.torsion_label_frame_4]
		
		self.spring_type = tk.StringVar()
		self.spg_name = tk.StringVar()
		self.wire_dia = tk.DoubleVar()
		self.inner_dia = tk.DoubleVar()
		self.no_of_turns = tk.DoubleVar()
		self.initial_torque = tk.DoubleVar()
		self.desired_start_angle = tk.DoubleVar()

		self.spg_stress = tk.DoubleVar()
		self.new_wire_dia = tk.DoubleVar()
		self.new_desired_start_angle = tk.DoubleVar()
		self.spring_index = tk.DoubleVar()
		self.wahl_factor = tk.DoubleVar()
		self.start_angle = tk.DoubleVar()
		self.stiffness = tk.DoubleVar()
		
		self.input_param()
		#number1 = tk.StringVar()
		
	def input_param(self):	
		self.input_frames = [self.torsion_label_frame_1,self.torsion_label_frame_2]
		
		
		label_spg_name = ttk.Label(self.torsion_label_frame_1,text = 'Spring Name')
		label_spg_name.grid(row =0, column = 0)
		entry_spg_name = ttk.Entry(self.torsion_label_frame_2, textvariable = self.spg_name)
		entry_spg_name.grid(row = 0, column = 0)
		
		label_wire_dia = ttk.Label(self.torsion_label_frame_1, text="Wire diameter(mm)" )
		label_wire_dia.grid(row=1, column=0)
		entry_wire_dia = ttk.Combobox(self.torsion_label_frame_2, textvariable = self.wire_dia, state = 'readonly',width =17)
		entry_wire_dia['values'] = (0.60,0.70,0.80,0.90,1.00,1.10,1.20)
		entry_wire_dia.current(0)
		entry_wire_dia.grid(row=1, column=0)
		
		label_inner_dia = ttk.Label(self.torsion_label_frame_1, text="Inner Diameter(mm)" )
		label_inner_dia.grid(row=2, column=0)
		entry_inner_dia = ttk.Entry(self.torsion_label_frame_2, textvariable = self.inner_dia)
		entry_inner_dia.grid(row=2, column=0)
		
		label_no_of_turns = ttk.Label(self.torsion_label_frame_1,text='No of Turns')
		label_no_of_turns.grid(row = 3, column = 0)
		entry_no_of_turns = ttk.Entry(self.torsion_label_frame_2,textvariable= self.no_of_turns)
		entry_no_of_turns.grid(row=3, column=0)
		
		label_initial_torque = ttk.Label(self.torsion_label_frame_1, text="Starting Torque(kgf-mm)" )
		label_initial_torque.grid(row=4, column=0)
		entryNum1_initial_torque = ttk.Entry(self.torsion_label_frame_2, textvariable = self.initial_torque)
		entryNum1_initial_torque.grid(row=4, column=0)

		label_desired_start_angle = ttk.Label(self.torsion_label_frame_1, text = 'Desired Starting Angle (Degrees)')
		label_desired_start_angle.grid(row=5, column=0)
		entry_desired_start_angle = ttk.Entry(self.torsion_label_frame_2,textvariable = self.desired_start_angle)
		entry_desired_start_angle.grid(row=5,column=0)
		
		
		buttonCal = tk.Button(self, text="Calculate", command=self.spg_calc)
		buttonCal.grid(row=20, column=0)
		button_back = tk.Button(self,text='Main Menu',command=lambda: self.controller.show_frame('StartPage'))
		button_back.grid(row = 25, column = 0)

		self.layout_plan(self.input_frames)
		
	def output_param(self):	
		# label_spring_type = ttk.Label(self.torsion_label_frame, text="Spring Type ('T' for Torsion/'C' for Compression)" )
		# label_spring_type.grid(row=1, column=0)
		# entry_spring_type = ttk.Entry(self.torsion_label_frame, textvariable = self.spring_type)
		# entry_spring_type.grid(row=1, column=1,sticky = 'ew'
		self.output_frames = [self.torsion_label_frame_3,self.torsion_label_frame_4]
		
		label_stress = ttk.Label(self.torsion_label_frame_3,text = 'Bending Stress')
		label_stress.grid(row =0, column = 0)
		entry_stress = ttk.Entry(self.torsion_label_frame_4)
		entry_stress.insert(0,self.stress)
		entry_stress.grid(row = 0, column = 0)
		
		label_new_wire_dia = ttk.Label(self.torsion_label_frame_3,text = 'New Wire Diameter')
		label_new_wire_dia.grid(row =1, column = 0)
		entry_new_wire_dia = ttk.Entry(self.torsion_label_frame_4)
		entry_new_wire_dia.insert(0,self.new_wire_dia)
		entry_new_wire_dia.grid(row = 1, column = 0)
		
		label_spring_index = ttk.Label(self.torsion_label_frame_3,text = 'Spring Index')
		label_spring_index.grid(row =2, column = 0)
		entry_spring_index = ttk.Entry(self.torsion_label_frame_4)
		entry_spring_index.insert(0,self.spring_index)
		entry_spring_index.grid(row = 2, column = 0)
		
		label_wahl_factor = ttk.Label(self.torsion_label_frame_3,text = 'Wahl Factor')
		label_wahl_factor.grid(row =3, column = 0)
		entry_wahl_factor = ttk.Entry(self.torsion_label_frame_4)
		entry_wahl_factor.insert(0,self.wahl_factor)
		entry_wahl_factor.grid(row = 3, column = 0)
		
		label_stiffness = ttk.Label(self.torsion_label_frame_3,text = 'Torsion Stiffness')
		label_stiffness.grid(row =4, column = 0)
		entry_stiffness = ttk.Entry(self.torsion_label_frame_4)
		entry_stiffness.insert(0,self.stiffness)
		entry_stiffness.grid(row = 4, column = 0)
		
		label_start_angle = ttk.Label(self.torsion_label_frame_3,text = 'Rotation Angle (Start)')
		label_start_angle.grid(row =5, column = 0)
		entry_start_angle = ttk.Entry(self.torsion_label_frame_4)
		entry_start_angle.insert(0,self.start_angle)
		entry_start_angle.grid(row = 5, column = 0)
		
		label_new_no_of_turns = ttk.Label(self.torsion_label_frame_3,text = 'Optimized No. of Turns')
		label_new_no_of_turns.grid(row =6, column = 0)
		entry_new_no_of_turns = ttk.Entry(self.torsion_label_frame_4)
		entry_new_no_of_turns.insert(0,self.new_no_of_turns)
		entry_new_no_of_turns.grid(row = 6, column = 0)		
		
		self.layout_plan(self.output_frames)	
	
	def spg_calc(self):
		spring_1 = Spring(str(self.spg_name.get()), self.wire_dia.get(),self.inner_dia.get(),self.no_of_turns.get(),self.initial_torque.get(),self.desired_start_angle.get())
		self.stress = round(spring_1.stress,2)
		self.new_wire_dia = round(spring_1.wire_dia,2)
		self.spring_index = round(spring_1.spring_index,2)
		self.wahl_factor = round(spring_1.wahl_index,2)
		self.stiffness = round(spring_1.stiffness,5)
		self.start_angle = round(spring_1.start_angle,3)
		self.new_no_of_turns = spring_1.no_of_turns
		self.output_param()
		#round(self.entry.get(), 2)
	def layout_plan(self, frames):
		for child in frames:
			child.grid_configure(padx = 6, pady = 6)
			for children in child.winfo_children():
				children.grid_configure(padx = 6, pady = 6)
