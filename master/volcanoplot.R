directory<-'/Users/miyakesho/Google ドライブ/master/research/TE_m6A/txt/squire'
file_name<-paste(directory,"/DESeq2_TE_only.txt",sep='')
res<-read.table(file_name,head=TRUE)
res<-subset(res,complete.cases(res))
##Volcanoplot
head(res)


with(subset(res, pvalue> 0.05),plot(log2FoldChange,-log10(pvalue),pch=20,main="TE Volcano plot",xlim=c(-15,15),ylim=c(0,15)))

with(subset(res, log2FoldChange> 1 & pvalue< 0.05),points(log2FoldChange,-log10(pvalue),pch=20,col="blue"))
with(subset(res, log2FoldChange< -1 & pvalue< 0.05),points(log2FoldChange,-log10(pvalue),pch=20,col="red"))

print(nrow(res[res$pvalue< 0.05,]))
print(nrow(res))
print(nrow(res[res$log2FoldChange>1 & res$pvalue< 0.05,]))
print(nrow(res[res$log2FoldChange<-1 & res$pvalue< 0.05,]))
a=res[res$log2FoldChange< -1 & res$pvalue< 0.05,]
b=res[res$log2FoldChange> 1 & res$pvalue< 0.05,]
