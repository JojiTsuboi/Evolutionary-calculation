# coding: utf-8
import math
import random
import pprint


def rastrigin(X, D):
    point = 0
    for i in range(D):
        tmp = X[i] * X[i] - (10 * math.cos(2 * math.pi * X[i])) + 10
        point = point + tmp
    return point

def sphere(X,D):
    point = 0
    for i in range(D):
        tmp = X[i] * X[i]
        point = point + tmp
    return point


def main():
    M = 30  # 粒子数
    D = 5  # 解の次元
    c = 1.494
    w = 0.729
    Tmax = 1000  # 繰り返し数
    Cr = 1e-5  # 終了条件
    Xmin = -5
    Xmax = 5  # 範囲

    # 位置と速度
    X = [[random.uniform(Xmin, Xmax) for i in range(D)] for j in range(M)]
    V = [[0.0 for i in range(D)] for j in range(M)]
    # 評価値格納
    F = ["" for i in range(M)]
    # Pbest
    Fp = [1.0 * 10 ** 10 for p in range(M)]
    Xp = [[random.uniform(Xmin, Xmax) for i in range(D)] for j in range(M)]
    # Gbest
    Fg = 1.0 * 10 ** 10
    Xg = [0.0 for i in range(D)]
    # print(Xg)
    # print(X)

    for t in range(Tmax):
        for i in range(M):
            F[i] = rastrigin(X[i], D)
            # print(F)
            # print(Fp)
            if F[i] < Fp[i]:
                Fp[i] = F[i]
                for d in range(D):
                    Xp[i][d] = X[i][d]
                # print(Xp)
                if Fp[i] < Fg:
                    Xg[d] = X[i][d]
                    Fg = Fp[i]
                print(Fg)
        if Fg < Cr:
            break
        for i in range(M):
            for d in range(D):
                r1 = random.random()
                r2 = random.random()
                # print(Xg[0])
                # print(X[i][d])
                V[i][d] = w * V[i][d] + c * r1 * (Xp[i][d] - X[i][d]) + c * r2 * (Xg[d] - X[i][d])
                X[i][d] = X[i][d] + V[i][d]

    print("終了時刻 t = " + str(t))
    print("解の目的関数値 Fg = " + str(Fg))
    print(Xg)


if __name__ == '__main__':
    main()
