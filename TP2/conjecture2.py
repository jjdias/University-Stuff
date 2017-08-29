import multiprocessing
import math
from multiprocessing import Process, Pool, Manager, Array
from multiprocessing import JoinableQueue
from time import sleep
import time


def isPrime(num):
    assert (num % 2 != 0)
    # Checando se eh primo apenas ateh a razi quadrada do numero.
    # Comesamos pelo 3 pois ja checamos o 2.
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return
    # Se tudo der certo, ele retorna o valor.
    else:
        return num

def Goldbach(par):

    file = open("dataDump.txt", "a")

    # print(str(par) + " = ")
    file.write("\n\n" + str(par) + " = ")

    for primo in primos:
        if primo > par:
            break
        if par - primo in primos:
            if primo <= par - primo:
                # print(str(primo) + " + " + str(par - primo))
                file.write(str(primo) + " + " + str(par - primo) + ", ")
            else:
                break

    file.close()

def worker():
    while not pares.empty():
        Goldbach(pares.get())
        pares.task_done()


if __name__ == "__main__":
    # O valor maximo que queremos usar
    n = 10000

    # Os valores primos que ficarao em uma lista compartilhada entre os processos.
    # Assim economizamos em memoria.
    # O metodo Manager() eh mais versatil embora mais lento que simplismente usar um Array.
    # manager = Manager()
    # primos = manager.list()

    # Tambem fiz com Array() "just because"
    primos = Array('i', 0)

    # Pool e um metodo simples de se dividir uma tarefa simples entre varios processos.
    # Aqui eles irao calcular os primos para nos.
    pool = Pool(processes=4)
    primos = pool.map(isPrime, range(3, n, 2))
    pool.close()

    # Forma mais ificiente que encontrei de colocar o 2 na lista de primos
    primos.insert(0, 2)

    # Remove os espasos vazius
    primos = [x for x in primos if x != None]

    # Print so para verificar se ta tudo certo.
    # Quando se usa o [:] no print de uma lista ele escreve a lista toda. Nao sei porque.
    # print(primos[:])

    # Os valores pares serao salvos em uma fila, "Queue",
    # e serao removidos comforme forem resolvidos pelos workers.
    pares = JoinableQueue()

    # Criando uma lista de pares
    for i in range(4, n, 2):
        pares.put(i)

    # Cria o arquivo onde guardaremos os dados.
    file = open("dataDump.txt", "w")
    file.write("Here we go.\n\n\n")
    file.close()

    # Cria os processos paralelos para realizar as tarefas.
    processos = []
    for i in range(4):
        # worker()
        p = multiprocessing.Process(target=worker, args=())
        processos.append(p)

    for p in processos:
        p.start()

    for p in processos:
        p.join()
