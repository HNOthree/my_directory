#make a bar plot(percentage)
library(ggplot2)
library(ggrepel)
library(scales)
directory=("/home/smiyake/sho/Fullset/SQuIRE/image/bargraph/")
Class_list<-c('RC', 'LINE', 'LTR', 'SINE', 'DNA')
family_list<-c('Helitron', 'L1', 'ERV1', 'CR1-Zenon', 'tRNA-Core-L2', 'hAT-Charlie', 'Gypsy', 'L2', 'PIF-Harbinger', 'RTE-BovB', 'tRNA', 'TcMar', 'TcMar-Tc1', 'Ngaro', 'hAT-Ac', 'Polinton', 'Rex-Babar', 'Harbinger', 'PIF-Harbinger?', 'EnSpm-CACTA', 'ERV', 'hAT', 'MITE?', 'BEL-Pao', 'Copia', 'Dong-R4', 'PIF-ISL2EU', 'Helitron?', 'Penelope', 'TcMar-Tc2', 'hAT-Tip100', 'I', 'MIR', 'PiggyBac', 'TcMar-Tigger', 'Gypsy-Cigr', 'Zisupton', 'L1-Tx1', 'Crypton', 'MITE', 'P', 'Proto2', 'TcMar-ISRm11', 'Mariner', 'Gypsy?', 'Pao', 'hAT-Charlie?', 'TcMar-Tc1?', 'Copia?', 'ERVK', 'hAT-Ac?', 'tRNA-L2?', 'Academ', 'RTE-X', 'MuDr', 'hAT-Tol2', 'hAT-hAT5', 'DIRS', 'R2-Hero')

Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/DESeq2_TE_separated.txt", sep="\t", header=T,encoding="utf-8")
table<-subset(Table,complete.cases(Table))
male_threshold<-2
female_threshold<--male_threshold
male_specific<-table[table$Log2FoldChange>male_threshold,]
male_specific<-transform(male_specific,Sexuality="Male Specific")
male_specific<-transform(male_specific,Count=1)
female_specific<-table[table$Log2FoldChange<female_threshold,]
female_specific<-transform(female_specific,Sexuality="Female Specific")
female_specific<-transform(female_specific,Count=1)
neutral<-table[table$Log2FoldChange>=female_threshold & table$Log2FoldChange<=male_threshold,]
neutral<-transform(neutral,Sexuality="Neutral")
neutral<-transform(neutral,Count=1)
all_data<-rbind(male_specific,female_specific)
all_data<-rbind(all_data,neutral)
print(nrow(male_specific))
print(nrow(female_specific))
print(nrow(neutral))
for(i in Class_list){
  class_subset<-all_data[all_data$Class==i,]
  g <- ggplot(class_subset, aes(x = Superfamily, y =Count , fill = Sexuality))
  g <- g + geom_bar(stat = "identity", position = "stack")
  g <- g +ggtitle(i)#+ scale_y_continuous(labels = percent)
  g <- g +scale_color_manual(values=c("red", "green", "blue"))
  g <- g+theme_bw() #+coord_flip()
  g <- g+theme(axis.text.x=element_text(size=rel(0.7), angle=90))#+theme(axis.text.x=element_text(size=rel(0.7), angle=90)) rotation
  name<-paste(directory,"Class/X_superfamily",sep='')
  name<-paste(name,i,sep='')
  name<-paste(name,"_barplot.png",sep='')
  ggsave(file = name, plot = g)
  plot(g)
}


for(i in family_list){
  family_subset<-all_data[all_data$Superfamily==i,]
  g <- ggplot(family_subset, aes(x = Family, y =Count , fill = Sexuality))
  g <- g + geom_bar(stat = "identity", position = "stack")
  g <- g +ggtitle(i)#+ scale_y_continuous(labels = percent)
  g <- g +scale_color_manual(values=c("red", "green", "blue"))
  g <- g+theme_bw()#+coord_flip()
  g <- g+theme(axis.text.x=element_text(size=rel(0.7), angle=90))
  name<-paste(directory,"Superfamily/X_family",sep='')
  name<-paste(name,i,sep='')
  name<-paste(name,"_barplot.png")
  ggsave(file = name, plot = g)
  plot(g)
}


##################X axis is log2FoldChange##############
bins=50
window=20
thresholds=c(-10)
i<-1
while(i<=bins){
  print(-10+signif(window*i/bins,digit=3))
  thresholds<-append(thresholds,-10+signif(window*i/bins,digit=3))
  i<-i+1
}

