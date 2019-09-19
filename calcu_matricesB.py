#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import subprocess

def OKI(n):
    try:
        n=int(n)
    except:
        n=OKI(input("Caracter no valido: "))
    return n

def OK(n):
    try:
        n=float(n)
    except:
        n=OK(input("Caracter no valido: "))
    return n

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)

def val(tp):
    while tp!="N" and tp!="M":
        tp=input("Introduzca \'N\' para dato numérico y \'M\' para matriz: ")
    return tp

#FUNCIÓN DE TIPO DE DATO
def dato():
    tipo_dato=val(input("Tipo de dato: "))
    if tipo_dato=="M":
        matr=crea_matriz(fil,col,numVal)
    else:
        matr=OK(input("Introduce número: "))
    return matr

def resultado(m):
    print("\nMATRIZ RESULTADO")
    print(m,"\n")

#FUNCIÓN PARA DEFINIR MATRIZ
def crea_matriz(fil,col,num):
    while True:
        try:
            valores = list(map(float, input("Introduce "+str(num)+" valores separados por espacios: ").split()))
            if len(valores)== num:
                matriz = np.array(valores).reshape(fil,col)
                break
        else:
            print("NUMERO DE VALORES NO CORRESPONDIENTE CON LAS DIMENSIONES ESPECIFICADAS")
        except:
            print("DATOS INCORRECTOS")
    return matriz
    
while True:
    print("          CALCULADORA DE MATRICES          ") 
    print("""************TABLA DE OPERADORES************
*******************************************
SUMA                           OPERADOR "+"
RESTA                          OPERADOR "-"
MULTIPLICACION                 OPERADOR "*"
CLEAR                          OPERADOR "C"
DATO MATRIZ                    OPERANDO "M"
DATO NÚMERO                    OPERANDO "N"
*******************************************
*******************************************""")
    
    fil=OKI(input("Indique número de filas: "))
    col=OKI(input("Indique número de columnas: "))
    e=fil
    f=-1;c=-1
    numVal=fil*col
    acum=crea_matriz(fil,col,numVal)
    resultado(acum)
    while True:
        oper=input("Introduzca operador: ")
        while oper!="+" and oper!="-" and oper!="*" and oper!="C":
            oper=input("Introduzca un operador válido: ")
        if oper=="+":
            matr=dato()
            acum=acum+matr
            numVal=fil*col
            resultado(acum)
        elif oper=="-":
            matr=dato()
            acum=acum-matr
            numval=fil*col
            resultado(acum)
        elif oper=="*":
            tipo_dato=val(input("Tipo de dato: "))
            if tipo_dato=="M":
                fil=col
                col=OKI(input("Introduce número de columnas: "))
                numVal=fil*col
                matr=crea_matriz(fil,col,numVal)
                acum=np.dot(acum,matr)
                fil=e
                resultado(acum)
                numVal=fil*col
            else:
                matr=OK(input("Introduce número: "))
                acum=acum*matr
                resultado(acum)
        elif oper=="C":
            break
        
    conti=ns(input("¿Reiniciar cálculos?: "))
    if conti=="n":
        break
    matr=0
    subprocess.call(["cmd.exe","/C","cls"]) 
