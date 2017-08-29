# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 08:47:37 2011
@author: pcardoso
"""
import numpy as np

print("""a carregar Rastrigin's function 6
        global minimum:
        f(x)=0; x(i)=0, i=1:n.""")

a = -5.12
b = 5.12


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
        Rastrigin's function 6
    """
    try:
        x = np.array(x)
        
        if np.isrealobj(x) and domfok(x):
            return 10 * len(x) + sum(x*x) - 10 * sum(np.cos(2*np.pi*np.cos(x)))
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
    print(domf())
    print("--", f((1, 2, 3, 4, 1, -2, 3)))
    print("--", f([1, 2, 30, 4]))
