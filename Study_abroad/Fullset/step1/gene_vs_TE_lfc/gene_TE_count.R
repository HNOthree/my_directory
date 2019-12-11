table = read.table("/home/smiyake/sho/Fullset/TEtranscripts/txt/FvsM_gene_TE_analysis_Name_separated_only_TE.txt", sep="\t", header=T,encoding="utf-8")
subtable<-table[table$TE_log2FoldChange> 1 & table$TE_pvalue<0.05 ,]
library(ggplot2)
library(ggrepel)

#all genelfc vs TElfc
g <- ggplot(subtable, aes(x=Gene_log2FoldChange,y=TE_log2FoldChange,colour=TE_Class))
g <- g + geom_point()+geom_abline(slope=1,colour="red")　#geom_pointは「散布図で書いてね」と指定するため
g=g+xlim(-8,8)+ylim(-8,8)
#ggsave(file = "Correlation.png", plot = g)
plot(g,add=TRUE)

#all distance vs count
g <- ggplot(table, aes(x=log2foldchange,fill=Class))
g <- g +  geom_histogram(position = "fill",bins=10)
g <- g +  geom_histogram(position = "stack",bins=20)+theme_bw()
g<-g+xlim(-5,5)
g<-g+xlim(0,100000)+ggtitle("The distribution of TE located downstram of gene")
plot(g)



Class_list<-c("DNA","DNA?","LINE","LTR","nonLTR","RC","Retro","SINE","Unknown","Unspecified")
#Class distance vs count
for( i in Class_list){
  subset<-subtable[(subtable$TE_class==i & subtable$Distance<10000),]
  if(nrow(subset)>0){
  print(i)
  
  g <- ggplot(subset, aes(x=Distance,fill=TE_family))
  g <- g +  geom_histogram(position = "stack",bins=30)
  g<-g+xlim(0,10000)
  name<- paste(i, "_stream.png", sep="")
  plot(g)
  #ggsave(file = name, plot = g)
  }
}

# family distance vs log fc
family_list<-c('Gypsy', 'Ngaro', 'L1', 'EnSpm-CACTA', 'LINE', 'MITE?', 'TcMar', 'SINE', 'DNA', 'hAT-Ac', 'L2', 'ERV', 'LTR', 'RTE-BovB', 'TcMar-Tc1', 'Polinton', 'Rex-Babar', 'Crypton', 'tRNA-Core-L2', 'PiggyBac', 'CR1-Zenon', 'Retro', 'PIF-Harbinger?', 'PIF-Harbinger', 'hAT-Charlie', 'Unknown', 'BEL-Pao', 'Helitron', 'Dong-R4', 'TcMar-Tc2', 'P', 'L1-Tx1', 'MIR', 'hAT', 'MITE', 'Zisupton', 'hAT-Tip100', 'Proto2', 'RTE-X', 'Copia', 'tRNA-L2?', 'Helitron?', 'hAT-Tol2', 'Penelope', 'Harbinger', 'ERV1', 'TcMar-Tigger', 'hAT-Charlie?', 'hAT-Ac?', 'Mariner', 'Gypsy-Cigr', 'tRNA', 'ERVK', 'TcMar-ISRm11', 'Gypsy?', 'Copia?', 'PIF-ISL2EU', 'MuDr', 'DNA?')
for( i in family_list){
  subset<-table[table$TE_family==i & table$TE_pvalue<0.05 & abs(table$TE_log2FoldChange)>1 & table$Distance<10000,]
  if(nrow(subset)>0){
   print(i)
   g <- ggplot(subset, aes(x=Distance,y=Gene_log2FoldChange,label=Gene_name))
   g <- g + geom_point()+ geom_text_repel()
   title_name<-paste("downstream ",i)
   g=g+xlim(0,10000)+ylim(-8,8)+ggtitle(title_name)
   name<- paste(i, "_upstream_DIstance_vs_Genelfc.png", sep="")
   plot(g)
   #ggsave(file = name, plot = g)
  }
 
}
 