i<-1
all_data=table[table$Log2FoldChange<thresholds[i],]
all_data=transform(all_data,LogFC="~-10")
while(i<length(thresholds)){
  subset=table[table$Log2FoldChange>thresholds[i] & table$Log2FoldChange<thresholds[i+1],]
  if(nrow(subset)>0){
   tag=paste(as.character(signif(thresholds[i],3)),as.character(signif(thresholds[i+1],3)),sep="~")
   subset=transform(subset,LogFC=tag)
   all_data=rbind(all_data,subset)
  }
  i<-i+1
}
subset=table[table$Log2FoldChange>thresholds[i],]
subset=transform(subset,LogFC="10~")
all_data=rbind(all_data,subset)
all_data=transform(all_data,Count=1)
#####all#########
g <- ggplot(all_data, aes(x = LogFC, y =Count , fill = Class))
g <- g + geom_bar(stat = "identity", position = "stack")
g <- g+theme_bw()+theme(legend.key.size =unit(0.5,"line"))#+coord_flip()
g <- g+theme(axis.text.x=element_text(size=rel(0.7), angle=90))#+theme(axis.text.x=element_text(size=rel(0.7), angle=90)) rotation
name<-paste(directory,"ALL_",sep='')
name<-paste(name,"_bargraph_stack.png",sep='')
ggsave(file = name, plot = g)
plot(g)

g <- ggplot(all_data, aes(x = LogFC, y =Count , fill = Class))
g <- g + geom_bar(stat = "identity", position = "fill")+ scale_y_continuous(labels = percent)
g <- g+theme_bw()+theme(legend.key.size =unit(0.5,"line"))#+coord_flip()
g <- g+theme(axis.text.x=element_text(size=rel(0.7), angle=90))#+theme(axis.text.x=element_text(size=rel(0.7), angle=90)) rotation
name<-paste(directory,"ALL_",sep='')
name<-paste(name,"_bargraph_fill.png",sep='')
ggsave(file = name, plot = g)
plot(g)


###BY Class
for(i in Class_list){
  class_subset<-all_data[all_data$Class==i,]
  g <- ggplot(class_subset, aes(x = LogFC, y =Count , fill = Superfamily))
  g <- g + geom_bar(stat = "identity", position = "stack")
  g <- g +ggtitle(i)#+ scale_y_continuous(labels = percent)
  g <- g+theme_bw()+theme(legend.key.size =unit(0.5,"line"))#+coord_flip()
  g <- g+theme(axis.text.x=element_text(size=rel(0.7), angle=90))#+theme(axis.text.x=element_text(size=rel(0.7), angle=90)) rotation
  name<-paste(directory,"Class/X_logFC/",sep='')
  name<-paste(name,i,sep='')
  name<-paste(name,"_bargraph_stack.png",sep='')
  ggsave(file = name, plot = g)
  plot(g)
  
  g <- ggplot(class_subset, aes(x = LogFC, y =Count , fill = Superfamily))
  g <- g + geom_bar(stat = "identity", position = "fill")
  g <- g +ggtitle(i)+ scale_y_continuous(labels = percent)
  g <- g+theme_bw()+theme(legend.key.size =unit(0.5,"line"))#+coord_flip()
  g <- g+theme(axis.text.x=element_text(size=rel(0.7), angle=90))
  name<-paste(directory,"Class/X_logFC/",sep='')
  name<-paste(name,i,sep='')
  name<-paste(name,"_bargraph_fill.png",sep='')
  ggsave(file = name, plot = g)
  plot(g)
}

for(i in family_list){
  family_subset<-all_data[all_data$Superfamily==i,]
  g <- ggplot(family_subset, aes(x = LogFC, y =Count , fill = Family))
  g <- g + geom_bar(stat = "identity", position = "stack")
  g <- g +ggtitle(i)#+ scale_y_continuous(labels = percent)
  g <- g+theme_bw()+theme(legend.key.size =unit(0.5,"line"))#+coord_flip()
  g <- g+theme(axis.text =element_text(size=rel(0.7), angle=90))
  name<-paste(directory,"Superfamily/X_logFC/",sep='')
  name<-paste(name,i,sep='')
  name<-paste(name,"_barplot_stack.png")
  ggsave(file = name, plot = g)
  plot(g)
  
  g <- ggplot(family_subset, aes(x = LogFC, y =Count , fill = Family))
  g <- g + geom_bar(stat = "identity", position = "fill")
  g <- g +ggtitle(i)+ scale_y_continuous(labels = percent)
  g <- g+theme_bw()+theme(legend.key.size =unit(0.5,"line"))#+coord_flip()
  g <- g+theme(axis.text.x=element_text(size=rel(0.7), angle=90))
  name<-paste(directory,"Superfamily/X_logFC/",sep='')
  name<-paste(name,i,sep='')
  name<-paste(name,"_bargraph_fill.png",sep='')
  ggsave(file = name, plot = g)
  plot(g)
}

