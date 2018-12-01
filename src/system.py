import random
from src.session import *

class System:
	def __init__(self):
		self._session_list = []


	def add_session(self,session):
		self._session_list.append(session)

	def get_session(self,name):
		found = False
		for i in self._session_list:
			if (i.name == name):
				found = True
				return i

		if found == False:
			return False

	def verify_user(self,name,password):
		verify = False
		for i in self._session_list:
			if i.name == name:
				if i.password == password:
					verify = True

		return verify





			

