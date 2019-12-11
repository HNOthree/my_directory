
#directory = commandArgs(trailingOnly=TRUE)[1]

directory<-'/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis'
file_name<-paste(directory,"/DESeq2_TE_separated.txt",sep='')
res<-read.table(file_name,head=TRUE)

##Volcanoplot

figname<-paste(directory,"/volcanoplot_TE.png",sep='')
png(figname)

with(subset(res, Padj> 0.05),plot(Log2FoldChange,-log10(Padj),pch=20,main="TE Volcano plot",xlim=c(-15,15),ylim=c(0,160),col=rgb(0,0,0,alpha=0.4)))

with(subset(res, Log2FoldChange> 1 & Padj< 0.05),points(Log2FoldChange,-log10(Padj),pch=20,col=rgb(0,0,1,alpha=0.4)))
with(subset(res, Log2FoldChange< -1 & Padj< 0.05),points(Log2FoldChange,-log10(Padj),pch=20,col=rgb(1,0,0,alpha=0.4)))
#with(subset(res, Family=="Olat_rnd-6_family-6001"),points(Log2FoldChange,-log10(Padj),pch=20,col=rgb(0,1,0,alpha=0.8)))
#with(subset(res, Family=="Olat_rnd-4_family-200"),points(Log2FoldChange,-log10(Padj),pch=20,col=rgb(1,1,0,alpha=0.8)))
#cols=c("green","yellow")
#par(ps=10)
#legend("topleft",legend=c("Olat_rnd-6_family-6001","Olat_rnd-4_family-200"),col=cols,pch=c(1,1))


dev.off()