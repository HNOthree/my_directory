from numpy.random import *
import numpy as np
import random
import math
import sys

def E_parameter(F,B,trans_prob,observe):
    kind=6 #出力する目の個数
    L = len(observe)  # 観測データの長さ
    K = len(trans_prob) - 1  # 隠れ状態の種類
    E = np.zeros((K + 1, kind + 1), dtype=float)
    e = np.zeros((K + 1, kind + 1), dtype=float)
    observe=[0]+observe

    k =1
    b=1
    while k<=K:
        while b <=kind:
            e_sub = 0
            for i in range (1,L+1):
                if b == int(observe[i]):#i番目 1スタート
                    #print(observe)
                    #print(i,b,observe[i])
                    #print(F[i][k],B[i][k])
                    e_sub += F[i][k]*B[i][k]
            E[k][b]=e_sub
            b += 1
        b = 1
        k += 1



    k=1
    b=1
    while k <=K:
        while b<=kind:
            e[k][b]=E[k][b]/(E[k][1]+E[k][2]+E[k][3]+E[k][4]+E[k][5]+E[k][6])
            b += 1
        b=1
        k+=1
    #print(e)
    return e

def A_parameter(emit_prob,trans_prob,observe,s,F,B):#Aのパラメータ更新
    L = len(observe)  # 観測データの長さ
    K = len(trans_prob) - 1  # 隠れ状態の種類
    A = np.zeros((K + 1, K + 1), dtype=float)
    observe=[0]+observe

    a = np.zeros((K + 1, K + 1), dtype=float)
    a[0,] = 0.5
    k = 1
    i = 1
    l = 1
    while k <= K:
        while l <= K:
            #print(k, l)
            x = int(observe[i+1])#i+1番目
            a_sub=0
            for j in range(1,L):
                a_sub += F[j][k]*trans_prob[k][l]*emit_prob[l][x]*B[j+1][l]
            A[k][l]=1/s[i+1]*a_sub
            l += 1
        k += 1
        l = 1
   # print(A)
    k = 1
    l = 1
    while k <= K:
        while l <= K:
            #print(a[k][l])
            #print(A[k][l])
            a[k][l]=A[k][l]/(A[k][1]+A[k][2])
            l += 1
        k += 1
        l = 1
    #print(a)

    return a


def Backward(emit_prob,trans_prob,observe,s): #後ろ向きアルゴリズム
    L = len(observe)  # 観測データの長さ
    K = len(trans_prob) - 1  # 隠れ状態の種類

    B = np.zeros((L + 1, K + 1), dtype=float)
    B[L,] = 1
    observe=[0]+observe

    ##########再帰##########

    i = L - 1
    l = 1
    while i >= 1:
        while l <= K:
            x = int(observe[i+1])

            B[i][l] = 1 / s[i + 1] * ((emit_prob[1][x] * B[i + 1][1] * trans_prob[l][1]) \
                                      + (emit_prob[2][x] * B[i + 1][2] * trans_prob[l][2]))

            l += 1
        i -= 1
        l = 1
    #print(B)
    return B



def Forward(emit_prob,trans_prob,observe):#前向きアルゴリズム
    L = len(observe)  # 観測データの長さ
    K = len(trans_prob) - 1  # 隠れ状態の種類
    observe=[0]+observe
    #print('観測データ   ', observe)

    ###########初期化#######

    F = np.zeros((L + 1, K + 1), dtype=float)
    F[0,] = 0
    F[0, 0] = 1
    s = np.zeros((L + 1), dtype=float)

    ##########再帰##########
    i = 1
    l = 1
    while i <= L:
        while l <= K:
            x = int(observe[i])
            if i == 1:
                s[i] = emit_prob[1][x] * (F[0][0] * trans_prob[0][1]) \
                       + emit_prob[2][x] * (F[0][0] * trans_prob[0][2])
                F[i][l] = emit_prob[l][x] * F[0][0] * trans_prob[0][l] / s[i]

            else:
                s[i] = emit_prob[1][x] * (F[i - 1][1] * trans_prob[1][1] + F[i - 1][2] * trans_prob[2][1]) + \
                       emit_prob[2][x] * (F[i - 1][1] * trans_prob[1][2] + F[i - 1][2] * trans_prob[2][2])
                F[i][l] = 1 / s[i] * emit_prob[l][x] * (F[i - 1][1] * trans_prob[1][l] + F[i - 1][2] * trans_prob[2][l])

            l += 1

        i += 1
        l = 1

    return F,s


def emit(fair_emit,loaded_emit,Hidden_state,number):#Fair Loadedのタグつけ

    Hidden_state=str(Hidden_state)

    if Hidden_state == "F":
        num= random.choices(number, fair_emit)
        return num[0]
    elif Hidden_state == "L":
        num= random.choices(number, loaded_emit)
        return num[0]


