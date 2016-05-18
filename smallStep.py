#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Recursive LTROLL interpeter
# God have mercy of our souls
# by: André Driemeyer andredriem@gmail.com



from tokenTree import TokenTree

##SmallSter funcionara da seguinte forma:
##Indentifica o tipo do nodo e aplica o step recursivamente


class SmallStep:

	operators = ('+','-','<','>','<=','>=','=','=/=','or','and','not not', ';', ':', ':=')
	types = ('nat','bool','unit')

	def __init__(self,tree):
		self.tree = tree

	def makeStep(self):
		print 'here'
		if len(self.tree) == 1:
			return self.tree
		print 'here2'
		if self.tree[0] == 'if':
			print self.tree[1]	
			if type(self.tree[1]) == type([]):
				print 'here4'
				temp = SmallStep(self.tree[1])
				temp.makeStep()
				self.tree[1] = temp.tree 
			elif self.tree[1] == 'true':
				if type(self.tree[5]) ==  type([]):
					temp = SmallStep(self.tree[5])
					temp.makeStep()
					self.tree[5] = temp.tree 
				else:
					self.tree = self.tree[5]
			elif self.tree[1] == 'false':
				print 'aqui'
				if type(self.tree[3]) ==  type([]):
					temp = SmallStep(self.tree[3])
					temp.makeStep()
					self.tree[3] = temp.tree 
				else:
					self.tree = self.tree[3]
		print 'here'

		

	






if __name__ == '__main__':
	tree = TokenTree('if if true then true else false then if true then false else true else true').tree
	test = SmallStep(tree)
	print 'new'
	test.makeStep()
	#test.makeStep()
	#test.makeStep()
	
	print test.tree


