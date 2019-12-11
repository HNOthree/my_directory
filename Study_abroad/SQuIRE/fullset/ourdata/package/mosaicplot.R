directory<-'/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/txt'
file_name<-paste(directory,"/DESeq2_TE_separated.txt",sep='')
res<-read.table(file_name,head=TRUE)
family="Olat_helitron1"

all_red<-nrow(res[res$Log2FoldChange< -1 & res$Pvalue<0.05,])
all_blue<-nrow(res[res$Log2FoldChange> -1 & res$Pvalue<0.05,])
all_black<-nrow(res)-all_red-all_blue

family_data<-res[res$Family==family,]
family_red<-nrow(family_data[family_data$Log2FoldChange< -1 & family_data$Pvalue<0.05,])
family_blue<-nrow(family_data[family_data$Log2FoldChange> -1 & family_data$Pvalue<0.05,])
family_black<-nrow(family_data)-family_red-family_blue

crosstab <- matrix(c(all_blue,family_blue,all_red,family_red,all_black,family_black), nrow = 2, ncol = 3)
colnames(crosstab) <- c("Male","Female","Neutral")
rownames(crosstab) <- c("ALL",family)
mosaicplot(crosstab)

mat<-matrix(c(all_blue,all_red,all_black,family_blue,family_red,family_black),nrow=2,byrow=T)
chisq.test(mat)
