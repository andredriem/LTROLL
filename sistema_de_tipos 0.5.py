#- * - coding: UTF - 8 -*-

import sys
import copy

sys.setrecursionlimit(2000)

lista_simbolos_operacao = ['+', '-']
lista_simbolos_comparacao = ['=', '>', '<', '>=', '<=']
lista_operadores_logicos = ['and', 'or']
lista_booleanos = ['true', 'false']

memoria = {


    3000:'v',

    }


def verificador_bem_tipada(expressao_simples):
    exp = expressao_simples

## tratamento de expressões compostas, é usado lista pra ilustrar.
    if (type(exp[0]) == list):
        exp_aux = copy.deepcopy(exp)
        del exp_aux[0]
        return verificador_bem_tipada([verificador_bem_tipada(exp[0]), exp_aux[0], exp_aux[1]])
    elif (len(exp) > 2) and (type(exp[2]) == list):
        exp_aux = copy.deepcopy(exp)
        del exp_aux[-1]
        return verificador_bem_tipada([exp[0], exp[1], verificador_bem_tipada(exp[2])])

## verifica se há algum erro explicito na expressao
    if (exp[0] == "error"):
        return "error"
    elif (len(exp) > 3) and (exp[2] == "error"):
            return "error"
    elif (len(exp) > 2) and (exp[1] == "error"):
            return "error"

    elif (((type(exp[0])==int) and (exp[0]>=0)) and (len(exp) == 1)):
        return "int"

    elif ((exp[0] in lista_booleanos) and (len(exp) == 1)) or (exp[0] == "bool"):
        return "bool"

    elif (exp[0] == "skip"):
        return "skip"

    elif (exp[0] in lista_booleanos) and (len(exp) == 1):
        return "bool"

    elif (exp[0] in lista_operadores_logicos): ## retorna false se começar com and ou or
        return "false"

    elif (exp[0] in lista_simbolos_comparacao):
        return "false"

    elif (exp[0] in lista_simbolos_operacao):
        return "false"


    elif (exp[0] == 'fn'):
        if len(exp) == 2:
            return "error"
        if (type(exp[1]) != list):
            if (type(exp[2]) != list):
                if (verificador_bem_tipada([exp[1]]) != "error") and (verificador_bem_tipada([exp[2]]) != "error"):
                    return "fn"
                else:
                    return "error"
            else:
                if (verificador_bem_tipada([exp[1]]) != "error") and (verificador_bem_tipada(exp[2]) != "error"):
                    return "fn"
                else:
                    return "error"
        else:
            if (type(exp[2]) != list):
                if (verificador_bem_tipada(exp[1]) != "error") and (verificador_bem_tipada([exp[2]]) != "error"):
                    return "fn"
                else:
                    return "error"
            else:
                if (verificador_bem_tipada(exp[1]) != "error") and (verificador_bem_tipada(exp[2]) != "error"):
                    return "fn"
                else:
                    return "error"


    elif exp[0] == '!':
        if (len(exp) != 2):
            return "error"
        elif (type(exp[1]) == list):
            if (verificador_bem_tipada(exp[1]) != "error"):
                return "derref"
            else:
                return "error"
        else:
            if (verificador_bem_tipada([exp[1]]) != "error"):
                return "derref"
            else:
                return "error"



    elif (exp[0] == 'not'):

        if (len(exp) == 1):
            return "error"
        elif (exp[1] == 'not'):
            if (len(exp) == 2):
                return "error"
            elif (verificador_bem_tipada([exp[2]]) == "bool"):
              return "bool"

    elif (len(exp) > 1) and ((type(exp[0]) == str) and (exp[1] == ':=')): ## verifica se houve atribuiçao p/ uma variavel
        memoria.update({exp[0] : exp[2]})
        return "atribuicao"
    elif (exp[0] == "atribuicao"):
        return "atribuicao"

## parte do codigo em que começo a tratar de coisas como and e or:

    if (len(exp) > 1):


        if (exp[1] in lista_simbolos_operacao):
            if (exp[0] == "int") or (verificador_bem_tipada([exp[0]]) == "int"):
                if (len(exp) == 2):  ## verifica se existe exp[2], evitando erro de compilacao
                    return "error"
                elif (exp[2] == "int") or (verificador_bem_tipada([exp[2]]) == "int"):
                    return "int"
                    ##elif (verificador_bem_tipada(exp[2]) == "error"):
                else:
                    return "error"


        elif (exp[1] in lista_simbolos_comparacao):
            if (exp[0] == "int") or (verificador_bem_tipada([exp[0]]) == "int"):
                if (exp[2] == "int") or (verificador_bem_tipada([exp[2]]) == "int"):
                    return "bool"
                else:
                    return "error"


        if (exp[1] in lista_operadores_logicos):
            if len(exp) == 2: ## verifica se nao ha nada do tipo "x or" ou "y and"
                return "error"
            elif (exp[0] == "bool" and exp[2] == "bool") or (verificador_bem_tipada([exp[0]]) == "bool" and (verificador_bem_tipada([exp[2]]) == 'bool')):
                return "bool"
            else:
                return "error"
    if (exp[0] == "for") or (exp[0] == "if"):
        return (testa_for_ou_if(exp[0], exp))


    return "error"






