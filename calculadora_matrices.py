#CALCULADORA DE MATRICES
from VALID import OK, OKI, ns
import numpy as np
import subprocess

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
    print("         CALCULADORA DE MATRICES          ") 
    print("""************TABLA DE OPERADORES************
*******************************************
SUMA                           OPERADOR "+"
RESTA                          OPERADOR "-"
MULTIPLICACION                 OPERADOR "*"
VER RESULTADO                  OPERADOR "="
*******************************************
*******************************************""")
    
    fil=OKI(input("Indique número de filas: "))
    col=OKI(input("Indique número de columnas: "))
    e=fil
    #c=col
    f=-1;c=-1
    acum=0
    matr=crea_matriz(fil,col)
    acum=matr
    print(acum)
    while True:
        oper=input("Introduzca operador: ")
        while oper!="+" and oper!="-" and oper!="*" and oper!="=":
            oper=input("Introduzca un operador válido: ")
        if oper=="+":
            matr=crea_matriz(fil,col)
            acum=acum+matr
        elif oper=="-":
            matr=crea_matriz(fil,col)
            acum=acum-matr
        elif oper=="*":
            fil=col
            col=OKI(input("Introduce número de columnas: "))
            matr=crea_matriz(fil,col)
            acum=np.dot(acum,matr)
            fil=e
            #col=c
        elif oper=="=":
            print("")
            print("MATRIZ RESULTADO")
            print(acum)
            print("")
            break
        print(matr)
    conti=ns(input("¿Reiniciar programa?: "))
    if conti=="n":
        break
    matr=0
    subprocess.call(["cmd.exe","/C","cls"])       
    
