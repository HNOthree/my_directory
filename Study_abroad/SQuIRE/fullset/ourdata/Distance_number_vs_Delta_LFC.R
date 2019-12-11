library(ggplot2)
library(ggrepel)
library(gridExtra)
Class_list<-c("DNA","DNA?","LINE","LTR","nonLTR","RC","Retro","SINE","Unknown","Unspecified")
family_list<-c("Academ",'Gypsy', 'Ngaro', 'L1', 'EnSpm-CACTA', 'LINE', 'MITE?', 'TcMar', 'SINE', 'DNA', 'hAT-Ac', 'L2', 'ERV', 'LTR', 'RTE-BovB', 'TcMar-Tc1', 'Polinton', 'Rex-Babar', 'Crypton', 'tRNA-Core-L2', 'PiggyBac', 'CR1-Zenon', 'Retro', 'PIF-Harbinger?', 'PIF-Harbinger', 'hAT-Charlie', 'Unknown', 'BEL-Pao', 'Helitron', 'Dong-R4', 'TcMar-Tc2', 'P', 'L1-Tx1', 'MIR', 'hAT', 'MITE', 'Zisupton', 'hAT-Tip100', 'Proto2', 'RTE-X', 'Copia', 'tRNA-L2?', 'Helitron?', 'hAT-Tol2', 'Penelope', 'Harbinger', 'ERV1', 'TcMar-Tigger', 'hAT-Charlie?', 'hAT-Ac?', 'Mariner', 'Gypsy-Cigr', 'tRNA', 'ERVK', 'TcMar-ISRm11', 'Gypsy?', 'Copia?', 'PIF-ISL2EU', 'MuDr', 'DNA?')
direcroty="/home/smiyake/sho/Fullset/SQuIRE/image/correlation/distance/number/"
Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/Gene_TE_number_purified.txt", sep="\t", header=T,encoding="utf-8")
Distance<-subset(Table,complete.cases(Table))
#Distance<-Distance[Distance$Direction_number<=10 & Distance$Direction_number>=-10,]
Distance$Direction_number<-as.factor(Distance$Direction_number)
Distance$Number<-as.factor(Distance$Number)
Table=read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/DESeq2_TE_separated.txt", sep="\t", header=T,encoding="utf-8")
TE<-subset(Table,complete.cases(Table))
TE_list=read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/TE_family_list.txt", sep="\t", header=T,encoding="utf-8")

##ALL
p2 <- ggplot(Distance, aes(x=Number,y=Abs_delta_LFC))
p2 <- p2 +geom_boxplot()+theme_bw()#+xlim(-10,10)#+xlim(0,500000)
save_name=paste(direcroty,"ALL",sep='')
save_name=paste(save_name,".png",sep='')
ggsave(file=save_name,plot=p2,width = 9, height = 6, dpi = 300)


##Class
for(i in Class_list){
  TE_subset<-TE[TE$Class==i,]
  D_subset<-Distance[Distance$Class==i,]
  if(nrow(D_subset)>0){
    
    p2 <- ggplot(D_subset, aes(x=Number,y=Abs_delta_LFC))
    p2 <- p2 +geom_boxplot()+theme_bw()+ylim(0,10)+ theme(legend.position = 'none')#+xlim(0,500000)
    p3 <- ggplot(D_subset, aes(x=Distance,y=Abs_delta_LFC))
    p3 <- p3 +geom_point()
    p3 <- p3+theme_bw()+xlim(0,500000)
    
    #p3 <- p3 + annotate("text", x=250000, y=9, parse=TRUE,label=correlation)+annotate("text", x=200000, y=10, parse=TRUE,label="Correlation_coefficiency") 
    g<- grid.arrange(p2, p3)
    save_name=paste(direcroty,"Class/",sep='')
    save_name=paste(save_name,i,sep='')
    save_name=paste(save_name,".png",sep='')
    ggsave(file=save_name,plot=g,
           width = 9, height = 6, dpi = 300)
    
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
    p2 <- ggplot(D_subset, aes(x=Number,y=Abs_delta_LFC))
    p2 <- p2 +geom_boxplot()+theme_bw()+ylim(0,10)+ theme(legend.position = 'none')#+xlim(0,500000)
    p3 <- ggplot(D_subset, aes(x=log10_Distance,y=Abs_delta_LFC,colour=Family))
    p3 <- p3 +geom_point()+theme_bw()+ylim(0,10)+xlim(0,5.7)+ theme(legend.position = 'none')
    g<- grid.arrange(p1, p2,p3)
    save_name=paste(direcroty,"superfamily/",sep='')
    save_name=paste(save_name,i,sep='')
    save_name=paste(save_name,".png",sep='')
    ggsave(file=save_name,plot=g,width = 9, height = 6, dpi = 300)
    
  }
}