def testa_for_ou_if(if_ou_for, expressao):

    exp = copy.deepcopy(expressao)

    if (if_ou_for == "if") or (if_ou_for == "for"):
        if (if_ou_for == "if"):
            tipo1 = "bool"
            then_ou_until = "then"
            else_or_do = "else"
        elif (if_ou_for == "for"):
            tipo1 = "int"
            then_ou_until = "until"
            else_or_do = "do"
        if (exp[0] == if_ou_for):
            if (len(exp) != 6): ## precisa ter 6 para se adequar em "if x then y else z"
                return "error"
            elif type(exp[1]) == list:
                if (verificador_bem_tipada(exp[1]) == tipo1):
                    if ((exp[2] == then_ou_until) and (exp[4] == else_or_do)):
                        if type(exp[3]) == list:
                            if type(exp[5]) == list:
                                if (if_ou_for == "if"):
                                    if (verificador_bem_tipada(exp[5])) == (verificador_bem_tipada(exp[3])):
                                        return verificador_bem_tipada(exp[3])
                                elif (if_ou_for == "for"):
                                    if (verificador_bem_tipada(exp[3]) == "int"):
                                        return verificador_bem_tipada(exp[5])
                                else:
                                    return "error"

                            else:
                                if (if_ou_for == "if"):
                                    if (verificador_bem_tipada([exp[5]])) == (verificador_bem_tipada(exp[3])):
                                        return verificador_bem_tipada(exp[3])
                                elif (if_ou_for == "for"):
                                    if (verificador_bem_tipada(exp[3]) == "int"):
                                        return verificador_bem_tipada(exp[5])
                                else:
                                    return "error"

                        else:
                            if type(exp[5]) == list:
                                if (if_ou_for == "if"):
                                    if (verificador_bem_tipada(exp[5])) == (verificador_bem_tipada([exp[3]])):
                                        return verificador_bem_tipada([exp[3]])
                                elif (if_ou_for == "for"):
                                    if (verificador_bem_tipada([exp[3]]) == "int"):
                                        return verificador_bem_tipada(exp[5])
                                else:
                                    return "error"
                            else:
                                if (if_ou_for == "if"):
                                    if (verificador_bem_tipada([exp[5]])) == (verificador_bem_tipada([exp[3]])):
                                        return (verificador_bem_tipada([exp[5]]))
                                elif (if_ou_for == "for"):
                                    if (verificador_bem_tipada([exp[3]]) == "int"):
                                        return verificador_bem_tipada([exp[5]])
                                else:
                                    return "error"
                    else:
                        return "error"
                else:
                    return "error"
            elif (verificador_bem_tipada([exp[1]]) == tipo1):
                if ((exp[2] == then_ou_until) and (exp[4] == else_or_do)):
                    if type(exp[3]) == list:
                        if type(exp[5]) == list:
                            if (if_ou_for == "if"):
                                if (verificador_bem_tipada(exp[5])) == (verificador_bem_tipada(exp[3])):
                                    return verificador_bem_tipada(exp[3])
                            elif (if_ou_for == "for"):
                                if (verificador_bem_tipada(exp[3]) == "int"):
                                    return verificador_bem_tipada(exp[5])
                            else:
                                return "error"

                        else:
                            if (if_ou_for == "if"):
                                if (verificador_bem_tipada([exp[5]])) == (verificador_bem_tipada(exp[3])):
                                    return verificador_bem_tipada(exp[3])
                            elif (if_ou_for == "for"):
                                if (verificador_bem_tipada(exp[3]) == "int"):
                                    return verificador_bem_tipada(exp[5])
                            else:
                                return "error"

                    else:
                        if type(exp[5]) == list:
                            if (if_ou_for == "if"):
                                if (verificador_bem_tipada(exp[5])) == (verificador_bem_tipada([exp[3]])):
                                    return verificador_bem_tipada([exp[3]])
                            elif (if_ou_for == "for"):
                                if (verificador_bem_tipada([exp[3]]) == "int"):
                                    return verificador_bem_tipada(exp[5])
                            else:
                                return "error"
                        else:
                            if (if_ou_for == "if"):
                                if (verificador_bem_tipada([exp[5]])) == (verificador_bem_tipada([exp[3]])):
                                    return (verificador_bem_tipada([exp[5]]))
                            elif (if_ou_for == "for"):
                                if (verificador_bem_tipada([exp[3]]) == "int"):
                                    return verificador_bem_tipada([exp[5]])
                            else:
                                return "error"
                else:
                    return "error"
            else:
                return "error"



def cutit(s, n):
    return s[n:]

## TESTE:
print(verificador_bem_tipada(['if', [2, '>', [4, '+', 3]], 'then', 3, 'else', 0]))
#print(verificador_bem_tipada(['fn', ['for', 2, 'until', 4, 'do', ['x', ':=', [2, '+', 5]]], ['not', 'not', 'false']]))
#print (verificador_bem_tipada(['for', 2, 'until', 4, 'do', ['x', ':=', [2, '+', 5]]]))
#print(verificador_bem_tipada(['for', [[[1, '>', 6], '+', [2, '-', [3, '+', 7]]], '>', 2], 'until', 'false', 'do', [[1, '<', 5], '-', 6]]))
#print (verificador_bem_tipada(['not', 'not', 'false']))

#def separador_expressoes()