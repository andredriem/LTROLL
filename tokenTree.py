#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Recursive LTROLL interpeter
# God have mercy of our souls
# by: André Driemeyer andredriem@gmail.com

import copy


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


		sentence_expression_flag = 0
		if self.tokens[0] == '$':
			self.tokens.pop(0)
			sentence_expression_flag = 1
			

		return_list = []
		##Pre-expression tokens treatment
		print 'tokens = ' + str(self.tokens)
		final = []
		if self.tokens[0] == 'if':
			return_list =  self.__makeTreeIf__(final,sentence_expression_flag)
		elif self.tokens[0] == 'for':
			return_list = self.__makeTreeFor__(final)
		elif self.tokens[0] == '!':
			self.tokens.pop(0)
			return_list = ['!', self.__makeTree__()]
		elif self.tokens[0] == 'fn':
			return_list = self.__makeTreeFn__(final)
		elif self.tokens[0] == '!':
			return_list = ['!', self.__makeTreeTypeGeneral__(final)]
		elif self.tokens[0] in self.types:
			return_list = self.__makeTreeTypeGeneral__(final)
		elif self.tokens[0] == 'true':
			self.tokens.pop(0)
			return_list = 'true'
		elif self.tokens[0] == 'false':
			self.tokens.pop(0)
			return_list = 'false'
		elif unicode(self.tokens[0]).isnumeric():
			temp = self.tokens.pop(0)
			return_list = temp
		elif self.tokens[0] in self.operators:
			pass		
		else:
			raise Exception('Mal Tipado')
		print 'final = ' + str(return_list)




		##Post-expression tokens treatment
		if sentence_expression_flag == 1: 
			try:
				if self.tokens[0] in self.operators:
					temp = self.tokens.pop(0)
					return [return_list,temp,(self.__makeTree__())]

				else: 
					return return_list
			except IndexError:
				return return_list
		return return_list
		


	def __makeTreeIf__(self,final,sentence_expression_flag):
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


		final.append(self.__makeTree__())

		
		if self.tokens[0] != '->':
			raise Exception('Mal Tipado'+str(final))	
		self.tokens.pop(0)
		final.append('->')

		final.append(self.__makeTree__())
	
		return final

	def __makeTreeTypeGeneral__(self,final):
		final.append(copy.deepcopy(self.tokens[0]))
		self.tokens.pop(0)
		
		try:
			if self.tokens[0] == '-->':
				temp = self.tokens.pop(0)
				return [final,'-->',self.__makeTree__()]
			else:
				return final
		except IndexError:
			return final

		
		



