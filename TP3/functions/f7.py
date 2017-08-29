# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 08:47:37 2011
@author: pcardoso
"""
import numpy as np
import math

print("""a carregar Ackley's Path function 10
       global minimum:
      f(x)=0; x(i)=0, i=1:n.
    """)

a = -32.768
b = 32.768


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
       Ackley's Path function 10
       global minimum:
      f(x)=0; x(i)=0, i=1:n.
    """
    try:
        x = np.array(x)
        
        if np.isrealobj(x) and domfok(x):
            aa = 20.0
            bb = 0.2
            c = 2.0 * math.pi
            s1 = 0.0
            s2 = 0.0
            for i in range(len(x)):
                s1 += x[i] ** 2.0 
                s2 += math.cos(c * x[i])
            return -aa * math.exp(-bb * math.sqrt(s1 / len(x))) - math.exp(s2 / len(x)) + aa + math.exp(1)
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
    print(f((0, 0, 0, 0)))
    print(f([1, 2, 30]))
    print(domf())
