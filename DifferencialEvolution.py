# coding: utf-8
import random
import math


def rastrigin(X, D):
    point = 0
    for i in range(D):
        tmp = X[i] * X[i] - (10 * math.cos(2 * math.pi * X[i])) + 10
        point = point + tmp
    return point


def sphere(X, D):
    point = 0
    for i in range(D):
        tmp = X[i] * X[i]
        point = point + tmp
    return point


def main():
    M = 30
    D = 5
    Cr = 0.9
    Fw = 0.5
    Tmax = 1000
    Fend = 1e-5
    Xmin, Xmax = -5, 5
    X = [[random.uniform(Xmin, Xmax) for i in range(D)] for j in range(M)]
    Xnew = [[0.0 for i in range(D)] for j in range(M)]
    V = [0.0 for i in range(D)]
    U = [0.0 for i in range(D)]
    F = [0.0 for i in range(M)]
    Ftmp = 0.0
    Fbest = 1.0 * 10 ** 10
    Xbest = [0.0 for i in range(D)]

    for i in range(M):
        F[i] = rastrigin(X[i], D)

    for t in range(Tmax):
        for i in range(M):
            num1 = random.randint(1, M-1)
            num2 = random.randint(1, M-1)
            num3 = random.randint(1, M-1)
            for j in range(D):
                V[j] = X[num1][j] + Fw * (X[num2][j] - X[num3][j])
            Jr = random.randint(1, D)
            for j in range(D):
                ri = random.uniform(0, 1)
                if ri < Cr or j == Jr:
                    U[j] = V[j]
                else:
                    U[j] = X[i][j]
            Ftmp = rastrigin(U, D)
            if Ftmp < F[i]:
                F[i] = Ftmp
                Xnew[i] = U
                Fbest = F[i]
                Xbest[j] = Fbest
            else:
                Xnew[i] = X[i]

        X = Xnew
        if Fbest < Fend:
            break
        print(t, min(F))

    print("終了時刻 t = " + str(t))
    print("解の目的関数 Fg = " + str(Fbest))


if __name__ == '__main__':
    main()
