from all_lib import *
class Spring():
	
	def __init__(self,name,wire_dia,inner_dia,no_of_turns,int_torque,desired_angle):
		self.name = name
		self.wire_dia = float(wire_dia)
		self.inner_dia = float(inner_dia)
		self.no_of_turns = float(no_of_turns)
		self.int_torque = int_torque
		self.desired_angle = desired_angle
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
		self.end_torque = self.stiffness*(self.start_angle - self.desired_angle)*10.0
		self.delta_inner_diameter = (self.no_of_turns * self.inner_dia)/(self.no_of_turns + (self.start_angle/360.0))
		self.free_length = ((self.no_of_turns - 1)*0.5) + self.no_of_turns*self.wire_dia
		self.pitch = self.free_length/(self.no_of_turns - 1)
		'''
		if self.stress > 90.0:
			print('Increasing the wire diameter by 0.1 millimeters')
			self.wire_dia += 0.1
			self.torsion()'''
		#if self.start_angle <= self.desired_start_angle:
			#print('Increasing the No of Turns by 1')
			#self.no_of_turns +=1
			#self.torsion()
	
	#def write_to_file(self):
		#spring_data = pd.DataFrame({'Name': self.name},columns = ['Name'])
