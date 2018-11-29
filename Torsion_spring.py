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
		#self.tk.geometry('400x200+100+200')
		self.torsion_label_frame = ttk.LabelFrame(self, text = 'Torsion Spring')
		self.torsion_label_frame.grid(row=1, column=1,sticky ='nsew')
		#self.torsion_label_frame.geometry()
		print 'Initialize'
		self.torsion_label_frame_1 = ttk.LabelFrame(self.torsion_label_frame, text='Input Parameters')
		self.torsion_label_frame_1.grid(row=0,column=0, sticky = 'nsew')
		self.torsion_label_frame_3 = ttk.LabelFrame(self.torsion_label_frame, text='Output Parameters')
		self.torsion_label_frame_3.grid(row=0,column=2, sticky = 'nsew')
		
		self.torsion_frame_list = [self.torsion_label_frame,self.torsion_label_frame_1,self.torsion_label_frame_3]
		
		self.spring_type = tk.StringVar()
		self.spg_name = tk.StringVar()
		self.wire_dia = tk.DoubleVar()
		self.inner_dia = tk.DoubleVar()
		self.no_of_turns = tk.DoubleVar()
		self.initial_torque = tk.DoubleVar()
		self.desired_angle = tk.DoubleVar()

		self.spg_stress = tk.DoubleVar()
		self.new_wire_dia = tk.DoubleVar()
		self.new_desired_start_angle = tk.DoubleVar()
		self.spring_index = tk.DoubleVar()
		self.wahl_factor = tk.DoubleVar()
		self.start_angle = tk.DoubleVar()
		self.stiffness = tk.DoubleVar()
		self.torque_desired_angle = tk.DoubleVar()
		self.inner_diameter = tk.DoubleVar()
		self.free_length = tk.DoubleVar()
		self.pitch = tk.DoubleVar()
		
		self.input_param()
		self.output_display()

		self.custom_warning = ttk.Style()
		self.custom_warning.configure("EntryStyle_1.TEntry", foreground="red")

		self.no_warning = ttk.Style()
		self.no_warning.configure("EntryStyle_2.TEntry", foreground="black")
				
		button_cal = ttk.Button(self, text="Calculate", command=self.spg_calc, width = 100)
		button_cal.grid(row=20, column=1)
		button_cal.grid_configure(padx = 2, pady = 2)
		
		button_back = ttk.Button(self,text='Main Menu',command=lambda: self.controller.show_frame('StartPage'), width = 100)
		button_back.grid(row = 25, column = 1)
		button_back.grid_configure(padx = 2, pady = 2)
		
		button_reset = ttk.Button(self,text='Reset',command= self.var_reset, width = 100)
		button_reset.grid(row = 30, column = 1)
		button_reset.grid_configure(padx = 2, pady = 2)
		
		button_deployment_dynamics = ttk.Button(self,text= 'Deployment Dynamics', width = 100)
		button_deployment_dynamics.grid(row = 31, column = 1)
		button_deployment_dynamics.grid_configure(padx = 2, pady = 2)
		
	def input_param(self):	
		self.input_frames = [self.torsion_label_frame_1]
		
		
		label_spg_name = ttk.Label(self.torsion_label_frame_1,text = 'Spring Name')
		label_spg_name.grid(row =0, column = 0, sticky = 'w')
		entry_spg_name = ttk.Entry(self.torsion_label_frame_1, textvariable = self.spg_name)
		entry_spg_name.grid(row = 0, column = 1, sticky = 'nsew')
		
		label_wire_dia = tk.Label(self.torsion_label_frame_1, text="Wire diameter(mm)" )
		label_wire_dia.grid(row=1, column=0, sticky = 'w')
		entry_wire_dia = ttk.Combobox(self.torsion_label_frame_1, textvariable = self.wire_dia, state = 'readonly',width =17)
		entry_wire_dia['values'] = (0.60,0.70,0.80,0.90,1.00,1.10,1.20,1.50,1.80,2.00,3.00)
		entry_wire_dia.current(0)
		entry_wire_dia.grid(row=1, column=1)
		
		label_inner_dia = ttk.Label(self.torsion_label_frame_1, text="Inner Diameter(mm)" )
		label_inner_dia.grid(row=2, column=0, sticky = 'w')
		entry_inner_dia = ttk.Entry(self.torsion_label_frame_1, textvariable = self.inner_dia)
		entry_inner_dia.grid(row=2, column=1)
		
		label_no_of_turns = ttk.Label(self.torsion_label_frame_1,text='No of Turns(N)')
		label_no_of_turns.grid(row = 3, column = 0, sticky = 'w')
		entry_no_of_turns = ttk.Entry(self.torsion_label_frame_1,textvariable= self.no_of_turns)
		entry_no_of_turns.grid(row=3, column=1)
		
		label_initial_torque = ttk.Label(self.torsion_label_frame_1, text="Starting Torque(kgf-mm)" )
		label_initial_torque.grid(row=4, column=0, sticky = 'w')
		entryNum1_initial_torque = ttk.Entry(self.torsion_label_frame_1, textvariable = self.initial_torque)
		entryNum1_initial_torque.grid(row=4, column=1)

		label_desired_angle = ttk.Label(self.torsion_label_frame_1, text = 'Angle of Deployment (Degrees)')
		label_desired_angle.grid(row=5, column=0, sticky = 'w')
		entry_desired_angle = ttk.Entry(self.torsion_label_frame_1,textvariable = self.desired_angle)
		entry_desired_angle.grid(row=5,column=1)

		self.layout_plan(self.input_frames)
		
	def output_display(self):
		self.output_frames = [self.torsion_label_frame_3]
		#,self.torsion_label_frame_4
		
		self.label_stress = ttk.Label(self.torsion_label_frame_3,text = 'Bending Stress (kgf/mm2)')
		self.label_stress.grid(row =0, column = 0, sticky = 'w')
		self.entry_stress = ttk.Entry(self.torsion_label_frame_3)
		self.entry_stress.grid(row = 0, column = 1,sticky = 'ew')
		self.entry_stress.configure(state = 'readonly')

		self.label_new_wire_dia = ttk.Label(self.torsion_label_frame_3,text = 'New Wire Diameter (mm)')
		self.label_new_wire_dia.grid(row =1, column = 0, sticky = 'w')
		self.entry_new_wire_dia = ttk.Entry(self.torsion_label_frame_3)
		self.entry_new_wire_dia.grid(row = 1, column = 1,sticky = 'ew')
		self.entry_new_wire_dia.configure(state = 'readonly')
		
		self.label_spring_index = ttk.Label(self.torsion_label_frame_3,text = 'Spring Index')
		self.label_spring_index.grid(row =2, column = 0, sticky = 'w')
		self.entry_spring_index = ttk.Entry(self.torsion_label_frame_3)
		self.entry_spring_index.grid(row = 2, column = 1,sticky = 'ew')
		self.entry_spring_index.configure(state = 'readonly')
		
		self.label_wahl_factor = ttk.Label(self.torsion_label_frame_3,text = 'Wahl Factor')
		self.label_wahl_factor.grid(row =3, column = 0, sticky = 'w')
		self.entry_wahl_factor = ttk.Entry(self.torsion_label_frame_3)
		self.entry_wahl_factor.grid(row = 3, column = 1,sticky = 'ew')
		self.entry_wahl_factor.configure(state = 'readonly')
		
		self.label_stiffness = ttk.Label(self.torsion_label_frame_3,text = 'Torsion Stiffness(kgf-cm/deg)')
		self.label_stiffness.grid(row =4, column = 0, sticky = 'w')
		self.entry_stiffness = ttk.Entry(self.torsion_label_frame_3)
		self.entry_stiffness.grid(row = 4, column = 1,sticky = 'ew')
		self.entry_stiffness.configure(state = 'readonly')
		
		self.label_start_angle = ttk.Label(self.torsion_label_frame_3,text = 'Total Rotation Angle')
		self.label_start_angle.grid(row =5, column = 0, sticky = 'w')
		self.entry_start_angle = ttk.Entry(self.torsion_label_frame_3)
		self.entry_start_angle.grid(row = 5, column = 1,sticky = 'ew')
		self.entry_start_angle.configure(state = 'readonly')
		
		self.label_Torque_180 = ttk.Label(self.torsion_label_frame_3,text = 'Torque at Deployment Angle (kgf-mm) ')
		self.label_Torque_180.grid(row =6, column = 0, sticky = 'w')
		self.entry_Torque_180 = ttk.Entry(self.torsion_label_frame_3)
		self.entry_Torque_180.grid(row = 6, column = 1,sticky = 'ew')
		self.entry_Torque_180.configure(state = 'readonly')
		
		self.label_inner_dia = ttk.Label(self.torsion_label_frame_3,text = 'New Inner Diameter Due To Pre Twist (mm)')
		self.label_inner_dia.grid(row =7, column = 0, sticky = 'w')
		self.entry_inner_dia = ttk.Entry(self.torsion_label_frame_3)
		self.entry_inner_dia.grid(row = 7, column = 1,sticky = 'ew')
		self.entry_inner_dia.configure(state = 'readonly')
		
		self.label_free_length = ttk.Label(self.torsion_label_frame_3,text = 'Free Length of Spring (mm)')
		self.label_free_length.grid(row =8, column = 0, sticky = 'w')
		self.entry_free_length = ttk.Entry(self.torsion_label_frame_3)
		self.entry_free_length.grid(row = 8, column = 1,sticky = 'ew')
		self.entry_free_length.configure(state = 'readonly')
		
		self.label_pitch = ttk.Label(self.torsion_label_frame_3,text = 'Pitch (mm)')
		self.label_pitch.grid(row =9, column = 0, sticky = 'w')
		self.entry_pitch = ttk.Entry(self.torsion_label_frame_3)
		self.entry_pitch.grid(row = 9, column = 1,sticky = 'ew')
		self.entry_pitch.configure(state = 'readonly')

		self.layout_plan(self.output_frames)
		
	def output_param(self):
		#self.F = (self.entry_new_wire_dia,self.entry_spring_index,self.entry_wahl_factor,self.entry_stiffness,self.entry_start_angle,self.entry_Torque_180,self.entry_inner_dia,self.entry_free_length,self.entry_pitch)
		

		self.entry_stress.configure(state = 'normal')
		self.entry_stress.delete(0, 'end')
		if self.spg_stress.get() >= 90.0:
			self.entry_stress.insert(0,self.spg_stress.get())
			self.entry_stress.configure(state = 'readonly',style ="EntryStyle_1.TEntry" )
		else:
			self.entry_stress.insert(0,self.spg_stress.get())
			self.entry_stress.configure(state = 'readonly',style ="EntryStyle_2.TEntry")	

		# for ent in self.F:
		# 	ent.configure(state = 'normal')
		# 	ent.delete(0, 'end')
		# 	ent.insert(0,ent.get())
		# 	ent.configure(state = 'readonly')
		
		self.entry_new_wire_dia.configure(state = 'normal')
		self.entry_new_wire_dia.delete(0, 'end')
		self.entry_new_wire_dia.insert(0,self.new_wire_dia.get())
		self.entry_new_wire_dia.configure(state = 'readonly')

		self.entry_spring_index.configure(state = 'normal')
		self.entry_spring_index.delete(0, 'end')
		self.entry_spring_index.insert(0,self.spring_index.get())
		self.entry_spring_index.configure(state = 'readonly')

		self.entry_wahl_factor.configure(state = 'normal')
		self.entry_wahl_factor.delete(0, 'end')
		self.entry_wahl_factor.insert(0,self.wahl_factor.get())
		self.entry_wahl_factor.configure(state = 'readonly')

		self.entry_stiffness.configure(state = 'normal')
		self.entry_stiffness.delete(0, 'end')
		self.entry_stiffness.insert(0,self.stiffness.get())
		self.entry_stiffness.configure(state = 'readonly')

		self.entry_start_angle.configure(state = 'normal')
		self.entry_start_angle.delete(0, 'end')
		self.entry_start_angle.insert(0,self.start_angle.get())
		self.entry_start_angle.configure(state = 'readonly')

		self.entry_Torque_180.configure(state = 'normal')
		self.entry_Torque_180.delete(0, 'end')
		self.entry_Torque_180.insert(0,self.torque_desired_angle.get())
		self.entry_Torque_180.configure(state = 'readonly')

		self.entry_inner_dia.configure(state = 'normal')
		self.entry_inner_dia.delete(0, 'end')
		self.entry_inner_dia.insert(0,self.inner_diameter.get())
		self.entry_inner_dia.configure(state = 'readonly')

		self.entry_free_length.configure(state = 'normal')
		self.entry_free_length.delete(0, 'end')
		self.entry_free_length.insert(0,self.free_length.get())
		self.entry_free_length.configure(state = 'readonly')

		self.entry_pitch.configure(state = 'normal')
		self.entry_pitch.delete(0, 'end')
		self.entry_pitch.insert(0,self.pitch.get())
		self.entry_pitch.configure(state = 'readonly')	
		
	def output_param_clear(self):	
		self.F = (self.entry_stress,self.entry_new_wire_dia,self.entry_spring_index,self.entry_wahl_factor,self.entry_stiffness,self.entry_start_angle,self.entry_Torque_180,self.entry_inner_dia,self.entry_free_length,self.entry_pitch)
		
		for ent in self.F:
			ent.configure(state = 'normal')
		 	ent.delete(0, 'end')
		 	ent.configure(state = 'readonly')
	
	def spg_calc(self):
		spring_1 = Spring(str(self.spg_name.get()), self.wire_dia.get(),self.inner_dia.get(),self.no_of_turns.get(),self.initial_torque.get(),self.desired_angle.get())
		self.spg_stress.set(round(spring_1.stress,2))
		#print type(self.spg_stress)
		self.new_wire_dia.set(round(spring_1.wire_dia,2))
		self.spring_index.set(round(spring_1.spring_index,2))
		self.wahl_factor.set(round(spring_1.wahl_index,2))
		self.stiffness.set(round(spring_1.stiffness,5))
		self.start_angle.set(round(spring_1.start_angle,3))
		self.torque_desired_angle.set(round(spring_1.end_torque,3))
		self.inner_diameter.set(round(spring_1.inner_dia,2))
		self.free_length.set(round(spring_1.free_length,2))
		self.pitch.set(round(spring_1.pitch,2))
		self.output_param()
	
	def layout_plan(self, frames):
		for child in frames:
			child.grid_configure(padx = 6, pady = 6)
			for children in child.winfo_children():
				children.grid_configure(padx = 6, pady = 6)
	
	def var_reset(self):
	
		self.spg_name.set('Default')
		self.wire_dia.set(0.0)
		self.inner_dia.set(0.0)
		self.no_of_turns.set(0.0)
		self.initial_torque.set(0.0)
		self.desired_angle.set(0.0)
		
		self.output_param_clear()
		
#Avoid calling layout_plan again on reset