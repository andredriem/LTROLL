#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Recursive LTROLL interpeter
# God have mercy of our souls
# by: André Driemeyer andredriem@gmail.com



from tokenTree import TokenTree
import copy

##SmallSter funcionara da seguinte forma:
##Indentifica o tipo do nodo e aplica o step recursivamente


class SmallStep:

	operators = ('+','-','<','>','<=','>=','=','=/=','or','and','not not')
	bools = ('true','false')
	types = ('nat','bool','unit')
	memory = {}

	def __init__(self,tree):
		self.tree = tree

	def makeStep(self):
		optype = self.__detectStepType__()
		if optype == 'e-op1':
			self.__eop1__()
		elif optype == 'e-op2':
			self.__eop2__()
		elif optype == 'e-plus':
			self.__eplus__()
		elif optype == 'e-minus':
			self.__eminus__()
		elif optype == 'e-equal':
			self.__eequal__()
		elif optype == 'e-nequal':
			self.__enequal__()
		elif optype == 'e-less':
			self.__eless__()
		elif optype == 'e-great':
			self.__egreat__()
		elif optype == 'e-lessequal':
			self.__elessequal__()
		elif optype == 'e-greatequal':
			self.__egreatequal__()
		elif optype == 'e-or':
			self.__eor__()
		elif optype == 'e-and':
			self.__eand__()
		elif optype == 'e-if1':
			self.__eif1__()
		elif optype == 'e-if2':
			optype = 'e-if2 or e-if3'
			self.__eif2__()
		elif optype == 'e-for1':
			self.__efor1__()
		elif optype == 'e-for2':
			self.__efor2__()
		elif optype == 'e-for3':
			optype = 'e-for3 or e-for4'
			self.__efor3__()
		elif optype == 'e-assing1':
			self.__eassing1__()
		elif optype == 'e-assing2':
			self.__eassing2__()
		elif optype == 'e-assing3':
			self.__eassing3__()
		elif optype == 'e-derref2':
			self.__ederref2__()
		elif optype == 'e-derref1':
			self.__ederref1__()
		elif optype == 'e-doispontos1':
			self.__edoispontos1__()
		elif optype == 'e-doispontos2':
			self.__edoispontos2__()
		elif optype == 'e-pontoevirgula1':
			self.__epontoevirgula1__()
		elif optype == 'e-pontoevirgula2':
			self.__epontoevirgula2__()
		elif optype == 'e-fn1':
			self.__efn1__()
		elif optype == 'e-fn2':
			self.__efn2__()
		elif optype == 'e-notnot1':
			self.__enotnot1__()
		elif optype == 'e-notnot2':
			self.__enotnot2__()

		print optype


	def __detectStepType__(self):
		print self.tree
		if len(self.tree) == 3 and type(self.tree[0]) == type([]) and self.tree[1] in self.operators:
			return 'e-op1'
		elif len(self.tree) == 3 and type(self.tree[2]) == type([]) and self.tree[1] in self.operators:
			return 'e-op2'
		elif len(self.tree) == 3 and self.tree[1] == '+':
			return 'e-plus'
		elif len(self.tree) == 3 and self.tree[1] == '-':
			return 'e-minus'
		elif len(self.tree) == 3 and self.tree[1] == '=':
			return 'e-equal'
		elif len(self.tree) == 3 and self.tree[1] == '=/=':
			return 'e-nequal'
		elif len(self.tree) == 3 and self.tree[1] == '>':
			return 'e-great'	
		elif len(self.tree) == 3 and self.tree[1] == '<':
			return 'e-less'
		elif len(self.tree) == 3 and self.tree[1] == '>=':
			return 'e-greatequal'
		elif len(self.tree) == 3 and self.tree[1] == '<=':
			return 'e-lessequal'
		elif len(self.tree) == 3 and self.tree[1] == 'or':
			return 'e-or'
		elif len(self.tree) == 3 and self.tree[1] == 'and':
			return 'e-and'
		elif self.tree[0] == 'if' and type(self.tree[1]) == type([]):
			return 'e-if1'
		elif self.tree[0] == 'if':
			return 'e-if2'
		elif self.tree[0] == 'for' and type(self.tree[1]) == type([]):
			return 'e-for1'
		elif self.tree[0] == 'for' and type(self.tree[3]) == type([]):
			return 'e-for2'
		elif self.tree[0] == 'for':
			return 'e-for3' 
		elif self.tree[0] == 'fn' and type(self.tree[1]) == type([]):
			return 'e-fn1' #todo
		elif self.tree[0] == 'fn':
			return 'e-fn2' #todo
		elif self.tree[0] == '!' and type(self.tree[1]) == type([]):
			return 'e-derref2' 
		elif self.tree[0] == '!':
			return 'e-derref1' 
		elif self.tree[1] == ':=' and type(self.tree[0]) == type([]):
			return 'e-assing3'
		elif self.tree[1] == ':=' and type(self.tree[2]) == type([]):
			return 'e-assing2'
		elif self.tree[1] == ':=':
			return 'e-assing1'
		elif self.tree[1] == ':' and type(self.tree[0]) == type([]):
			return 'e-doispontos1'
		elif self.tree[1] == ':':
			return 'e-doispontos2'
		elif self.tree[1] == ';' and type(self.tree[2]) == type([]):
			return 'e-pontoevirgula1'
		elif self.tree[1] == ';':
			return 'e-pontoevirgula2'
		elif self.tree[0] == 'notnot' and type(self.tree[1]) == type([]):
			return 'e-notnot1'
		elif self.tree[0] == 'notnot':
			return 'e-notnot2'
		else:
			return 'error'

	def __eop1__(self):
		newStep = SmallStep(self.tree[0])
		newStep.makeStep()
		self.tree[0] = newStep.tree

	def __eop2__(self):
		newStep = SmallStep(self.tree[2])
		newStep.makeStep()
		self.tree[2] = newStep.tree
	def __eplus__(self):
		if self.tree[0].isdigit() and self.tree[2].isdigit():
			self.tree = str(int(self.tree[0]) - int(self.tree[2]))
			if int(self.tree) <= 0:
				self.tree = '0'
		else:
			raise Exception("Mal Tipado")  
	def __eminus__(self):
		if self.tree[0].isdigit() and self.tree[2].isdigit():
			self.tree = str(int(self.tree[0]) + int(self.tree[2]))
		else:
			raise Exception("Mal Tipado")

	def __eequal__(self):
		if self.tree[0] == self.tree[2]:
			self.tree = 'false'
		else:
			self.tree = 'true'

	def __enequal__(self):
		if self.tree[0] == self.tree[2]:
			self.tree = 'true'
		else:
			self.tree = 'false'
	def __eless__(self):
		if self.tree[0].isdigit() and self.tree[2].isdigit():
			self.tree = str(int(self.tree[0]) > int(self.tree[2])).lower()
		else:
			raise Exception("Mal Tipado")
	def __egreat__(self):
		if self.tree[0].isdigit() and self.tree[2].isdigit():
			self.tree = str(int(self.tree[0]) < int(self.tree[2])).lower()
		else:
			raise Exception("Mal Tipado")
	def __elessequal__(self):
		if self.tree[0].isdigit() and self.tree[2].isdigit():
			self.tree = str(int(self.tree[0]) >= int(self.tree[2])).lower()
		else:
			raise Exception("Mal Tipado")
	def __egreatequal__(self):
		if self.tree[0].isdigit() and self.tree[2].isdigit():
			self.tree = str(int(self.tree[0]) <= int(self.tree[2])).lower()
		else:
			raise Exception("Mal Tipado")
	def __eor__(self):
		if (self.tree[0] in self.bools) and (self.tree[2] in self.bools):
			self.tree = str((self.tree[0]) and bool(self.tree[2])).lower()
		else:
			raise Exception("Mal Tipado")				
	def __eand__(self):
		if (self.tree[0] in self.bools) and (self.tree[2] in self.bools):
			self.tree = str((self.tree[0]) or bool(self.tree[2])).lower()
		else:
			raise Exception("Mal Tipado")
	def __eif1__(self):
		newStep = SmallStep(self.tree[1])
		newStep.makeStep()
		self.tree[1] = newStep.tree
			 
	def __eif2__(self):
		if self.tree[1] == 'false':
			self.tree = self.tree[3]
		elif self.tree[1] == 'true':			
			self.tree = self.tree[5]
		else:
			raise Exception("Mal Tipado")

	def __efor1__(self):
		newStep = SmallStep(self.tree[1])
		newStep.makeStep()
		self.tree[1] = newStep.tree
	def __efor2__(self):
		newStep = SmallStep(self.tree[3])
		newStep.makeStep()
		self.tree[3] = newStep.tree
	def __efor3__(self):
		if self.tree[1].isdigit() and self.tree[3].isdigit():
			if self.tree[1] == self.tree[3]:
				self.tree = self.tree[5]
			else:
				self.tree[3] = [self.tree[3],'+','1']
				self.tree = [copy.deepcopy(self.tree[5]),':',self.tree]
		else:
			raise Exception("Mal Tipado")
	def __eassing3__(self):
		newStep = SmallStep(self.tree[0])
		newStep.makeStep()
		self.tree[0] = newStep.tree
	def __eassing2__(self):
		newStep = SmallStep(self.tree[2])
		newStep.makeStep()
		self.tree[2] = newStep.tree
	def __eassing1__(self):
		self.memory[copy.deepcopy(self.tree[2])] = self.tree[0]
		self.tree = 'skip'
	def __ederref1__(self):
		try:
			self.tree = self.memory[self.tree[1]]
		except:
			raise Exception("Variavel nao esta na memoria")
	def __ederref2__(self):
		newStep = SmallStep(self.tree[1])
		newStep.makeStep()
		self.tree[1] = newStep.tree
	def __edoispontos1__(self):
		newStep = SmallStep(self.tree[0])
		newStep.makeStep()
		self.tree[0] = newStep.tree		
	def __edoispontos2__(self):
		self.tree = self.tree[2]	
	def __epontoevirgula1__(self):
		newStep = SmallStep(self.tree[2])
		newStep.makeStep()
		self.tree[2] = newStep.tree
	def __epontoevirgula2__(self):
		self.tree = self.tree[0]
	def __efn1__(self):
		newStep = SmallStep(self.tree[1])
		newStep.makeStep()
		self.tree[1] = newStep.tree
	def __efn2__(self):	
		self.__replaceInTree__(self.tree[1],self.tree[5])
		self.tree = self.tree[5]
	def __enotnot1__(self):
		newStep = SmallStep(self.tree[1])
		newStep.makeStep()
		self.tree[1] = newStep.tree
	def __enotnot2__(self):
		if self.tree[1] == 'true' or self.tree[1] == 'false':
			self.tree = str(not bool(self.tree[1])).lower() 
	

	def __replaceInTree__(self,element,atree):
		for node in atree:
			
			if type(node) == type([]):
				self.__replaceInTree__(element,node)
			elif 'x' in atree:
				loc = atree.index('x')
				atree[loc] = copy.copy(element)
		
		pass






if __name__ == '__main__':
	tree = TokenTree('notnot $ true and false').tree
	print 'tree: ' + str(tree)
	test = SmallStep(tree)
	raw_input(' ')
	while True:
		test.makeStep()
		print test.tree
		print 'memoria: ' + str(test.memory)
		raw_input(' ')
		if type(test.tree) == type(' '):
			exit()



