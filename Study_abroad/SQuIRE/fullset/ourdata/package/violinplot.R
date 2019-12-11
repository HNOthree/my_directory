library(ggplot2)
library(ggrepel)
library(gridExtra)
#library(vioplot)

directory = commandArgs(trailingOnly=TRUE)[1]

myfunc<-function(directory){

 load_name<-paste(directory,"/TE_in_enrichregion.txt",sep='')
 Table=read.table(load_name, sep="\t", header=T,encoding="utf-8")
 TE<-subset(Table,complete.cases(Table))


 p<-ggplot(TE, aes(x=Sexuality,y=Log2FoldChange,colour=Sexuality))
 p <- p +geom_violin()+geom_boxplot(width=.1,outer.colour=NA)
 p<-p+theme_bw()+coord_flip()+scale_color_manual(values=c("#2dfc03","#fc2003","#03b1fc","#fc03eb"))
 save_name<-paste(directory,"/violinplot.png",sep='')
 ggsave(file=save_name,plot=p,width = 6, dpi = 300)

 p<-ggplot(TE, aes(x=Log2FoldChange,fill=Sexuality,colour=Sexuality))
 #p<-p+geom_histogram()
 p <- p +geom_histogram(position = "dodge", alpha = 0.4)
 p<-p+theme_bw()+scale_fill_manual(values=c("#2dfc03","#fc2003","#03b1fc","#fc03eb"))+scale_color_manual(values=c("#2dfc03","#fc2003","#03b1fc","#fc03eb"))
 save_name<-paste(directory,"/histgram_separated_enrichregion.png",sep='')
 ggsave(file=save_name,plot=p,width =8, dpi = 300 )
}

myfunc(directory)
