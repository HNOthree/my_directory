library(ggplot2)
library(ggrepel)
library(scales)
directory = commandArgs(trailingOnly=TRUE)[1]#directory where you want to save the figure

####All you have to do is pushing run botton
hist_func<-function(direcroty){
 file_name<-paste(directory,"/DESeq2_TE_separated.txt",sep='')

 Table = read.table(file_name, sep="\t", header=T,encoding="utf-8")
 table<-subset(Table,complete.cases(Table))
 
 p<-ggplot(table, aes(x=Log2FoldChange,colour=Class,fill=Class))
 p <- p +geom_histogram(bins=50,na.rm = TRUE)
 p<-p+theme_bw()
 
 save_name<-paste(directory,"/TE_lfc_distribution.png",sep='')
 ggsave(file=save_name,plot=p,
        width = 6, dpi = 300)
 }

hist_func(directory)

