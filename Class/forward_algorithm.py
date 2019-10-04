import numpy as np
import sys
import math
import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-logsum','-l', default=False, action='store_true',help='do forward algorithm with log sum')
    args = parser.parse_args()


    if args.logsum :
        return 'logsum'
    else:
        return 'scaling'

def Viterbi_logsum(emit_prob,trans_prob,observe):

    L = len(observe) #観測データの長さ
    K = len(trans_prob)-1 #隠れ状態の種類

    print('観測データ',observe)

###########初期化#######

    F = np.zeros((L+1, K+1), dtype=float)
    F[0,] = - sys.maxsize #+ 1000000
    F[0,0] = 0

##########再帰##########
    i = 1
    l = 1
    while i <= L :
        while l <= K:
            x = int(observe[i-1])-1

            if i == 1 :
                if l== 1:
                    F[i][l] = math.log10(emit_prob[l][x]) + math.log10( 10.0**(F[i-1][0]+math.log10(trans_prob[0][1])))
                else :
                    F[i][l] = math.log10(emit_prob[l][x]) + math.log10( 10.0**(F[i-1][0]+math.log10(trans_prob[0][2])))


            else :
                F[i][l] = math.log10(emit_prob[l][x]) +math.log10( 10.0**(F[i - 1][1] + math.log10(trans_prob[1][l]))
                                                                   + 10.0**(F[i - 1][2] + math.log10(trans_prob[2][l])))

            l += 1

        i += 1
        l = 1

    px= 10.0**F[L][1]+ 10.0**F[L][2]

    return px


def Viterbi_scaling(emit_prob,trans_prob,observe):

    L = len(observe) #観測データの長さ
    K = len(trans_prob)-1 #隠れ状態の種類

    print('観測データ   ',observe)

###########初期化#######

    F = np.zeros((L+1, K+1), dtype=float)
    F[0,] = 0
    F[0,0] = 1
    s =np.zeros((L+1), dtype=float)

##########再帰##########
    i = 1
    l = 1
    while i <= L :
        while l <= K:
            x = int(observe[i-1])-1
            if i == 1 :
                    s[i] = emit_prob[1][x] * (F[0][0] * trans_prob[0][1])\
                           + emit_prob[2][x] * (F[0][0] * trans_prob[0][2])
                    F[i][l] =  emit_prob[l][x] * F[i-1][0] * trans_prob[0][l] / s[i]

            else:
                s[i] = emit_prob[1][x] * (F[i - 1][1] * trans_prob[1][1] + F[i - 1][2] * trans_prob[2][1]) + \
                       emit_prob[2][x] * (F[i - 1][1] * trans_prob[1][2] + F[i - 1][2] * trans_prob[2][2])
                F[i][l] = 1 / s[i] * emit_prob[l][x] * (F[i - 1][1] * trans_prob[1][l] + F[i - 1][2] * trans_prob[2][l])

            l += 1

        i += 1
        l = 1

    print(F)
    print(s)
    j = 1
    px = 1
    while j <=L:
        px = px * s[j]
        j += 1

    return px






def main():
    result = parser()
    emit_prob = [[],
                 [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6],
                 [1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 2]]

    # 遷移確率
    trans_prob = [[0, 0.5, 0.5],
                  [0, 0.95, 0.05],
                  [0, 0.1, 0.9]]

    observe = input('観測された出目:')
    observe = str(observe)

    if result == 'scaling':
        print("スケーリング版")
        probability = Viterbi_scaling(emit_prob, trans_prob, observe)

    elif result == 'logsum':
        print("対数変換版")
        probability = Viterbi_logsum(emit_prob, trans_prob, observe)

    else :
        print("Error")

    print('確率', "{:.5}".format(probability))

main()