def generate_observe():#正解データの生成
    start_weight = [0.5, 0.5]
    fair_weight = [0.95, 0.05]
    load_weight = [0.1, 0.9]
    fair_emit = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]
    loaded_emit = [1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 2]
    status = ['F', 'L']
    number = [1, 2, 3, 4, 5, 6]


    L=30000-1
    Hidden_state = ['0']*(L+1)
    Observe = ['0']*(L+1)
    Hidden =str(random.choices(status,start_weight))
    Hidden_state[0]=Hidden[2]
    Observe[0]=emit(fair_emit,loaded_emit,Hidden_state[0],number)

    i = 1
    while i <= L:
        if Hidden_state[i - 1] == 'F':
            Hidden = str(random.choices(status, fair_weight))
            Hidden_state[i] = Hidden[2]
            Observe[i] = emit(fair_emit, loaded_emit, Hidden_state[i], number)

        elif Hidden_state[i - 1] == 'L':
            Hidden = str(random.choices(status, load_weight))
            Hidden_state[i] = Hidden[2]
            Observe[i] = emit(fair_emit, loaded_emit, Hidden_state[i], number)

        else:
            print('?')
        i += 1


    print('観測データ　', "".join(map(str, Observe)))
    print('正解隠れ状態', "".join(map(str, Hidden_state)))
    return Observe, Hidden_state


def main():

#############正解データ生成

    Observe,hiddenstate=generate_observe()


    #print('観測データ　', "".join(map(str, Observe)))
    #print('正解隠れ状態', "".join(map(str, hiddenstate)))

#############################################


#######初期確率生成

    emit_prob_BW_1=[0]
    emit_prob_BW_2=[0]

    trans_prob_BW1=[0]
    trans_prob_BW2=[0]

    p=rand()
    trans_prob_BW1.append(p)
    trans_prob_BW1.append(1-p)
    p=rand()
    trans_prob_BW2.append(p)
    trans_prob_BW2.append(1-p)


    denominator=100
    numerator=denominator

    for i in range(1,6):
        number =randint(1, numerator-(7-i))
        emit_prob_BW_1.append(number/denominator)
        numerator -= number

        #print (i)

    emit_prob_BW_1.append(numerator/denominator)

    numerator=denominator
    for i in range(1, 6):
        number = randint(1, numerator - (7 - i))
        emit_prob_BW_2.append(number / denominator)
        numerator -= number

        #print(i)

    emit_prob_BW_2.append(numerator / denominator)



    emit_prob=[[],emit_prob_BW_1,emit_prob_BW_2]
    trans_prob=[[0,0.5,0.5],trans_prob_BW1,trans_prob_BW2]
    print('初期生成確率'),
    for i in range(1,3):
        if i == 1:
            print('Fair')
        else:
            print('Loaded')
        print(emit_prob[i][1],emit_prob[i][2],emit_prob[i][3],emit_prob[i][4],emit_prob[i][5],emit_prob[i][6])


    print('初期遷移確率')
    for i in range(1,3):
        if i == 1:
            print('Fair')
        else:
            print('Loaded')
        print(trans_prob[i][1],trans_prob[i][2])


##################################################



########再帰


#######F,Bの計算

    #F=[] #Forward変数
    #B=[] #backward変数
    A=[]#EMアルゴリズム
    E=[]#
    index= -sys.maxsize

    while True:
        F,S=Forward(emit_prob,trans_prob,Observe)
        #print('F\n',F)
        #print('S\n',S)


        log_si=0
        for i in S:
            #print(i)
            if i==0 :
                log_si=0
            else:
                log_si+=math.log10(i)

        if log_si ==index:
            break
        elif log_si < index:
            #print('Error')
            break

        else:
            index=log_si
            B = Backward(emit_prob, trans_prob, Observe, S)
            # print('B\n',B)
            A = A_parameter(emit_prob, trans_prob, Observe, S, F, B)
            # print('A\n',A)
            E = E_parameter(F, B, trans_prob, Observe)
            # print('E\n',E)
            emit_prob=E
            trans_prob=A
            #print("index",index)


    print('推定生成確率'),
    for i in range(1, 3):
        if i == 1:
            print('Fair')
        else:
            print('Loaded')
        print(emit_prob[i][1], emit_prob[i][2], emit_prob[i][3], emit_prob[i][4], emit_prob[i][5], emit_prob[i][6])

    print('推定遷移確率')
    for i in range(1, 3):
        if i == 1:
            print('Fair')
        else:
            print('Loaded')
        print(trans_prob[i][1], trans_prob[i][2])


    #print('Emit Probability\n',E[1:])
    #print('Trans_Probabirity\n',A[1:])

main()