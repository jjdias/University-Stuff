import random
import numpy as np


class Particle:
    def __init__(self, f, n=2, eta1=2, eta2=2, xi=.7289):
        self.f = f
        self.n = n
        self.eta1 = eta1
        self.eta2 = eta2
        self.xi = xi

        # inicializa a posicao da particula, velocidade e o valor de f(posicao)
        self.x = np.array([f.a + random.random() * (f.b - f.a) for _ in range(n)])
        self.v = np.array([f.a + random.random() * (f.b - f.a) for _ in range(n)])
        self.fx = self.f.f(self.x)

        # define/guarda o personal best da particula e o f(pb)
        self.pb = self.x
        self.fpb = self.fx

    def get_pb(self):
        return self.pb, self.fpb

    def step(self, gb):
        # calcula a nova velocidade
        npgb = np.array(gb[:])
        self.v = self.v \
                 + self.eta1 * random.random() * (self.pb - self.x) \
                 + self.eta2 * random.random() * (npgb - self.x)

        # aplica fator de constricao
        self.v *= self.xi

        # atualiza a posicao da particular tendo em conta a posicao anterioe
        # e a velocidade
        self.x = self.x + self.v

        # verifica se não saiu do dominio/intervalo
        for i in range(self.n):
            if self.x[i] > self.f.b:
                self.x[i] = self.f.b
            elif self.x[i] < self.f.a:
                self.x[i] = self.f.a

        # calcula o novo valor da funcao objetivo
        self.fx = self.f.f(self.x)

        # atualiza o personal best
        if self.fpb > self.fx:
            self.pb = self.x
            self.fpb = self.fx

    def __repr__(self):
        return "x = " + str(self.x) \
               + "\t v = " + str(self.v) \
               + "\t f(x) = " + str(self.fx)


if __name__ == "__main__":
    p = Particle(n=2)
    print(p)
    for _ in range(10):
        p.step(*p.get_pb())
        print(p)
