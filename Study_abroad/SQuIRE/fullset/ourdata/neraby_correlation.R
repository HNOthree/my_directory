library(ggplot2)
library(ggrepel)
library(gridExtra)
Class_list<-c("DNA","LINE","LTR","RC","SINE")
direcroty="/home/smiyake/sho/Fullset/SQuIRE/image/correlation/nearby/"
family_list=read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/superfamily_list.txt", sep="\t", header=T,encoding="utf-8")
layout <- rbind(c(1, 1),
                 c(2, 3),
                 c(4, 5))


#####Distance
Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/Gene_TE_distance.txt", sep="\t", header=T,encoding="utf-8")
Distance<-subset(Table,complete.cases(Table))

length_seq<-c(1000,5000,10000,25000,50000,100000,500000)
all_set=Distance[Distance$Distance<=1000,]
Label=paste("0~",as.character(1000))
all_set<-transform(all_set, distance=Label )
for(i in 1:6){
  subset=Distance[Distance$Distance>length_seq[i] &Distance$Distance<length_seq[i+1],]
  Label=paste(as.character(length_seq[i]),"~")
  Label=paste(Label,as.character(length_seq[i+1]))
  subset<-transform(subset, distance=Label )
  all_set=rbind(all_set,subset)
}
Distance<-all_set
sample<-Distance[Distance$Distance<1000 &Distance$Superfamily=="Ngaro",]
#####Number
Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/Gene_TE_number.txt", sep="\t", header=T,encoding="utf-8")
Number<-subset(Table,complete.cases(Table))
#Distance<-Distance[Distance$Direction_number<=10 & Distance$Direction_number>=-10,]
Number$Direction_number<-as.factor(Number$Direction_number)
Number$Number<-as.factor(Number$Number)

#####TE
Table=read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/DESeq2_TE_separated.txt", sep="\t", header=T,encoding="utf-8")
TE<-subset(Table,complete.cases(Table))
TE_list=read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/TE_family_list.txt", sep="\t", header=T,encoding="utf-8")


p1<-ggplot(TE, aes(x=Log2FoldChange))
p1 <- p1 +geom_histogram(binwidth = 0.4)
p1<-p1+theme_bw()+xlim(-10,10)

p2 <- ggplot(Number, aes(x=Number,y=Abs_delta_LFC))
p2 <- p2 +geom_boxplot()+theme_bw()
p3 <- ggplot(Number, aes(x=Number,y=Log10_distance))
p3 <- p3 +geom_boxplot()+theme_bw()
p4 <- ggplot(Distance, aes(x=Log10_distance,y=Abs_delta_LFC))
p4 <- p4 +geom_point()+theme_bw()+xlim(0,6)
p5 <- ggplot(Distance, aes(x=distance,y=Abs_delta_LFC))
p5 <- p5 +geom_boxplot()+theme_bw()+theme(axis.text.x=element_text(size=rel(0.7), angle=90))

g<-grid.arrange(p1,p2,p3,p4,p5,layout_matrix = layout)
save_name=paste(direcroty,"ALL_distance",sep='')
save_name=paste(save_name,".png",sep='')
ggsave(file=save_name,plot=p5,
       width = 9, height = 6, dpi = 300)

for (i in Class_list){
  T_sub<-TE[TE$Class==i,]
  D_sub<-Distance[Distance$Class==i,]
  N_sub<-Number[Number$Class==i,]
  
  p1<-ggplot(T_sub, aes(x=Log2FoldChange,fill=Superfamily))
  p1 <- p1 +geom_histogram(binwidth = 0.4)
  p1<-p1+theme_bw()+xlim(-10,10)+ theme(legend.position = 'none')
  
  p2 <- ggplot(N_sub, aes(x=Number,y=Abs_delta_LFC))
  p2 <- p2 +geom_boxplot()+theme_bw()
  p3 <- ggplot(N_sub, aes(x=Number,y=Log10_distance))
  p3 <- p3 +geom_boxplot()+theme_bw()
  p4 <- ggplot(D_sub, aes(x=Log10_distance,y=Abs_delta_LFC,colour=Superfamily))
  p4 <- p4 +geom_point()+theme_bw()+xlim(0,6)+ theme(legend.position = 'none')
  p5 <- ggplot(D_sub, aes(x=distance,y=Abs_delta_LFC))
  p5 <- p5 +geom_boxplot()+theme_bw()+theme(axis.text.x=element_text(size=rel(0.7), angle=90))
  
  g<-grid.arrange(p1,p2,p3,p4,p5,layout_matrix = layout)
  save_name=paste(direcroty,"class/",sep='')
  save_name=paste(save_name,i,sep='')
  save_name=paste(save_name,"_distance.png",sep='')
  ggsave(file=save_name,plot=p5,
         width = 9, height = 6, dpi = 300)
  
  
}



for (i in family_list$Superfamily){
  print(i)
  T_sub<-TE[TE$Superfamily==i,]
  D_sub<-Distance[Distance$Superfamily==i,]
  N_sub<-Number[Number$Superfamily==i,]
  if(nrow(T_sub)>0 && nrow(D_sub)>0 && nrow(N_sub)>0){
   p1<-ggplot(T_sub, aes(x=Log2FoldChange,fill=Family))
   p1 <- p1 +geom_histogram(binwidth = 0.4)
   p1<-p1+theme_bw()+xlim(-10,10)+ theme(legend.position = 'none')
  
   p2 <- ggplot(N_sub, aes(x=Number,y=Abs_delta_LFC))
   p2 <- p2 +geom_boxplot()+theme_bw()
   p3 <- ggplot(N_sub, aes(x=Number,y=Log10_distance))
   p3 <- p3 +geom_boxplot()+theme_bw()
   p4 <- ggplot(D_sub, aes(x=Log10_distance,y=Abs_delta_LFC,colour=Family))
   p4 <- p4 +geom_point()+theme_bw()+xlim(0,6)+ theme(legend.position = 'none')
   p5 <- ggplot(D_sub, aes(x=distance,y=Abs_delta_LFC))
   p5 <- p5 +geom_boxplot()+theme_bw()+theme(axis.text.x=element_text(size=rel(0.7), angle=90))
  
   g<-grid.arrange(p1,p2,p3,p4,p5,layout_matrix = layout)
   save_name=paste(direcroty,"superfamily/",sep='')
   save_name=paste(save_name,i,sep='')
   save_name=paste(save_name,".png",sep='')
   ggsave(file=save_name,plot=g,
         width = 9, height = 6, dpi = 300)
  }
  
}
