library(ggplot2)
library(ggrepel)
Class_list<-c("DNA","DNA?","LINE","LTR","nonLTR","RC","Retro","SINE","Unknown","Unspecified")
family_list<-c('Gypsy', 'Ngaro', 'L1', 'EnSpm-CACTA', 'LINE', 'MITE?', 'TcMar', 'SINE', 'DNA', 'hAT-Ac', 'L2', 'ERV', 'LTR', 'RTE-BovB', 'TcMar-Tc1', 'Polinton', 'Rex-Babar', 'Crypton', 'tRNA-Core-L2', 'PiggyBac', 'CR1-Zenon', 'Retro', 'PIF-Harbinger?', 'PIF-Harbinger', 'hAT-Charlie', 'Unknown', 'BEL-Pao', 'Helitron', 'Dong-R4', 'TcMar-Tc2', 'P', 'L1-Tx1', 'MIR', 'hAT', 'MITE', 'Zisupton', 'hAT-Tip100', 'Proto2', 'RTE-X', 'Copia', 'tRNA-L2?', 'Helitron?', 'hAT-Tol2', 'Penelope', 'Harbinger', 'ERV1', 'TcMar-Tigger', 'hAT-Charlie?', 'hAT-Ac?', 'Mariner', 'Gypsy-Cigr', 'tRNA', 'ERVK', 'TcMar-ISRm11', 'Gypsy?', 'Copia?', 'PIF-ISL2EU', 'MuDr', 'DNA?')


Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/TE_transcript_merge.txt", sep="\t", header=T,encoding="utf-8")
table<-subset(Table,complete.cases(Table))

g <- ggplot(table, aes(x=Gene_log2FoldChange,y=TE_log2FoldChange,colour=Class))
g <- g + geom_point()　#geom_pointは「散布図で書いてね」と指定するため
g=g+xlim(-15,15)+ylim(-15,15)
#ggsave(file = "upsteram_overlap_genelfc_TElfc_all_.png", plot = g)
plot(g,add=TRUE)
g <- ggplot(table, aes(x=TE_Class,y=Gene_log2FoldChange,colour=TE_Class))
g <- g + geom_boxplot()　#geom_pointは「散布図で書いてね」と指定するため

x<-table[,"Gene_log2FoldChange"]
y<-table[,"TE_log2FoldChange"]
correlation=cor(x, y, method="pearson")
print(correlation)

###group by Class
for( i in Class_list){
  
  subset<-table[table$Class==i ,]
  if(nrow(subset)>0){
    print(i)
    g <- ggplot(subset, aes(x=Gene_log2FoldChange,y=TE_log2FoldChange))
    g <- g +geom_point()
    g=g+xlim(-8,8)+ylim(-8,8)
    #title_name<-paste("upstream female ",i)
    g=g+ggtitle(i)
    #name<- paste(i, "_upstream_overlap_Class_boxplot.png", sep="")
    plot(g)
    #ggsave(file = name, plot = g)
    
    x<-subset[,"Gene_log2FoldChange"]
    y<-subset[,"TE_log2FoldChange"]
    correlation=cor(x, y, method="pearson")
    print(correlation)
  }
}

##Group by Family
for( i in family_list){
  subset<-table[table$Superfamily==i,]
  #subset_non<-subset[subset$Gene_pvalue >= 0.05 | subset$TE_pvalue >= 0.05,]
  #subset_non<-transform(subset_non, status="Not significant" )
  #subset_sig<-subset[subset$Gene_pvalue<0.05 & subset$TE_pvalue<0.05,]
  #subset_sig<-transform(subset_sig, status="Significant" )
  #subsetfig=rbind(subset_non,subset_sig)
  if(nrow(subset)>0){
    print(i)
    g <- ggplot(subset, aes(x=Gene_log2FoldChange,y=TE_log2FoldChange))
    g <- g +geom_point()
    g=g+xlim(-15,15)+ylim(-15,15)
    #title_name<-paste("upstream female ",i)
    g=g+ggtitle(i)
    name<-paste("/home/smiyake/sho/Fullset/SQuIRE/image/correlation/",i,sep='')
    name<- paste(name, "_correlation.png", sep="")
    plot(g)
    ggsave(file = name, plot = g)
    
    x<-subset[,"Gene_log2FoldChange"]
    y<-subset[,"TE_log2FoldChange"]
    correlation=cor(x, y, method="pearson")
    print(correlation)
  }
}
