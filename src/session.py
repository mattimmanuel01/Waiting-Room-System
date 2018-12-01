from flask_login import UserMixin
import random

class session(UserMixin):
	def __init__(self,name,password):
		self._name = name
		self._password = password
		self._numbers = []
		self._dict = {}

	# can cause error if customers waiting > 100
	def get_number(self):
		found = False
		while found == False:
			random_number = random.randint(1,101)
			if random_number not in self._numbers:
				found = True
				self._numbers.append(random_number)
				self._dict[random_number] = 0
				return random_number

	def remove_number(self,number):
		print(self._numbers)
		self._numbers.remove(number)


	def get_list(self):
		return self._numbers

	@property
	def name(self):
		return self._name

	@property
	def password(self):
		return self._password
	
	def set_quantity(self,number,qty):
		for i in self._dict.keys():
			if i == number:
				self._dict[i] = qty

	def get_quantity(self,number):
		return self._dict[number]

	def get_id(self):
		return self._name
	