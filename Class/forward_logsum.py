import numpy as np
import sys
import math


def Viterbi(emit_prob,trans_prob,observe):

    L = len(observe) #観測データの長さ
    K = len(trans_prob)-1 #隠れ状態の種類

    print('観測データ',observe)
    print('')

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



def main() :
    #出力確率
    emit_prob = [[],
                 [1/6, 1/6, 1/6, 1/6, 1/6, 1/6],
                 [1/10, 1/10, 1/10, 1/10, 1/10, 1/2]]

    #遷移確率
    trans_prob = [[0,0.5,0.5] ,
                  [0,0.95,0.05],
                  [0,0.1, 0.9]]


    observe = input('観測された出目:')
    observe = str(observe)

    probability = Viterbi(emit_prob,trans_prob,observe)

    print('確率',  "{:.5}".format(probability))


main()