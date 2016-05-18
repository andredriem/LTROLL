#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Recursive LTROLL interpeter
# God have mercy of our souls
# by: André Driemeyer andredriem@gmail.com




#Creates Program Tree
class TokenTree:

	operators = ('+','-','<','>','<=','>=','=','=/=','or','and','not not', ';', ':', ':=')
	types = ('nat','bool','unit')

	def __init__(self,program_string):
		self.program_string = program_string
		self.tokens = self.program_string.split(' ')
		self.tree = self.__makeTree__()
		print self.tree
		

	
	def __makeTree__(self):


		##Pre-expression tokens treatment
		print 'tokens = ' + str(self.tokens)
		final = []
		if self.tokens[0] == 'if':
			return_list =  self.__makeTreeIf__(final)
		elif self.tokens[0] == 'for':
			return_list = self.__makeTreeFor__(final)
		elif self.tokens[0] == '!':
			self.tokens.pop(0)
			return ['!', self.__makeTree__()]
		elif self.tokens[0] == 'fn':
			return_list = self.__makeTreeFn__(final)
		elif self.tokens[0] in self.types:
			return_list = self.__makeTreeType__(final)
		elif self.tokens[0] == 'true':
			self.tokens.pop(0)
			return_list = 'true'
		elif self.tokens[0] == 'false':
			self.tokens.pop(0)
			return_list = 'false'
		elif unicode(self.tokens[0]).isnumeric():
			temp = self.tokens.pop(0)
			return_list = temp			
		else:
			raise Exception('Mal Tipado')
		print 'final = ' + str(return_list)




		##Post-expression tokens treatment
		try:
			if self.tokens[0] in self.operators:
				temp = self.tokens.pop(0)
				return [return_list,temp,(self.__makeTree__())]

			else: 
				return return_list
		except IndexError:
			return return_list
		


	def __makeTreeIf__(self,final):
		final.append('if')
		self.tokens.pop(0)
		final.append(self.__makeTree__())
	
		if self.tokens[0] != 'then':
			raise Exception('Mal Tipado'+str(final))
		self.tokens.pop(0)
		final.append('then')
		final.append(self.__makeTree__())


		if self.tokens[0] != 'else':
			 raise Exception('Mal Tipado')
		self.tokens.pop(0)
		final.append('else')
		final.append(self.__makeTree__())
		return final

	def __makeTreeFor__(self,final):
		final.append('for')
		self.tokens.pop(0)
		final.append(self.__makeTree__())
		if self.tokens[0] != 'until':
			raise Exception('Mal Tipado'+str(final))
		self.tokens.pop(0)
		final.append('until')
		final.append(self.__makeTree__())

		if self.tokens[0] != 'do':
			 raise Exception('Mal Tipado')
		self.tokens.pop(0)
		final.append('do')
		final.append(self.__makeTree__())
		return final

	def __makeTreeFn__(self,final):
		final.append('fn')
		self.tokens.pop(0)
		print 'entrei'

		final.append(self.__makeTree__())

		

		if self.tokens[0] != '/':
			raise Exception('Mal Tipado'+str(final))
		self.tokens.pop(0)
		final.append('/')
		temp = self.tokens.pop(0)
		final.append(self.__makeTree__())

		
		if self.tokens[0] != '->':
			raise Exception('Mal Tipado'+str(final))	
		self.tokens.pop(0)
		final.append('->')

		final.append(self.__makeTree__())
	
		return final

	def __makeTreeType__(self,final):
		

		
		
		
			


if __name__ == '__main__':
	test = TokenTree('if 30 then fn 3 / nat -> true else 0')
	
