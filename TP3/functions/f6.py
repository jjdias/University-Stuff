# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 08:47:37 2011
@author: pcardoso
"""
import numpy as np
import math

print("""a carregar Griewangk's function 8
    global minimum:
    f(x)=0; x(i)=0, i=1:n.""")

a = -600
b = 600


def domf():
    return a,b


def domfok(x):
    x = np.array(x)
    if np.all(x >= a) and np.all(x <= b):
        return True
    else:
        return False


def f(x):
    """
       Griewangk's function 8
        global minimum
         f(x)=0; x(i)=0, i=1:n.
    """
    try:
        x = np.array(x)
        
        if np.isrealobj(x) and domfok(x):
            s = 0.0
            for i in range(len(x)):
                s += x[i] ** 2
            p = 1.0
            for i in range(len(x)):
                p *= math.cos(x[i] / math.sqrt(i + 1))
            return s / 4000.0 - p + 1.0
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
    print(f((0,0,0,0)))
    print(f([1,2,30]))
    print(domf())
    