##family
for (i in TE_list[TE_list$Family,]){
      TE_subset<-TE[TE$Family==i,]
      D_subset<-Distance[Distance$Family==i,]
      if(nrow(D_subset)>5){
        
       if(abs(median(TE_subset$Log2FoldChange))>2 &&abs(mean(TE_subset$Log2FoldChange))>2 ){
         x<-D_subset[,"log10_Distance"]
         y<-D_subset[,"Abs_delta_LFC"]
         correlation=cor(x, y, method="pearson")
         
         p1<-ggplot(TE_subset, aes(x=Log2FoldChange))
         p1 <- p1 + geom_histogram(binwidth = 0.4)
         p1<-p1+theme_bw()+ggtitle(i)+xlim(-10,10)
         p2 <- ggplot(D_subset, aes(x=Number,y=Abs_delta_LFC))
         p2 <- p2 +geom_boxplot()+theme_bw()+ylim(0,10)
         p3 <- ggplot(D_subset, aes(x=log10_Distance,y=Abs_delta_LFC))
         p3 <- p3 +geom_point()+theme_bw()+ylim(0,10)+xlim(0,6)+ theme(legend.position = 'none')
         p3 <- p3 + annotate("text", x=4, y=9, parse=TRUE,label=correlation)+annotate("text", x=3, y=10, parse=TRUE,label="Correlation_coefficiency") 
         g<- grid.arrange(p1, p2,p3)
      
         save_name=paste(direcroty,"family/",sep='')
         save_name=paste(save_name,i,sep='')
         save_name=paste(save_name,".png",sep='')
         ggsave(file=save_name,plot=g,width = 9, height = 6, dpi = 300)
        }
      }
    }

#####################################################
length_seq=c(3,3.7,4.4,4.7,5,5.7)
all_set=Distance[Distance$log10_Distance<=3,]
Label=paste("0~",as.character(3))
all_set<-transform(all_set, distance=Label )
for(i in 1:6){
  subset=Distance[Distance$log10_Distance>length_seq[i] &Distance$log10_Distance<length_seq[i+1],]
  Label=paste(as.character(length_seq[i]),"~")
  Label=paste(Label,as.character(length_seq[i+1]))
  subset<-transform(subset, distance=Label )
  all_set=rbind(all_set,subset)
}

g <- ggplot(all_set, aes(x = distance, y = Abs_delta_LFC))
g <- g + geom_boxplot()+theme_bw()+ylim(0,15)
g <- g+theme(axis.text.x=element_text(size=rel(0.7), angle=90))
save_name=paste(direcroty,"Distance",sep='')
save_name=paste(save_name,".png",sep='')
ggsave(file=save_name,plot=g,width = 9, height = 6, dpi = 300)
plot(g)


##################################
Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/Gene_TE_distance_lfc.txt", sep="\t", header=T,encoding="utf-8")
Distance_gene<-subset(Table,complete.cases(Table))
Distance_gene<-Distance_gene[Distance_gene$Direction_number<=10 & Distance_gene$Direction_number>=-10,]
Distance_gene$Direction_number<-as.factor(Distance_gene$Direction_number)
Distance_gene$Number<-as.factor(Distance_gene$Number)

subset<-Distance_gene[Distance_gene$Superfamily=="ERV1" & Distance_gene$Distance>1000 & Distance_gene$Distance<5000,]
write.csv(subset,"corr.csv",row.names = FALSE)
x<-subset[,"Gene_log2FoldChange"]
y<-subset[,"TE_log2FoldChange"]
correlation=cor(x, y, method="pearson")
print(correlation)

g <- ggplot(Distance_gene, aes(x = Number, y = Delta_LFC))
g <- g + geom_boxplot()+theme_bw()+ylim(-1.0,1.0)
g <- g+theme(axis.text.x=element_text(size=rel(0.7), angle=90))

plot(g)

