directory<-'/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis'
file_name<-paste(directory,"/DESeq2_TE_separated.txt",sep='')
res<-read.table(file_name,head=TRUE)

##Volcanoplot
head(res)


with(subset(res, Padj> 0.05),plot(Log2FoldChange,-log10(Pvalue),pch=20,main="TE Volcano plot",xlim=c(-15,15),ylim=c(0,150)))

with(subset(res, Log2FoldChange> 1 & Padj< 0.05),points(Log2FoldChange,-log10(Padj),pch=20,col="blue"))
with(subset(res, Log2FoldChange< -1 & Padj< 0.05),points(Log2FoldChange,-log10(Padj),pch=20,col="red"))

