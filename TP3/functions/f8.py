# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 08:47:37 2011
@author: pcardoso
"""
import numpy as np
import math

print("""a carregar Michalewicz's function 12
    global minimum:
        f(x)=-4.687 (n=5); x(i)=???, i=1:n.
        f(x)=-9.66 (n=10); x(i)=???, i=1:n.
    """)

a = 0
b = math.pi


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
         Michalewicz's function 12
         global minimum:
            f(x)=-4.687 (n=5); x(i)=???, i=1:n.
            f(x)=-9.66 (n=10); x(i)=???, i=1:n.
    """
    try:
        x = np.array(x)
        
        if np.isrealobj(x) and domfok(x):
            s = 0.0
            m = 20
            for i in range(len(x)):
                s += math.sin(x[i]) * (math.sin((i + 1) * x[i]**2 / math.pi))**(2 * m)
            return -s
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
    print(f((2.1, 1.5)))
    print(f([1, 2, 30]))
    print(domf())
