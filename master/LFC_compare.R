library(ggplot2)
directory<-'/Users/miyakesho/Google ドライブ/master/research/TE_m6A/txt/squire'
file_name<-paste(directory,"/DESeq2_TE_only_modified.txt",sep='')
data<-read.table(file_name,head=TRUE)
data["label"]="ALL"
SVA=data[data$Superfamily=="Alu",]
SVA["label"]="Alu"
data<- rbind(data,SVA)

t.test(data$Log2foldchange, SVA$Log2foldchange, var.equal=T)

p <- ggplot(data, aes(x=label,y=Log2foldchange))
p <- p +geom_boxplot()+theme_bw()#+xlim(-10,10)#+xlim(0,500000)
plot(p)
save_name=paste(direcroty,"ALL",sep='')
save_name=paste(save_name,".png",sep='')
ggsave(file=save_name,plot=p2,width = 9, height = 6, dpi = 300)


p <- ggplot(data, aes(x=Log2foldchange,y = ..density..,fill=label))+ylab("normalized count")
p <- ggplot(data, aes(x=Log2foldchange,fill=label)) 
p <- p + geom_histogram(binwidth = 0.3,position = "identity", alpha = 0.7)+theme_bw()#+xlim(-10,10)#+xlim(0,500000)
plot(p)

p <- ggplot(SVA, aes(x=Log2foldchange,y = ..density..,colour=Family,fill=Family))+ylab("normalized count")
p <- p + geom_histogram(binwidth = 0.3,position = "stack", alpha = 0.7)+theme_bw()#+xlim(-10,10)#+xlim(0,500000)
plot(p)
