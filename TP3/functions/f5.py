# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 08:47:37 2011
@author: pcardoso
"""
import numpy as np
import math

print("""a carregar Schwefel's function 7
        global minimum:
        f(x)=-n·418.9829; x(i)=420.9687, i=1:n. 
    """)

a = -500
b = 500


def domf():
    return a, b


def domfok(x):
    x = np.array(x)
    if np.all(x >= a) and np.all(x <= b):
        return True
    else:
        return False


def f(x):
    """
        Schwefel's function 7
        global minimum
        f(x)=-n·418.9829; x(i)=420.9687, i=1:n.
    """
    try:
        x = np.array(x)
        
        if np.isrealobj(x) and domfok(x):
            s = 0.0
            for i in range(len(x)):
                s -= x[i] * math.sin(math.sqrt(math.fabs(x[i])))
            return s
        else:
            raise Exception("Erro")
    except Exception as inst:
        if inst.__str__() == "Erro":
            print("o argumento nao pertence ao dominio: " + str(domf()))
            print("o argumento deve ser um vector: [1,2,...]")
        else:
            print(inst)


def minf():
    return 0   

if __name__ == "__main__":
    # exemplo de chamada a funcao
    print(f((420.9687, 420.9687, 420.9687)))
    print(f([1, 2, 30]))
    print(domf())
