
import sys
import re
from smallStep import SmallStep
from typeSystem import TypeSystem
from tokenTree import TokenTree

def programPreParsing(program):
        program = program.replace('\n',' ')
        program = program.replace(')',' ')
        program = program.replace('(','$')
        program = re.sub(' +',' ',program)
        if program[0] == ' ':
                program = program[1:]
        if program[len(program)-1] == ' ':
                program = program[:-1]
        return program



if __name__ == '__main__':
        if len(sys.argv) != 2:
                print 'argumentos invalidos, o programa agora ira fechar...'
                exit()
        try:
                f = open(sys.argv[1],'r')
        except IOError:
                print 'arquivo inexistente, o programa agora ira fechar...'
        program = f.read()
        program = programPreParsing(program)
        tree = TokenTree(program).tree

        dic = {}
        dic['result'] = ['ref',['nat']]
        dic['quadrado'] = ['ref',[['nat'],'-->',['nat']]]
        dic['rec'] = ['ref',[['nat'],'-->',['nat']]]
        dic['fn1'] = ['ref',[  [['nat'],'-->',['bool']] , '-->' , ['bool'] ]]
        dic['x1'] = ['ref',['nat']]
        dic['x2'] = ['ref',['nat']]
        dic['x3'] = ['ref',['nat']]
        dic['bool1'] = ['ref',['bool']]
        dic['bool2'] = ['ref',['bool']]

        temptree = []
        for x in range(len(dic.keys())):
                temptree.append(dic.keys()[x])
                temptree.append(dic.values()[x])
        
        tree = [temptree,'#',tree]
        print 'foi montada a arvore:'
        print tree
        print '----------------'

        print 'tipo da funcao:'
        final_type = TypeSystem(tree[2],dic).checkType()
        print final_type

        print '---------------'
        print '\n\n'
        print 'agora o programa ira comecar a realizar o small-step'

        smallStep = SmallStep(tree)
	raw_input(' ')
	while True:
		smallStep.makeStep()
                print '-----------------------------'
		print smallStep.tree
		print 'memoria: ' + str(smallStep.memory)
		raw_input(' ')
		if type(smallStep.tree) == type(' ') or smallStep.tree[0] == 'if':
			exit()


#potencia labels : { 'result' : 'nat' , 'quadrado' : ['nat',-->,'nat'] }





























