import numpy as np
import sys
import math

def compare(V,trans_prob,i,l): #トレースバックを求める
    label1 = V[i - 1][1] + math.log10(trans_prob[1][l])
    label2 = V[i - 1][2] + math.log10(trans_prob[2][l])
    if label1 > label2 :
        return 1
    else :
        return 2


def Viterbi(emit_prob,trans_prob,observe):

    L = len(observe) #観測データの長さ
    K = len(trans_prob)-1 #隠れ状態の種類

    print('観測データ',observe)

###########初期化#######

    V = np.zeros((L+1, K+1), dtype=float)
    ptr= np.zeros((K+1,L+1), dtype=int)
    V[0,] = - sys.maxsize + 1000000
    V[0,0] = 0

##########再帰##########
    i = 1
    l = 1
    while i <= L :
        while l <= K:
            x = int(observe[i-1])-1

            if i == 1 :
                V[i][l] = math.log10(emit_prob[l][x]) + max(V[0][0]+math.log10(trans_prob[0][1])
                                                       ,V[0][0]+math.log10(trans_prob[0][2]))
                ptr[l][i] = compare(V,trans_prob,i,l)

            else :
                V[i][l] = math.log10(emit_prob[l][x]) +max(V[i - 1][1] + math.log10(trans_prob[1][l])
                                                                   , V[i - 1][2] + math.log10(trans_prob[2][l]))
                ptr[l][i] = compare(V, trans_prob, i, l)

            l += 1

        i += 1
        l = 1

########隠れ状態のラベル###########
    i = L
    pre_pi = np.zeros((L+1), dtype=int)
    pre_pi[L]= compare(V,trans_prob,i,l)

    while i > 0:
        pre_pi[i-1] = ptr[pre_pi[i]][i]
        i -= 1

    pre_pi = pre_pi[1:]


#######隠れ状態列###########

    Hidden_status = np.zeros((L+1), dtype=str)
    i = 1
    while i <= L :
        if pre_pi[i-1] == 1 :
            Hidden_status[i]= "F"
        elif pre_pi[i-1] == 2 :
            Hidden_status[i] = "L"
        else :
            Hidden_status[i] = "?"
        i += 1
    Hidden_status = Hidden_status[1:]

    return (10** V[L][pre_pi[L-1]],Hidden_status)



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

    probability,Hidden_status= Viterbi(emit_prob,trans_prob,observe)
    print('隠れ状態　', ''.join(map(str, Hidden_status)))

    print('確率', probability)


main()