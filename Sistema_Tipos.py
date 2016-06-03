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
        if var == int(var):
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
