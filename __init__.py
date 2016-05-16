#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Recursive LTROLL interpeter
# God have mercy of our souls
# by: André Driemeyer andredriem@gmail.com



PROGRAM_STRING = "if true then 1 else 0"




#Detects witch type or expression the string give is;
#for this first version of the project it only determines if the expression is a IF
class Parser:

	def __init__(self,expression):
		self.e = e
		self.type = 'IF'


	def __getType__(self):
		if 'if' == e.split(' ')[0]:
			return 'IF'

	def getType(self):
		if self.type == 'IF':
			return self.__getTypeIF__(self)



	 def __getTypeIF__(self):
		counte = 0
		temp = e.split(' ')
		for stirng int temp:
			if string == 'if':
				counter += 1
			elif string == 'then'


if __name__ == '__main__':
	print PROGRAM_STRING.split(' ')[0]
	
