# coding: utf-8
import random
import math
import copy


def value(V, X, D):
    point = 0
    for i in range(D):
        tmp = V[i] * X[i]
        point = point + tmp
    return point


def weight(W, X, D):
    point = 0
    for i in range(D):
        tmp = W[i] * X[i]
        point = point + tmp
    return point


def main():
    M = 20
    D = 10

    Pm = 0.05
    Tmax = 100

    # Weight = [7, 5, 1, 9, 6]
    # Value = [50, 40, 10, 70, 55]
    # Wmax = 15
    Weight = [3, 6, 5, 4, 8, 5, 3, 4, 8, 2, ]
    Value = [70, 120, 90, 70, 130, 80, 40, 50, 30, 70]
    Wmax = 20

    X = [[0.0 for i in range(D)] for j in range(M)]
    Xnext = [[0.0 for i in range(D)] for j in range(M)]
    F = [0.0 for i in range(M)]
    Fbest = 0
    Xbest = [0.0 for i in range(D)]
    p1, p2 = 0, 0
    i, d, d1, d2, tmp = 0, 0, 0, 0, 0

    # for t in range(Tmax):
    # 生成
    for i in range(M):
        for j in range(D):
            X[i][j] = random.randint(0, 1)
    # 評価
    a = 0
    for i in range(M):
        for j in range(D):
            F[i] = value(Value, X[i], D)
            a = weight(Weight, X[i], D)
            # print(F[i], a)
            if a > Wmax:
                F[i] = 1
            if Fbest < F[i]:
                Fbest = F[i]
                Xbest = copy.copy(X[i])
    # print(F)

    sumf = sum(F)
    r = random.uniform(0, 1)

    # 選択
    for i in range(M):
        # print(F, sumf)
        prob = F[i] / sumf
        if r < prob:
            p1 = i
            break
        r = r - prob
    r = random.uniform(0, 1)
    sumf = sumf - F[p1]
    for i in range(M):
        if i != p1:
            prob = F[i] / sumf
            if r < prob:
                p2 = i
                break
            r = r - prob
        d1 = random.randint(0, D)
        for i in range(100):
            d2 = random.randint(0, D)
            if d1 != d2:
                break

        if d1 < d2:
            tmp = d1
            d1 = d2
            d2 = tmp

        # 交叉
        for d in range(D):
            if d <= d1 or d > d2:
                Xnext[i][d] = X[p1][d]
            else:
                Xnext[i][d] = X[p2][d]
        # 突然変異
        for d in range(D):
            per = random.uniform(0, 1)
            if per < Pm:
                Xnext[i][d] = 1 - Xnext[i][d]
    X = copy.copy(Xnext)
    print("解の目的関数値Fg = " + str(Fbest))
    print("最適解 Xbest = " + str(Xbest))


if __name__ == '__main__':
    main()
