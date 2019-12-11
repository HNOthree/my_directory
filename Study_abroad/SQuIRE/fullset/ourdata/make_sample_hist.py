import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
data=pd.read_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/DESeq2_TE_separated.txt",sep='\t')

m_number=data[data.Log2FoldChange>1]
m_number=m_number[m_number.Pvalue<0.05]
print(len(m_number))
f_number=data[data.Log2FoldChange<-1]
f_number=f_number[f_number.Pvalue<0.05]
print(len(f_number))
TE=[]
for i in range(len(data)):
 parameter=np.random.rand()
 if(parameter<float(len(m_number))/len(data)):
  mu, sigma = 4,1
  TE.append( mu + sigma * np.random.randn())
 elif(parameter>=float(len(m_number)/len(data)) and parameter<float(len(m_number)/len(data))+float(len(f_number))/len(data)):
  mu, sigma = -4,2
  TE.append(mu+sigma * np.random.randn())
 else:
  mu, sigma = 0.5,1.5
  TE.append( mu + sigma * np.random.randn())
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
print(len(TE),len(data.Log2FoldChange))
ax.hist(data.Log2FoldChange.dropna(),bins=50,normed=True,alpha=0.5,label="Result")
ax.hist(TE, bins=50, normed=True,alpha=0.5,label="Gaussian model")
ax.set_title('The distribution of gaussian mixuture model')
ax.set_xlabel('Log2 fold change')
ax.set_ylabel('freq')
ax.set_xlim(-10,10)
ax.legend(loc='upper left')
fig.savefig("/home/smiyake/sho/Fullset/SQuIRE/image/gaussian_mixture.png",dpi=300)
fig.show()



fig = plt.figure()
ax = fig.add_subplot(1,1,1)
sigma = [1,2,1.5]
muu = [4,-4,0.5]
x = np.arange(-10., 10., 0.01)     #-8から８まで0.01刻みの配列

for i in zip(sigma,muu):     #zipは同時にループしてくれます
    y = (1 / np.sqrt(2 * np.pi * i[0] ) ) * np.exp(-(x - i[1]) ** 2 / (2 * i[0]) )     #ガウス分布の公式
    ax.plot(x, y)     #x, yをplotします
    ax.grid()     #グリット線
    ax.set_xlabel('Log2 fold change')     #x軸のラベル
    ax.set_ylabel('Frequency')     #y軸のラベル
    ax.legend(["σ=1.0 μ=4.0", "σ=2.0 μ=-4.0","σ=1.5 μ=0.5"],loc="upper left")   #凡例を左上に表示
fig.savefig("/home/smiyake/sho/Fullset/SQuIRE/image/Gaussian.png",dpi=300)
fig.show()

test=stats.mannwhitneyu(TE, data.Log2FoldChange)
print(test)
