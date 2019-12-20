# coding: utf-8
import math
import random
import pprint
from statistics import mean, median,variance,stdev

func = 0  # 0:rastrigin 1:sphere

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
    M = 30  # 粒子数
    D = 20  # 解の次元
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
    Fp = [1.0 * 10 ** 33 for p in range(M)]
    Xp = [[random.uniform(Xmin, Xmax) for i in range(D)] for j in range(M)]
    # Gbest
    Fg = 1.0 * 10 ** 33
    Xg = [0.0 for i in range(D)]
    # print(Xg)
    # print(X)

# def PSO():
    for t in range(Tmax):
        for i in range(M):
            if func == 0:
                F[i] = rastrigin(X[i], D)   #Rastrigin
            else:
                F[i] = sphere(X[i], D)      #Sphere
            # print(F)
            # print(Fp)
            if F[i] < Fp[i]:
                Fp[i] = F[i]
                for d in range(D):
                    Xp[i][d] = X[i][d]
                # print(Xp)
                if Fp[i] < Fg:
                    Xg = X[i]
                    Fg = Fp[i]
                # print(Fg)
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

    # print("終了時刻 t = " + str(t))
    # print("解の目的関数値 Fg = " + str(Fg))
    # print(Xg)
    return Fg,t,D


if __name__ == '__main__':
    # main()
    Fg_list = []
    t_list = []
    for a in range(100):
        Fg,t,D = main()
        print(Fg)
        print(t)
        Fg_list.append(Fg)
        t_list.append(t)
    if func == 0:
        Func = "Rastrigin"
    else:
        Func = "Sphere"
    Fg_ave = mean(Fg_list)
    t_ave = mean(t_list)

    x = 0
    for i in range(len(Fg_list)):
        x += (Fg_ave-Fg_list[i])**2
    Un_dispersion = x/len(Fg_list)
    dispersion = x/(len(Fg_list)-1)

    print("次元　" + str(D))
    print("関数　" + str(Func))
    # print("Fg_list = " + str(Fg_list))
    # print("t_list = " + str(t_list))
    print("Fg_ave = " + str(Fg_ave))
    print("t_ave = " + str(t_ave))
    print("Unbiased dispersion = " + str(Un_dispersion))
    print("dispersion = " + str(dispersion))

