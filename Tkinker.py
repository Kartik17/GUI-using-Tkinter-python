import Tkinter as tk
import ttk
from functools import partial
from Tkinter import Menu
import tkMessageBox as mBox
#from Spring_code import Spring
import string
import math
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#fig, axis = plt.subplots(1,1, figsize =(8,4))


LARGE_FONT=("Verdana", 12)

class Spring():
	
	def __init__(self,name,wire_dia,inner_dia,no_of_turns,int_torque,desired_start_angle):
		self.name = name
		self.wire_dia = float(wire_dia)
		self.inner_dia = float(inner_dia)
		self.no_of_turns = float(no_of_turns)
		self.int_torque = int_torque
		self.desired_start_angle = desired_start_angle
		self.torsion()
	def torsion(self):
		self.mean_dia = self.wire_dia + self.inner_dia
		self.spring_index = (self.mean_dia)/(self.wire_dia)
		self.wahl_index = (4*(self.spring_index)**2 - self.spring_index -1)/(4*(self.spring_index**2) - 4*self.spring_index)
		self.iterative_step()
		
	def iterative_step(self):
		self.stress = (32*self.wahl_index*self.int_torque)/(math.pi*(self.wire_dia**3))
		self.start_angle = (64*self.int_torque*self.mean_dia*self.no_of_turns*180.0)/(13500.0*(self.wire_dia**4)*math.pi)
		self.stiffness = self.int_torque*0.1/self.start_angle
		self.end_torque = self.stiffness*(self.start_angle-180.0)*10.0
		
		if self.stress > 80.0:
			print('Increasing the wire diameter by 0.1 millimeters')
			self.wire_dia += 0.1
			self.torsion()
		elif self.start_angle < self.desired_start_angle:
			self.no_of_turns +=1
			self.torsion()
	
	#def write_to_file(self):
		#spring_data = pd.DataFrame({'Name': self.name},columns = ['Name'])

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
		self.geometry('640x480')
		self.menu_bar()
		self.frames = {}
		frame = StartPage(container,self)
		self.frames[StartPage] = frame
		frame.grid(row=0, column = 0, sticky="nsew")
		self.show_frame(StartPage)

	def show_frame(self,cont):
		frame = self.frames[cont]
		frame.tkraise()


class StartPage(tk.Frame):
	def __init__(self,parent,controller):
#Parent represents a widget to act as the parent of the current object. 
#All widgets in tkinter except the root window require a parent.
#controller represents some other object that is designed to act as a common point of interaction for several pages of widgets. It is an attempt to decouple the pages. That is to say, each page doesn't need to know about the other pages. 
#If it wants to interact with another page, such as causing it to be visible, it can ask the controller to make it visible.
		tk.Frame.__init__(self,parent)
	
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
		
		
		buttonCal = tk.Button(self, text="Calculate", command=self.spg_calc).grid(row=20, column=0)

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
		self.stress = spring_1.stress
		self.new_wire_dia = spring_1.wire_dia
		self.spring_index = spring_1.spring_index
		self.wahl_factor = spring_1.wahl_index
		self.stiffness = spring_1.stiffness
		self.start_angle = spring_1.start_angle
		self.new_no_of_turns = spring_1.no_of_turns
		self.output_param()
		
	def layout_plan(self, frames):
		for child in frames:
			child.grid_configure(padx = 6, pady = 6)
			for children in child.winfo_children():
				children.grid_configure(padx = 6, pady = 6)
		
		
app = Spring_Tool()
app.mainloop()