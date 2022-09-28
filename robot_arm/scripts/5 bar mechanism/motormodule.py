'''
Motor Module Python API
'''
import serial
from struct import *
import time

class MotorModuleController():
	def __init__(self, port):
		try:
			self.ser = serial.Serial(port, timeout = .05)
			self.ser.baudrate = 115200
			self.rx_data = [0, 0, 0, 0, 0, 0]
			self.rx_values_1 = [0, 0, 0, 0]
			self.rx_values_2 = [0, 0, 0, 0]
			self.rx_values_3 = [0, 0, 0, 0]
			self.tx_data = [0, 0, 0, 0, 0, 0, 0, 0, 0]

			print('connected to motor module controller')
		except:
			print('failed to connect to motor module controller')
			pass
	def send_data(self):
		pass
	def send_command(self, id, p_des, v_des, kp, kd, i_ff):
			"""
			send_command(desired position, desired velocity, position gain, velocity gain, feed-forward current)

			Sends data over CAN, reads response, and populates rx_data with the response.
			"""
			id = int(id)
			b = bytes(bytearray([id])) + pack("f", p_des) + pack("f", v_des) + pack("f", kp) + pack("f", kd) + pack("f", i_ff)
			#bytes(bytearray([id]))返回一个字节的字节数组
			#pack("f",p_des)返回四个字节的字节数组-float占4位
			#b总共是1+4*5 = 21个字节的字节数组bytes类
			#print(int.from_bytes(b, byteorder='big'))
			self.ser.write(b)
			#ser.write(b)发送是字节，b是按16进制表示的字节，在发送时，先把16进制转换成对应的ASCII码，串口再根据收到的ASCII值显示对应的字符

			b_rx = self.ser.read(13)#在串口返回的数据包括ID，位置，速度，力矩1+3*4 = 13
			if id==1:
				self.rx_values_1[0] = b_rx[0];					# ID 第一个字节
				self.rx_values_1[1] = unpack('f', b_rx[1:5])		# Position第二三四五个字节
				self.rx_values_1[2] = unpack('f', b_rx[5:9])		# Velocity第6789个字节
				self.rx_values_1[3] = unpack('f', b_rx[9:13])	# Current 第10 11 12 13个字节
			elif id==2:
				self.rx_values_2[0] = b_rx[0];					# ID
				self.rx_values_2[1] = unpack('f', b_rx[1:5])		# Position
				self.rx_values_2[2] = unpack('f', b_rx[5:9])		# Velocity
				self.rx_values_2[3] = unpack('f', b_rx[9:13])	# Current				
			elif id==3:
				self.rx_values_3[0] = b_rx[0];					# ID
				self.rx_values_3[1] = unpack('f', b_rx[1:5])		# Position
				self.rx_values_3[2] = unpack('f', b_rx[5:9])		# Velocity
				self.rx_values_3[3] = unpack('f', b_rx[9:13])	# Current
			else:
				pass

			#print(self.rx_values)
	def enable_motor(self, id):
		"""
		Puts motor with CAN ID "id" into torque-control mode.  2nd red LED will turn on
		"""
		b = b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFC'#bytes类型 共8个字节
		b = b + bytes(bytearray([id])) #加一个ID
		self.ser.write(b)
		#time.sleep(.1)
		#self.ser.flushInput()
	def disable_motor(self, id):
		"""
		Removes motor with CAN ID "id" from torque-control mode.  2nd red LED will turn off
		"""
		b = b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFD'
		b = b + bytes(bytearray([id]))
		self.ser.write(b)
	def zero_motor(self, id):
		"""
		Removes motor with CAN ID "id" from torque-control mode.  2nd red LED will turn off
		"""
		b = b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFE'
		b = b + bytes(bytearray([id]))
		self.ser.write(b)
		# b_rx = self.ser.read(13)
		# if id==1:
		# 	self.rx_values_1[0] = b_rx[0];					# ID
		# 	self.rx_values_1[1] = unpack('f', b_rx[1:5])		# Position
		# 	self.rx_values_1[2] = unpack('f', b_rx[5:9])		# Velocity
		# 	self.rx_values_1[3] = unpack('f', b_rx[9:13])	# Current
		# elif id==2:
		# 	self.rx_values_2[0] = b_rx[0];					# ID
		# 	self.rx_values_2[1] = unpack('f', b_rx[1:5])		# Position
		# 	self.rx_values_2[2] = unpack('f', b_rx[5:9])		# Velocity
		# 	self.rx_values_2[3] = unpack('f', b_rx[9:13])	# Current				
		# elif id==3:
		# 	self.rx_values_3[0] = b_rx[0];					# ID
		# 	self.rx_values_3[1] = unpack('f', b_rx[1:5])		# Position
		# 	self.rx_values_3[2] = unpack('f', b_rx[5:9])		# Velocity
		# 	self.rx_values_3[3] = unpack('f', b_rx[9:13])	# Current
		# else:
		# 	pass


