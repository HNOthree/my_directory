library(ggplot2)
library(ggrepel)
Class_list<-c("DNA","DNA?","LINE","LTR","nonLTR","RC","Retro","SINE","Unknown","Unspecified")
family_list<-c('Gypsy', 'Ngaro', 'L1', 'EnSpm-CACTA', 'LINE', 'MITE?', 'TcMar', 'SINE', 'DNA', 'hAT-Ac', 'L2', 'ERV', 'LTR', 'RTE-BovB', 'TcMar-Tc1', 'Polinton', 'Rex-Babar', 'Crypton', 'tRNA-Core-L2', 'PiggyBac', 'CR1-Zenon', 'Retro', 'PIF-Harbinger?', 'PIF-Harbinger', 'hAT-Charlie', 'Unknown', 'BEL-Pao', 'Helitron', 'Dong-R4', 'TcMar-Tc2', 'P', 'L1-Tx1', 'MIR', 'hAT', 'MITE', 'Zisupton', 'hAT-Tip100', 'Proto2', 'RTE-X', 'Copia', 'tRNA-L2?', 'Helitron?', 'hAT-Tol2', 'Penelope', 'Harbinger', 'ERV1', 'TcMar-Tigger', 'hAT-Charlie?', 'hAT-Ac?', 'Mariner', 'Gypsy-Cigr', 'tRNA', 'ERVK', 'TcMar-ISRm11', 'Gypsy?', 'Copia?', 'PIF-ISL2EU', 'MuDr', 'DNA?')

names=c("0_500","500_1000","1000_5000","5000_10000","10000_50000")
for (name in names){
  Name<-sprintf("/home/smiyake/sho/Fullset/txt/step2/upstream_%s_groupby_family.txt",name)
  Table = read.table(Name, sep="\t", header=T,encoding="utf-8")
  table<-subset(Table,complete.cases(Table))
  
  g <- ggplot(table, aes(x=Gene_log2FC_mean,y=TE_log2FC,colour=TE_class))
  g <- g + geom_point()+scale_fill_manual(Class_list)　#geom_pointは「散布図で書いてね」と指定するため
  g=g+xlim(-8,8)+ylim(-8,8)+ggtitle(name)
  output_name<-paste(name,"_upsteram_genelfc_TElfc_groupbyfamily.png")
  ggsave(file = output_name, plot = g)
  plot(g,add=TRUE)
  
  x<-table[,"Gene_log2FC_mean"]
  y<-table[,"TE_log2FC"]
  correlation=cor(x, y, method="pearson")
  print(correlation)
}
for( i in Class_list){
  
  subset<-table[table$TE_Class==i ,]
  if(nrow(subset)>0){
    print(i)
    g <- ggplot(subset, aes(x=gene_log2FC_mean,y=TE_log2FC,colour=TE_superfamily))
    g <- g +geom_point()+xlim(-8,8)+ylim(-8,8)
    #title_name<-paste("upstream female ",i)
    g=g+ggtitle(i)
    name<- paste(i, "_upstream_overlap_Class_groupbyfamily.png", sep="")
    plot(g)
    ggsave(file = name, plot = g)
    
    x<-subset[,"gene_log2FC_mean"]
    y<-subset[,"TE_log2FC"]
    correlation=cor(x, y, method="pearson")
    print(correlation)
  }
}
