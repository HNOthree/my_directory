import argparse
import numpy as np
import pandas as pd
import random
global result
def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-local','-l', default=False, action='store_true',help='do local alignment')
    parser.add_argument('-amino','-a', default=False, action='store_true',help='do amino acid alignment')

    args = parser.parse_args()

    if args.local:

     if args.amino:
      return 'local_amino'

     else :
         return 'local'

    if args.amino:
        return 'amino'
    else :
        return 'DNA'


def generate_seq(length) :
    if result == 'amino' or result == 'local_amino':
     seq = 'ACDEFGHIKLMNPQRSTVWY'
    else:
     seq ='ATGC'


    sr = random.SystemRandom()

    return ''.join([sr.choice(seq) for i in range(length)])


def gap (seq1,seq2,j,i):

    if result == 'amino' or result == 'local_amino':
        gap_matrix = pd.read_csv("BLOSUM50.csv", header=0, index_col=0)

        if j == 0 or i == 0:
            return -8

    else :
        gap_matrix = pd.read_csv("DNA.csv",header=0,index_col=0)

        if j == 0 or i == 0 :
            return -2

    gap_cost = gap_matrix[seq1][seq2]
    if i == 1 and j == 1:
        print('置換行列')
        print(gap_matrix)
    return gap_cost


def comparing(Compare_ij,Compare_i,Compare_j):
    if result == 'local' or result == 'local_amino' :   #局所アラインメント

        if max(0,Compare_ij, Compare_i, Compare_j) == Compare_ij:
            trace_matrix = 3
            maximum = Compare_ij
        elif max(0,Compare_ij, Compare_i, Compare_j) == Compare_i:
            trace_matrix = 1
            maximum = Compare_i
        elif max(0,Compare_ij, Compare_i, Compare_j) == Compare_j:
            trace_matrix = 2
            maximum = Compare_j
        else :
            trace_matrix = 0
            maximum = 0
    else :#大域アラインメント
        max(Compare_ij, Compare_i, Compare_j)
        if max(Compare_ij, Compare_i, Compare_j) == Compare_ij:
            trace_matrix = 3
            maximum = Compare_ij
        elif max(Compare_ij, Compare_i, Compare_j) == Compare_i:
            trace_matrix = 1
            maximum = Compare_i
        else:
            trace_matrix = 2
            maximum = Compare_j
    return maximum,trace_matrix

def DP (seq1,seq2) :
 i = 0
 j = 0
 n = len(seq1)
 m = len(seq2)
 score_matrix = np.zeros((m,n),dtype=int)
 trace_matrix = np.zeros((m,n),dtype=int) #トレースバック行列の作成
 if result == 'DNA'or result == 'local':
     d_cost = -2
 elif result == 'amino' or result == 'local_amino':
     d_cost = -8


 Compare_i = 0
 Compare_j = 0
 Compare_ij = 0

 while i<m :
     while j<n :
         if j == 0 and i == 0 :

                score_matrix[i][j] = 0  #初期化、0,0のスコア
                trace_matrix[i][j] = 0
                j += 1
         elif i == 0 :
             if result == 'local' or result == 'local_amino':
                 score_matrix[i][j] = 0
                 trace_matrix[i][j] = 0  # 局所アラインメントの初期化
                 j += 1
             else:
                score_matrix[i][j] = j * gap(seq1[j],seq2[i],j,i) #1行目
                trace_matrix[i][j] = 1
                j += 1
         elif j == 0 :
             if result == 'local' or result == 'local_amino':
                 score_matrix[i][j] = 0
                 trace_matrix[i][j] = 0  # 局所アラインメントの初期化
                 j += 1
             else:
                score_matrix[i][j] = score_matrix[i-1][j] + gap(seq1[j],seq2[i],j,i) #1列目
                trace_matrix[i][j] = 2
                j += 1
         else :

          Compare_ij = score_matrix[i-1][j-1] + gap(seq1[j],seq2[i],j,i)

          Compare_i = score_matrix[i-1][j] + d_cost
          Compare_j = score_matrix[i][j-1] + d_cost
          score_matrix[i][j],trace_matrix[i][j]= comparing(Compare_ij,Compare_i,Compare_j) #最大値を用いたi,jのスコア

          j += 1
     i += 1
     j = 0
 return score_matrix,trace_matrix


def traceback (seq1,seq2,score_matrix,trace_matrix):
 new_rseq1 = ''
 new_rseq2 = ''



 #局所アラインメント
 if result == 'local'or result == 'local_amino':

   l=np.argmax(score_matrix)
   x = len(seq1)
   y = len(seq2)
   m = l // x
   n = l%x
   print('最大値index')
   print(n,m,score_matrix[m][n])


   while trace_matrix[m][n] != 0 :
       if trace_matrix[m][n] == 3:
           new_rseq1 = new_rseq1 + seq1[n]
           new_rseq2 = new_rseq2 + seq2[m]
           n -= 1
           m -= 1

       elif trace_matrix[m][n] == 2:
           new_rseq1 = new_rseq1 + seq1[n]
           new_rseq2 = new_rseq2 + '-'
           n -= 1
       elif trace_matrix[m][n] == 1:
           new_rseq1 = new_rseq1 + '-'
           new_rseq2 = new_rseq2 + seq2[m]
           m -= 1


#大域アラインメント
 else:
  n = len(seq1)-1
  m = len(seq2)-1



  while n>0 and m>0 :
   if  trace_matrix[m][n] == 3:
         new_rseq1 = new_rseq1 + seq1[n]
         new_rseq2 = new_rseq2 + seq2[m]
         n -= 1
         m -= 1

   elif trace_matrix[m][n] == 2:
         new_rseq1 = new_rseq1 + seq1[n]
         new_rseq2 = new_rseq2 + '-'
         n -= 1
   else :
         new_rseq1 = new_rseq1 + '-'
         new_rseq2 = new_rseq2 + seq2[m]
         m -= 1
  while True:
     if n==0 and m ==0 :
         break
     elif n > 0 :
         new_rseq1 = new_rseq1 + seq1[n]
         new_rseq2 = new_rseq2 + '-'
         n -=1
     elif m > 0 :
         new_rseq1 = new_rseq1 + '-'
         new_rseq2 = new_rseq2 + seq2[m]
         m -= 1
     else :
         print(n,m)

 new_seq1 = new_rseq1[::-1]
 new_seq2 = new_rseq2[::-1]
 return new_seq1,new_seq2


def main():
 #配列を入力する場合
 seq1 = '0'+input ('アラインメントする最初の配列:')
 seq2 = '0'+input ('アラインメントする二番目の配列:')
 '''
 #ランダムに配列生成する場合
 length = int(input('最長配列の記入'))
 length = 4000
 seq1 = '0' + generate_seq(length)
 seq2 = '0' + generate_seq(length)
 '''
 print(seq1[1:])
 print(seq2[1:])
 score_matrix,trace_matrix = DP(seq1,seq2)
 print('スコア行列')
 print(score_matrix)
 print('トレース行列')
 print(trace_matrix)
 new_seq1,new_seq2=traceback(seq1,seq2,score_matrix,trace_matrix)
 print('アラインメントされた配列')
 print(new_seq1)
 print(new_seq2)

result = parser()
print(result)
main();