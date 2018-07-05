#CALCULADORA DE MATRICES
from VALID import OK, OKI, ns
import numpy as np
import subprocess

def crea_matriz(fil,col,f,c):
    e_fil=[]
    for f in range(0,fil):
        e_col=[]
        f+=1
        for c in range(0,col):
            c+=1
            valor=OK(input('Introduzca el componente (%d,%d): '%(f,c)))
            e_col.append(valor)
        e_fil.append(e_col)
        #for i in e_fil:
            #print(i)
    return e_fil
    
while True:
    fil=OKI(input("Indique número de filas: "))
    col=OKI(input("Indique número de columnas: "))

    f=-1;c=-1
    acum=0
    matr=crea_matriz(fil,col,f,c)
    acum=np.array([matr],float)
    print(acum)
    while True:
        oper=input("Introduzca operador: ")
        while oper!="+" and oper!="-" and oper!="/" and oper!="=":
            oper=input("Introduzca un operador válido: ")
        if oper=="+":
            matr=crea_matriz(fil,col,f,c)
            matri=np.array([matr],float)
            acum+=matri
        elif oper=="-":
            matr=crea_matriz(fil,col,f,c)
            matri=np.array([matr],float)
            acum-=matri
        elif oper=="/":
            matr=crea_matriz(fil,col,f,c)
            matri=np.array([matr],float)
            acum/=matri
        elif oper=="=":
            print("MATRIZ RESULTADO")
            print(acum)
            break
        print(matri)
    conti=ns(input("¿Reiniciar programa?: "))
    if conti=="n":
        break
    matr=0
    subprocess.call(["cmd.exe","/C","cls"])
        
    


