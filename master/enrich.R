library(ggplot2)
library(scales)
file_name="/Users/miyakesho/Google ドライブ/master/research/TE_m6A/txt/squire/DESeq2_TE_only_modified.txt"
all_table=read.table(file_name,sep="\t", header=T,encoding="utf-8")
#all_table<-subset(all_table,complete.cases(all_table))
family_list=read.table("/Users/miyakesho/Google ドライブ/master/research/TE_m6A/txt/family_list/Family_list.txt",sep="\t", header=T,encoding="utf-8")

#####upregulated###
all<- family_list
pvalue=0.05
threshold=1


all_expressing=nrow(all_table)
all_m6A=nrow(all_table[all_table$Pvalue<pvalue & all_table$Log2foldchange>threshold,])

pvalue_list <- c()
appear_list <- c()
for (family in family_list$Family){
  family_expressing<-nrow(all_table[all_table$Family==family,])
  family_m6A<-nrow(all_table[all_table$Family==family & all_table$Pvalue<pvalue & all_table$Log2foldchange>threshold,])
  fisher_matrix = matrix(c(family_m6A,family_expressing,all_m6A,all_expressing),nrow=2)
  pvalue_list <- c(pvalue_list,fisher.test(fisher_matrix)$p.value)
  appear_list <- c(appear_list,(family_m6A/family_expressing)/(all_m6A/all_expressing))
}

all$Pvalue<-pvalue_list
all$Times<-appear_list
all$Significant <- all$Pvalue<0.05/nrow(all)
all<-all[all$Times!=0,]
all <- all[order(all$Pvalue,decreasing = F),]
head(all)
p<-ggplot(all,aes(x=log2(Times),y=-log10(Pvalue),color=Significant))+scale_color_manual(values=c("#101507","#bf7340"))
p<-p+geom_point(alpha=0.4,na.rm = TRUE) +theme_bw()+xlim(-5,5)#+ylim(0,30)
#p<-p+layer(data=sub, mapping=aes(x=log2(EsC),y=-log10(Pvals),color=fam),geom="point",stat="identity",position="identity")
plot(p)


#####downregulated###
all<- family_list
pvalue=0.05
threshold=-1


all_expressing=nrow(all_table)
all_m6A=nrow(all_table[all_table$Pvalue<pvalue & all_table$Log2foldchange<threshold,])

pvalue_list <- c()
appear_list <- c()
for (family in family_list$Family){
  family_expressing<-nrow(all_table[all_table$Family==family,])
  family_m6A<-nrow(all_table[all_table$Family==family & all_table$Pvalue<pvalue & all_table$Log2foldchange<threshold,])
  fisher_matrix = matrix(c(family_m6A,family_expressing,all_m6A,all_expressing),nrow=2)
  pvalue_list <- c(pvalue_list,fisher.test(fisher_matrix)$p.value)
  appear_list <- c(appear_list,(family_m6A/family_expressing)/(all_m6A/all_expressing))
}

all$Pvalue<-pvalue_list
all$Times<-appear_list
all$Significant <- all$Pvalue<0.05/nrow(all)
all<-all[all$Times!=0,]
all <- all[order(all$Pvalue,decreasing = F),]
head(all)
p<-ggplot(all,aes(x=log2(Times),y=-log10(Pvalue),color=Significant))+scale_color_manual(values=c("#101507","#bf7340"))
p<-p+geom_point(alpha=0.4,na.rm = TRUE) +theme_bw()+xlim(-10,10)#+ylim(0,30)
#p<-p+layer(data=sub, mapping=aes(x=log2(EsC),y=-log10(Pvals),color=fam),geom="point",stat="identity",position="identity")
plot(p)

