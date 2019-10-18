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
        matr=crea_matriz(fil,col)
    else:
        matr=OK(input("Introduce número: "))
    return matr

#FUNCIÓN PARA DEFINIR MATRIZ
def crea_matriz(fil,col):
    f=-1;c=-1
    e_fil=[]
    for f in range(fil):
        e_col=[]
        f+=1
        for c in range(col):
            c+=1
            valor=OK(input('Introduzca el componente (%d,%d): '%(f,c)))
            e_col.append(valor)
        e_fil.append(e_col)
        matri=np.array(e_fil,float)
    return matri
    
while True:
    print("          CALCULADORA DE MATRICES          ") 
    print("""************TABLA DE OPERADORES************
*******************************************
SUMA                           OPERADOR "+"
RESTA                          OPERADOR "-"
MULTIPLICACION                 OPERADOR "*"
FINALIZAR CALCULO              OPERADOR "C"
DATO MATRIZ                    OPERANDO "M"
DATO NÚMERO                    OPERANDO "N"
*******************************************
*******************************************""")
    
    fil=OKI(input("Indique número de filas: "))
    col=OKI(input("Indique número de columnas: "))
    e=fil
    f=-1;c=-1
    acum=crea_matriz(fil,col)
    print("\n")
    print(acum,"\n")
    while True:
        oper=input("Introduzca operador: ")
        while oper!="+" and oper!="-" and oper!="*" and oper!="C":
            oper=input("Introduzca un operador válido: ")
        if oper=="+":
            matr=dato()
            acum=acum+matr
        elif oper=="-":
            matr=dato()
            acum=acum-matr
        elif oper=="*":
            tipo_dato=val(input("Tipo de dato: "))
            if tipo_dato=="M":
                fil=col
                col=OKI(input("Introduce número de columnas: "))
                matr=crea_matriz(fil,col)
                acum=np.dot(acum,matr)
                fil=e
            else:
                matr=OK(input("Introduce número: "))
                acum=acum*matr
                
        if oper!="C":
            print("\nRESULTADO")
            print(acum,"\n")

        else:
            break
        
    conti=ns(input("¿Reiniciar cálculos?: "))
    if conti=="n":
        break
    matr=0
    subprocess.call(["cmd.exe","/C","cls"])
