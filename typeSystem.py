#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Recursive LTROLL type checker
# God have mercy of our souls
# by: André Driemeyer andredriem@gmail.com

from tokenTree import TokenTree
import copy

class TypeSystem:

        bools = ('true','false')
        nat_to_nat_op = ('+','-')
        nat_to_bool_op = ('<','>','<=','>=')
        nat_or_bool_to_bool_op = ('=','=/=')
        bool_to_bool_op = ('or','and')

        def __init__(self, tree, variables = {}):
                self.variables = variables
                self.tree = tree
                pass
        def getTree(self):
                return self.tree
        def checkType(self):
                rule = self.__detectTypeRule__()
                #print '------------------------'
                #print rule
                #print self.variables
                #print self.tree
                if rule == 't-int':
                        return self.__tint__()
                elif rule == 't-bool':
                        return self.__tbool__()
                elif rule == 't-skip':
                        return self.__tskip__()
                elif rule == 't-label1':
                        return self.__tlabel1__()
                elif rule == 't-label2':
                        return self.__tlabel2__()
                elif rule == 't-in':
                        return self.__tin__()
                elif rule == 't-fn':
                        return self.__tfn__()
                elif rule == 't-assing':
                        return self.__tassing__()
                elif rule == 't-derref':
                        return self.__tderref__()
                elif rule == 't-pontoevirgula':
                        return self.__tpontoevirgula__()
                elif rule == 't-doispontos':
                        return self.__tdoispontos__()
                elif rule == 't-genbool':
                        return self.__tgenbool__()
                elif rule == 't-natbool':
                        return self.__tnatbool__()
                elif rule == 't-natnat':
                        return self.__tnatnat__()
                elif rule == 't-for':
                        return self.__tfor__()
                elif rule == 't-if':
                        return self.__tif__()



        def __detectTypeRule__(self):
                if type(self.tree) == type('string') and self.tree.isdigit() == True:
                        return 't-int'
                elif type(self.tree) == type('string') and self.tree in self.bools:
                        return 't-bool'
                elif type(self.tree) == type('string') and self.tree == 'skip':
                        return 't-skip'
                elif type(self.tree) == type('string') and self.tree in self.variables:
                        return 't-label1'
                elif type(self.tree) == type('string') and self.tree not in self.variables:
                        return 't-label2'
                elif self.tree[0] == 'fn':
                        return 't-fn'
                elif self.tree[1] == 'in':
                        return 't-in'
                elif self.tree[1] == ':=':
                        return 't-assing'
                elif self.tree[0] == '!':
                        return 't-derref'
                elif self.tree[1] == ';':
                        return 't-pontoevirgula'
                elif self.tree[1] == ':':
                        return 't-doispontos'
                elif self.tree[1] in self.nat_or_bool_to_bool_op:
                        return 't-genbool'
                elif self.tree[1] in self.nat_to_bool_op:
                        return 't-natbool'
                elif self.tree[1] in self.nat_to_nat_op:
                        return 't-natnat'    
                elif self.tree[0] == 'for':
                        return 't-for'
                elif self.tree[0] == 'for':
                        return 't-for'
                elif self.tree[0] == 'if':
                        return 't-if'               



        def __tint__(self):
                return ['nat']
        def __tbool__(self):
                return ['bool']
        def __tskip__(self):
                return ['unit']
        def __tlabel1__(self):
                return self.variables[self.tree]
        def __tlabel2__(self):
                return ['unit']
        def __tfn__(self):
                type_variable = self.tree[3]
                new_variables = copy.deepcopy(self.variables)
                new_variables[self.tree[1]] = type_variable
                type_expression = TypeSystem(self.tree[5],new_variables).checkType()

                return [type_variable,'-->',type_expression]
        def __tin__(self):
                type_function = TypeSystem(self.tree[0],self.variables).checkType()
                type_variable = TypeSystem(self.tree[2],self.variables).checkType()
                if type_function[0] == type_variable:
                        return type_function[2]
                else:
                        raise TypeError("Funcao esta recebendo argumento do "
                                        "tipo: " + str(type_variable) + " enquanto" 
                                        " deveria estar recebendo do tipo: " +
                                        str(type_function[0]))
        def __tassing__(self):
                if self.tree[2] in self.variables:
                        label_type = self.variables[self.tree[2]]
                else:
                        raise TypeError("label '%s' nao declarada"%(self.tree[2]))
                value_type = TypeSystem(self.tree[0],self.variables).checkType()
                
                if label_type == ['unit']:
                        self.variables[self.tree[2]] = ['ref',value_type]
                elif label_type[1] != value_type:
                        raise TypeError("label ja usada antes para outro tipo")
                return ['unit']
        def __tderref__(self):
                if self.tree[1] not in self.variables:
                        print self.variables
                        raise TypeError("label nao foi acossiada a nenhuma variavel anteriormente")
                else:
                        return self.variables[self.tree[1]][1]
        def __tpontoevirgula__(self):
                typeSystemFirst = TypeSystem(self.tree[2],copy.deepcopy(self.variables))
                typeSystemFirst.checkType()
                self.variables = typeSystemFirst.variables
                return TypeSystem(self.tree[0],self.variables).checkType()
        def __tdoispontos__(self):
                typeSystemFirst = TypeSystem(self.tree[0],copy.deepcopy(self.variables))
                typeSystemFirst.checkType()
                self.variables = typeSystemFirst.variables
                return TypeSystem(self.tree[2],self.variables).checkType()
        ##Generalizacao das regras das funcoes == e =/=
        def __tgenbool__(self):
                temp = TypeSystem(self.tree[0],self.variables)
                type_first = temp.checkType()
                type_second = TypeSystem(self.tree[2],temp.variables).checkType()
                if type_first == type_second:
                        return ['bool']
                else:
                        raise TypeError("Tentando comparar 2 tipos diferentes")
        ##Generalizacao das regras das funcoes > < >= <=
        def __tnatbool__(self):
                temp = TypeSystem(self.tree[0],self.variables)
                type_first = temp.checkType()
                type_second = TypeSystem(self.tree[2],temp.variables).checkType()
                if type_first == ['nat'] and type_second == ['nat']:
                        return ['bool']
                else:
                        raise TypeError("Operacao so aceita naturais")
        #Generalizacao das regras das funcoes + - 
        def __tnatnat__(self):
                temp = TypeSystem(self.tree[0],self.variables)
                type_first = temp.checkType()
                type_second = TypeSystem(self.tree[2],temp.variables).checkType()
                if type_first == ['nat'] and type_second == ['nat']:
                        return ['nat']
                else:
                        raise TypeError("Operacao so aceita naturais")         
        def __tfor__(self):
                temp = TypeSystem(self.tree[1],self.variables)
                type_first = temp.checkType()
                temp2 = TypeSystem(self.tree[3],temp.variables)
                type_second = temp2.checkType()
                type_third = TypeSystem(self.tree[5],temp2.variables).checkType()
                if type_first == ['nat'] and type_second == ['nat']:
                        return type_third
                else:
                        raise TypeError("Comparacao do for deve ser feita com naturais")
        def __tif__(self):
                temp = TypeSystem(self.tree[1],self.variables)
                type_first = temp.checkType()
                temp2 = TypeSystem(self.tree[3],temp.variables)
                type_second = temp2.checkType()
                type_third = TypeSystem(self.tree[5],temp2.variables).checkType()
                if type_first == ['bool'] and type_second == type_third:
                        return type_third
                else:
                        raise TypeError("Comparacao do for deve ser feita com naturais")
                               
                



if __name__ == '__main__':
        dic = {}
        #dic['pizza'] = ['ref',['nat']]
	tree = TokenTree('for $ $ 4 := pizza : 3 until $ $ 9 := pizza : 6 do ! pizza').tree
	print 'tree: ' + str(tree)
        test = TypeSystem(tree,dic)
        print test.checkType()
        print test.variables





