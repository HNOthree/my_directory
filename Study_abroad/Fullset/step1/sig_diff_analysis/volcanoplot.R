res_sig<-read.table("/home/smiyake/sho/Fullset/txt/FvsM_sigdiff_TE_separated.txt",head=TRUE)
res<-read.table("/home/smiyake/sho/Fullset/txt/FvsM_gene_TE_analysis_Name_separated_only_TE.txt",head=TRUE)
head(res)


with(subset(res, padj> 0.05),plot(log2foldchange,-log10(pvalue),pch=20,main="TE Volcano plot",xlim=c(-8,8),ylim=c(0,200)))

with(subset(res_sig, log2FoldChange> -1),points(log2FoldChange,-log10(padj),pch=20,col="green"))
with(subset(res_sig, log2FoldChange<1),points(log2FoldChange,-log10(padj),pch=20,col="red"))
