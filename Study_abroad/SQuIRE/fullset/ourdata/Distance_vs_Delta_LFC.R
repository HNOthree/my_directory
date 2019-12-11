library(ggplot2)
library(ggrepel)
library(gridExtra)
Class_list<-c("DNA","DNA?","LINE","LTR","nonLTR","RC","Retro","SINE","Unknown","Unspecified")
family_list<-c('Gypsy', 'Ngaro', 'L1', 'EnSpm-CACTA', 'LINE', 'MITE?', 'TcMar', 'SINE', 'DNA', 'hAT-Ac', 'L2', 'ERV', 'LTR', 'RTE-BovB', 'TcMar-Tc1', 'Polinton', 'Rex-Babar', 'Crypton', 'tRNA-Core-L2', 'PiggyBac', 'CR1-Zenon', 'Retro', 'PIF-Harbinger?', 'PIF-Harbinger', 'hAT-Charlie', 'Unknown', 'BEL-Pao', 'Helitron', 'Dong-R4', 'TcMar-Tc2', 'P', 'L1-Tx1', 'MIR', 'hAT', 'MITE', 'Zisupton', 'hAT-Tip100', 'Proto2', 'RTE-X', 'Copia', 'tRNA-L2?', 'Helitron?', 'hAT-Tol2', 'Penelope', 'Harbinger', 'ERV1', 'TcMar-Tigger', 'hAT-Charlie?', 'hAT-Ac?', 'Mariner', 'Gypsy-Cigr', 'tRNA', 'ERVK', 'TcMar-ISRm11', 'Gypsy?', 'Copia?', 'PIF-ISL2EU', 'MuDr', 'DNA?')
direcroty="/home/smiyake/sho/Fullset/SQuIRE/image/correlation/distance/"

Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/SQuIRE_gene_TE_distance.txt", sep="\t", header=T,encoding="utf-8")
Distance<-subset(Table,complete.cases(Table))
Table=read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/DESeq2_TE_separated.txt", sep="\t", header=T,encoding="utf-8")
TE<-subset(Table,complete.cases(Table))
TE_list=read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/TE_family_list.txt", sep="\t", header=T,encoding="utf-8")

##ALL
p1<-ggplot(TE, aes(x=Log2FoldChange,fill=Class))
p1 <- p1 + geom_histogram(binwidth = 0.4)
p1<-p1+theme_bw()+xlim(-10,10)
p2 <- ggplot(Distance, aes(x=Distance,y=Delta_LFC,colour=Class))
p2 <- p2 +geom_point()+theme_bw()+ylim(-10,10)+ theme(legend.position = 'none')#+xlim(0,500000)
g<- grid.arrange(p1, p2)
save_name=paste(direcroty,"ALL",sep='')
save_name=paste(save_name,".png",sep='')
ggsave(file=save_name,plot=g,width = 9, height = 6, dpi = 300)

##Class
for(i in Class_list){
  TE_subset<-TE[TE$Class==i,]
  D_subset<-Distance[Distance$Class==i,]
  if(nrow(D_subset)>0){
   p1<-ggplot(TE_subset, aes(x=Log2FoldChange,fill=Superfamily))
   p1 <- p1 + geom_histogram(binwidth = 0.4)+ theme(legend.position = 'none')
   p1<-p1+theme_bw()+ggtitle(i)+xlim(-10,10)
   p2 <- ggplot(D_subset, aes(x=Distance,y=Delta_LFC,colour=Superfamily))
   p2 <- p2 +geom_point()+theme_bw()+ylim(-10,10)+ theme(legend.position = 'none')#+xlim(0,500000)
   g<- grid.arrange(p1, p2)
   save_name=paste(direcroty,"Class/",sep='')
   save_name=paste(save_name,i,sep='')
   save_name=paste(save_name,".png",sep='')
   ggsave(file=save_name,plot=g,width = 9, height = 6, dpi = 300)
   
  }
}

###Superfamily
for(i in family_list){
  TE_subset<-TE[TE$Superfamily==i,]
  D_subset<-Distance[Distance$Superfamily==i,]
  if(nrow(D_subset)>0){
    p1<-ggplot(TE_subset, aes(x=Log2FoldChange,fill=Family))
    p1 <- p1 + geom_histogram(binwidth = 0.4)
    p1<-p1+theme_bw()+ggtitle(i)+xlim(-10,10)+ theme(legend.position = 'none')
    p2 <- ggplot(D_subset, aes(x=Distance,y=Delta_LFC,colour=Family))
    p2 <- p2 +geom_point()+theme_bw()+ylim(-10,10)+ theme(legend.position = 'none')#+xlim(0,500000)
    g<- grid.arrange(p1, p2)
    save_name=paste(direcroty,"superfamily/",sep='')
    save_name=paste(save_name,i,sep='')
    save_name=paste(save_name,".png",sep='')
    ggsave(file=save_name,plot=g,width = 9, height = 6, dpi = 300)
    
  }
}


###family
for (i in TE_list[TE_list$Family,]){
  TE_subset<-TE[TE$Family==i,]
  D_subset<-Distance[Distance$Family==i,]
  if(nrow(D_subset)>5){
    x<-D_subset[,"Distance"]
    y<-D_subset[,"Delta_LFC"]
    correlation=cor(x, y, method="pearson")
  
    if(abs(correlation)>0.5){
      p1<-ggplot(TE_subset, aes(x=Log2FoldChange))
      p1 <- p1 + geom_histogram(binwidth = 0.4)
      p1<-p1+theme_bw()+ggtitle(i)+xlim(-10,10)
      p2 <- ggplot(D_subset, aes(x=Distance,y=Delta_LFC))
      p2 <- p2 +geom_point()+theme_bw()+ylim(-10,10)+xlim(0,300000)
      p2 <- p2 + annotate("text", x=250000, y=9, parse=TRUE,label=correlation)+annotate("text", x=200000, y=10, parse=TRUE,label="Correlation_coefficiency") 
      g<- grid.arrange(p1, p2)
      
      save_name=paste(direcroty,"family/",sep='')
      save_name=paste(save_name,i,sep='')
      save_name=paste(save_name,".png",sep='')
      ggsave(file=save_name,plot=g,width = 9, height = 6, dpi = 300)
      }
  }
}
