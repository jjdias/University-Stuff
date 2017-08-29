# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 08:47:37 2011
@author: pcardoso
"""
import numpy as np

print("""a carregar Rotated hyper-ellipsoid function
        global minimum:
        f(x)=0; x(i)=0, i=1:n.
  """)


a = -65.536
b = 65.536


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
        Rotated hyper-ellipsoid function
    """
    try:
        x = np.array(x)
        if np.isrealobj(x) and domfok(x):            
            s = 0.0
            for i in range(len(x)):
                saux = 0.0
                for j in range(i + 1):
                    saux += x[j]
                s += saux ** 2.0
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
    print(f((0, 0, 0)))
    print(f([-65, 65]))
    print(domf())
    
