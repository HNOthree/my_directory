import numpy as np
import random
import math
import sys



def status_disicion(s,i,f1,f2,emit_prob,x):
    #print(s,i,f1,f2,emit_prob,x)
    j=0
    px=1

    if i ==1:
        status_can1 =0.5*emit_prob[1][x]
        status_can2=0.5*emit_prob[2][x]
    else:
        while j <i:
         px *=s[j]
         j +=1

        status_can1 = f1*95/100* emit_prob[1][x]+f2*10/100*emit_prob[1][x]
        status_can2 = f1*5/100*emit_prob[2][x]+f2*90/100*emit_prob[2][x]

    if status_can1>status_can2:
        return 'F'
    elif status_can2>status_can1:
        return 'L'
    else:
        return '?'


def emit(fair_emit,loaded_emit,Hidden_state,number):

    Hidden_state=str(Hidden_state)

    if Hidden_state == "F":
        num= random.choices(number, fair_emit)
        return num[0]
    elif Hidden_state == "L":
        num= random.choices(number, loaded_emit)
        return num[0]



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

    return Hidden_status

def posterior(emit_prob,trans_prob,observe):


    L = len(observe)  # 観測データの長さ
    K = len(trans_prob) - 1  # 隠れ状態の種類

    #print('観測データ   ', observe)
    #############前向きアルゴリズム
    F = np.zeros((L + 1, K + 1), dtype=float)
    F[0,] = 0
    F[0, 0] = 1
    s = np.zeros((L + 1), dtype=float)
    Hidden_status = np.zeros((L + 1), dtype=str)

    i = 1
    l = 1
    while i <= L:
        while l <= K:
            x = int(observe[i - 1]) - 1
            if i == 1:
                s[i] = emit_prob[1][x] * (F[0][0] * trans_prob[0][1]) \
                       + emit_prob[2][x] * (F[0][0] * trans_prob[0][2])
                F[i][l] = emit_prob[l][x] * F[i - 1][0] * trans_prob[0][l] / s[i]

            else:
                s[i] = emit_prob[1][x] * (F[i - 1][1] * trans_prob[1][1] + F[i - 1][2] * trans_prob[2][1]) + \
                       emit_prob[2][x] * (F[i - 1][1] * trans_prob[1][2] + F[i - 1][2] * trans_prob[2][2])
                F[i][l] = 1 / s[i] * emit_prob[l][x] * (F[i - 1][1] * trans_prob[1][l] + F[i - 1][2] * trans_prob[2][l])

            l += 1

        i += 1
        l = 1


    ###########初期化#######

    B = np.zeros((L + 1, K + 1), dtype=float)
    B[L,] = 1

    ##########再帰##########

    i = L - 1
    l = 1
    while i >= 1:
        while l <= K:
            x = int(observe[i]) - 1

            B[i][l] = 1 / s[i + 1] * ((emit_prob[1][x] * B[i + 1][1] * trans_prob[l][1]) \
                                      + (emit_prob[2][x] * B[i + 1][2] * trans_prob[l][2]))

            l += 1
        if B[i][1]*F[i][1]>B[i][2]*F[i][2]:
            Hidden_status[i]='F'
        elif B[i][1]*F[i][1]<B[i][2]*F[i][2]:
            Hidden_status[i]='L'
        else:
            Hidden_status[i] = '?'

        i -= 1
        l = 1

    return Hidden_status






def main():
    start_weight=[0.5,0.5]
    fair_weight = [0.95,0.05]
    load_weight = [0.1,0.9]
    fair_emit =[1/6,1/6,1/6,1/6,1/6,1/6]
    loaded_emit=[1/10,1/10,1/10,1/10,1/10,1/2]
    status =['F','L']
    number=[1,2,3,4,5,6]
    count=10
    now=1
    Viterbi_accrate=[]
    posterior_accurate=[]

    while now <=count:
        L=10000
        Hidden_state = ['0']*(L+1)
        Observe = ['0']*(L+1)
        Hidden =str(random.choices(status,start_weight))
        Hidden_state[0]=Hidden[2]
        Observe[0]=emit(fair_emit,loaded_emit,Hidden_state[0],number)

###データ生成
        i=1
        while i<= L:
            if Hidden_state[i-1]=='F':
                Hidden = str(random.choices(status, fair_weight))
                Hidden_state[i] = Hidden[2]
                Observe[i]=emit(fair_emit,loaded_emit,Hidden_state[i],number)

            elif Hidden_state[i-1]=='L':
                Hidden = str(random.choices(status, load_weight))
                Hidden_state[i] = Hidden[2]
                Observe[i]=emit(fair_emit,loaded_emit,Hidden_state[i],number)

            else:
                print('?')
            i += 1
        print('観測データ　',"".join(map(str, Observe)))
        print('正解隠れ状態',"".join(map(str,Hidden_state)))


        emit_prob = [[],
                     [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6],
                     [1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 2]]

        # 遷移確率
        trans_prob = [[0, 0.5, 0.5],
                      [0, 0.95, 0.05],
                      [0, 0.1, 0.9]]

############

############Viterbi
        Viterbi_status = Viterbi(emit_prob, trans_prob, Observe)
        print('Viterbi推定',"".join(map(str, Viterbi_status)))
############

##########posterior_decoding
        #######前向きアルゴリズム
        posterior_status = posterior(emit_prob, trans_prob, Observe)
        posterior_status=posterior_status[1:]
        print('事後推定　　',"".join(map(str, posterior_status)))




#########accuracy
        hit=0
        i=0
        while i !=L+1:
            if Viterbi_status[i]== Hidden_state[i]:
                hit+= 1
            i +=1

        Viterbi_accrate.append(hit/(L+1))

        hit = 0
        i = 0
        while i != L + 1:
            if posterior_status[i] == Hidden_state[i]:
                hit += 1
            i += 1
        posterior_accurate.append(hit/(L+1))
        now +=1
    print('Viterbi',Viterbi_accrate)
    print('Posterior',posterior_accurate)
    Viterbi_sum=0
    posterior_sum=0
    for i in Viterbi_accrate:
        Viterbi_sum += i

    for j in posterior_accurate:
        posterior_sum+=j
    print('Viterbi_accurate' ,Viterbi_sum/count)
    print('Posterior_accurate', posterior_sum / count)
main()
