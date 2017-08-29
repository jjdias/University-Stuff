# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 08:47:37 2011
@author: pcardoso
"""
import numpy as np

a = -2.048
b = 2.048

print("""a carregar Rosenbrock's valley (De Jong's function 2)
        global minimum
        f(x)=0; x(i)=1, i=1:n.
    """)


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
        Rosenbrock's valley (De Jong's function 2)
            global minimum
            f(x)=0; x(i)=1, i=1:n.
    """
    try:
        x = np.array(x)
        if np.isrealobj(x) and domfok(x):
                s1 = 0.0
                s2 = 0.0
                for i in range(x.__len__() - 1):
                    s1 += (x[i+1] - x[i] * x[i]) ** 2.0
                    s2 += (1.0 - x[i]) ** 2.0
                    
                return 100 * s1 + s2
        else:
            raise Exception("Erro")
    except Exception as inst:
        if inst.__str__() == "Erro":
            print("o argumento nao pertence ao dominio: " + str(domf()))
        else:
            print(inst)
   

def minf():
    return 0


if __name__ == "__main__":
    # exemplo de chamada a funcao
    print(f((0, 1, 2)))
    print(f([1, 2, 30]))
    print(f("[1, 1, 1]"))
    print(domf())
