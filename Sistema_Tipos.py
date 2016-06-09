#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===================================
# A memoria será definida por um dicionário:
# Onde:
# Chave => Endereço da memória
# Valor da chave => Valor na memória
#====================================
# Exemplos:
# Endereços:
# 0 => 0
# 1 => 1
# 3000 => v
# v => 1000
#=====================================

memoria = {

    0:0,
    1:1,
    3000:'v',
    'v':42

    }

 if is_a_number(x):
	print("xd")
 else:
    print(":(")   
#======================================
# Funções principais:
# is_a_number => identifica se o tipo é inteiro
# is_a_bool => identifica se o tipo é booleano
#======================================
# Função is_a_number(var)=> bool
# onde var é uma variavel
#======================================
def is_a_number(var):
    try:
        if var == int(var) and var>= 0 :
            return True
    except Exception:
        return False
        
#======================================
# Função is_a_bool(var)=> bool
# onde var é uma variavel 
#======================================
def is_a_bool(var):
    try:
        if var == bool(var):
            return True
    except Exception:
        return False
#=======================================
debug = [2, "+", 4]

##if 3>=2 then 4 else 3


def is_a_skip(var):
    try:
        if var == "skip":
            return True
    except Exception:
        return False


def is_a_fn(lista):

    v1 = lista[0]
    v2 = lista[1]
    v3 = lista[2]
        
        if is_a_number(lista[3]) or lista[3] == lista[1]:
            for i in xrange(3, len(lista), 1):
                if (lista[i] == "+" or lista[i] == "-") and not((is_a_number(lista[i-1]) and is_a_number(lista[i+1]))) and not((lista[i-1]==lista[1]) and (lista[i+1]==lista[1])):
                    

def verificador_bem_tipada(expressao):
    