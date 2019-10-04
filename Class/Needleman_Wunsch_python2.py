# coding: UTF-8
import numpy as np



def DP (d_gap,seq1,seq2,ss_score,sd_score) :
 i = 0
 j = 0
 n = len(seq1)
 m = len(seq2)
 score_matrix = np.zeros((m,n),dtype=int)
 trace_matrix = np.zeros((m,n),dtype=int) #トレースバック行列の作成
 Compare_i = 0
 Compare_j = 0
 Compare_ij = 0

 while(i<m):
     while(j<n):
         if j == 0 and i == 0 :
          score_matrix[i][j] = 0  #0,0のスコア
          trace_matrix[i][j] = 0
          j += 1
         elif i == 0 :
          score_matrix[i][j] = -j * d_gap #1行目
          trace_matrix[i][j] = 1
          j += 1
         elif j == 0 :
          score_matrix[i][j] = score_matrix[i-1][j] - d_gap #1列目
          trace_matrix[i][j] = 2
          j += 1
         else :
          if seq1[j] == seq2[i] :
              Compare_ij = score_matrix[i-1][j-1] + ss_score#同一塩基
          else :
              Compare_ij = score_matrix[i-1][j-1] + sd_score #異なる塩基
          Compare_i = score_matrix[i-1][j] - d_gap
          Compare_j = score_matrix[i][j-1] - d_gap
          score_matrix[i][j]= max(Compare_ij,Compare_i,Compare_j) #最大値を用いたi,jのスコア
          if max(Compare_ij,Compare_i,Compare_j) == Compare_ij:
              trace_matrix[i][j] = 3
          elif max(Compare_ij,Compare_i,Compare_j) == Compare_i :
              trace_matrix[i][j] = 1
          else :
              trace_matrix[i][j] = 2
          j += 1
     i += 1
     j = 0
 return score_matrix,trace_matrix

def traceback (seq1,seq2,trace_matrix):
 n = len(seq1)-1
 m = len(seq2)-1
 L = max(n,m) #0付加補正

 new_seq1 = np.zeros((L),dtype=str) #アラインメントされた配列
 new_seq2 = np.zeros((L),dtype=str) #アラインメントされた配列
 while (n>0 and m>0) :
  if  trace_matrix[m][n] == 3:
         new_seq1[L-1] = seq1[n]
         new_seq2[L-1] = seq2[m]
         n -= 1
         m -= 1
         L -= 1
  elif trace_matrix[m][n] == 2:
         new_seq1[L-1] = seq1[n]
         new_seq2[L-1] = '-'
         n -= 1
         L -= 1
  else :
         new_seq1[L-1] = '-'
         new_seq2[L-1] = seq2[m]
         m -= 1
         L -= 1
 return new_seq1,new_seq2


d_gap = input('ギャップコストの記入:')
ss_score = input('同一塩基だった時の置換スコアの記入:')
sd_score = input('異なる塩基だった時の置換スコアの記入:')
seq1 = '0'+raw_input ('アラインメントする最初の配列:')
seq2 = '0'+raw_input ('アラインメントする二番目の配列:')
score_matrix,trace_matrix = DP(d_gap,seq1,seq2,ss_score,sd_score)
print('スコア行列')
print(score_matrix)
new_seq1,new_seq2=traceback(seq1,seq2,trace_matrix)
print('アラインメントされた配列')
print(new_seq1)
print(new_seq2)