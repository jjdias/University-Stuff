from multiprocessing import Value, Process, Array
import os
from functions.particle import *
# from particle import *
import functions.f3 as f


class PSO(Process):
    def __init__(self, f, n=2,
                 numero_particulas=20,
                 eta1=2, eta2=2, xi=.7289,
                 numero_maximo_iteracoes=10,
                 p_id=-1, gb=None, fgb=None
                 ):
        Process.__init__(self)
        self.f = f
        self.n = n
        self.xi = xi
        self.numero_particulas = numero_particulas
        self.eta1 = eta1
        self.eta2 = eta2
        self.numero_maximo_iteracoes = numero_maximo_iteracoes
        self.num_process = p_id  # PQ?
        self.gb = gb
        self.fgb = fgb

    def run(self):

        particulas = []

        gb = self.gb
        fgb = self.fgb

        # cria lista de particulas
        for p_id in range(self.numero_particulas):
            # cria a particula
            p = Particle(self.f, self.n, self.eta1, self.eta2)
            # adiciona a paritula a lista
            particulas.append(p)

            # atualiza o global best
            ppb, fppb = p.get_pb()
            if fppb < fgb.value:
                fgb.value = fppb  # f(posicao do global best)
                gb = list(ppb)  # posicao do global best
                id_bp = p_id  # indice da melhor particula

        # print(id_bp, particulas[id_bp], gb, fgb)

        # main cycle
        for _ in range(self.numero_maximo_iteracoes):

            # para cada particual
            for p_id, p in enumerate(particulas):

                # for each particle do a step
                p.step(gb)

                # update the global best, if needed
                # aqui a função get_pd() faz um return dos valores da particula
                ppb, fppb = p.get_pb()

                # print('process id:', os.getpid())
                # print(str(fgb.value) + " " + str(self.num_process) + " " + str(fppb))

                # Se o melhor da particula for maior que o global atual
                if fppb < fgb.value:
                    fgb.value = fppb
                    # gb é uma lista e estamos atualizando ela.
                    gb = list(ppb)
                    id_bp = p_id

                    # print(self.num_process)
                    # print(p_id, id_bp, particulas[id_bp], gb[:], fgb.value)
                    # print('process id:', os.getpid())


if __name__ == "__main__":

    gb = Array('d', range(2))
    fgb = Value('d', 0)
    fgb.value += 10 ** 10

    # p = PSO(
    #             f,
    #             n=2,
    #             numero_particulas=50,
    #             eta1=2,
    #             eta2=2,
    #             xi=0.7289,
    #             numero_maximo_iteracoes=1000,
    #             p_id=1,
    #             gb=gb,
    #             fgb=fgb)
    #
    # p.run()

    islands = []

    for i in range(3):
        p = PSO(
            f,
            n=2,
            numero_particulas=50,
            eta1=2,
            eta2=2,
            xi=0.7289,
            numero_maximo_iteracoes=1000,
            p_id=i,
            gb=gb,
            fgb=fgb)

        islands.append(p)

    for p in islands:
        p.start()

    for p in islands:
        p.join()

