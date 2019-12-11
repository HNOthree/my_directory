library(ggplot2)
library(ggrepel)
Class_list<-c("DNA","DNA?","LINE","LTR","nonLTR","RC","Retro","SINE","Unknown","Unspecified")
family_list<-c('Gypsy', 'Ngaro', 'L1', 'EnSpm-CACTA', 'LINE', 'MITE?', 'TcMar', 'SINE', 'DNA', 'hAT-Ac', 'L2', 'ERV', 'LTR', 'RTE-BovB', 'TcMar-Tc1', 'Polinton', 'Rex-Babar', 'Crypton', 'tRNA-Core-L2', 'PiggyBac', 'CR1-Zenon', 'Retro', 'PIF-Harbinger?', 'PIF-Harbinger', 'hAT-Charlie', 'Unknown', 'BEL-Pao', 'Helitron', 'Dong-R4', 'TcMar-Tc2', 'P', 'L1-Tx1', 'MIR', 'hAT', 'MITE', 'Zisupton', 'hAT-Tip100', 'Proto2', 'RTE-X', 'Copia', 'tRNA-L2?', 'Helitron?', 'hAT-Tol2', 'Penelope', 'Harbinger', 'ERV1', 'TcMar-Tigger', 'hAT-Charlie?', 'hAT-Ac?', 'Mariner', 'Gypsy-Cigr', 'tRNA', 'ERVK', 'TcMar-ISRm11', 'Gypsy?', 'Copia?', 'PIF-ISL2EU', 'MuDr', 'DNA?')

#upstream NOT overlap
Table = read.table("/home/smiyake/sho/Fullset/txt/merge_transcript_TE_upstream_50000_lfc.txt", sep="\t", header=T,encoding="utf-8")
table<-subset(Table,complete.cases(Table))
maletable<-table[table$TE_log2FoldChange > 1 & table$TE_pvalue < 0.05 &table$Distance < 1000 ,]
maletable<-transform(maletable, Sexuality_Specificity="Male" )
femaletable<-table[table$TE_log2FoldChange< -1 & table$TE_pvalue<0.05 &table$Distance < 1000,]
femaletable<-transform(femaletable, Sexuality_Specificity="Female" )
background_table<-table[table$TE_pvalue>0.05  &table$Distance < 1000,]
background_table<-transform(background_table, Sexuality_Specificity="Neutral" )
all_table=rbind(maletable,femaletable)
all_table=rbind(all_table,background_table)

######all###############
g <- ggplot(all_table, aes(x=Gene_log2FoldChange,y=TE_log2FoldChange,colour=TE_Class))
g <- g + geom_point()　#geom_pointは「散布図で書いてね」と指定するため
g=g+xlim(-8,8)+ylim(-8,8)
ggsave(file = "upsteram_overlap_genelfc_TElfc_all_.png", plot = g)
plot(g,add=TRUE)

g <- ggplot(table, aes(x=TE_Class,y=Gene_log2FoldChange,colour=TE_Class))
g <- g + geom_boxplot()　#geom_pointは「散布図で書いてね」と指定するため

#ggsave(file = "upsteram_overlap_histgram_male.png", plot = g)
plot(g,add=TRUE)


#upstream overlap
Table = read.table("/home/smiyake/sho/Fullset/upstream_transcripts_TE_overlap_lfc.txt", sep="\t", header=T,encoding="utf-8")
table<-subset(Table,complete.cases(Table))
maletable<-table[table$TE_log2FoldChange > 1 & table$TE_pvalue < 0.05 ,]
maletable<-transform(maletable, Sexuality_Specificity="Male" )
femaletable<-table[table$TE_log2FoldChange< -1 & table$TE_pvalue<0.05  ,]
femaletable<-transform(femaletable, Sexuality_Specificity="Female" )
background_table<-table[table$TE_pvalue>0.05 ,]
background_table<-transform(background_table, Sexuality_Specificity="Neutral" )
all_table=rbind(maletable,femaletable)
all_table=rbind(all_table,background_table)

######all###############
g <- ggplot(all_table, aes(x=Gene_log2FoldChange,y=TE_log2FoldChange,colour=TE_Class))
g <- g + geom_point()　#geom_pointは「散布図で書いてね」と指定するため
g=g+xlim(-8,8)+ylim(-8,8)
#ggsave(file = "upsteram_overlap_genelfc_TElfc_all_.png", plot = g)
plot(g,add=TRUE)

g <- ggplot(table, aes(x=TE_Class,y=Gene_log2FoldChange,colour=TE_Class))
g <- g + geom_boxplot()　#geom_pointは「散布図で書いてね」と指定するため

#ggsave(file = "upsteram_overlap_histgram_male.png", plot = g)
plot(g,add=TRUE)

x<-all_table[,"Gene_log2FoldChange"]
y<-all_table[,"TE_log2FoldChange"]
correlation=cor(x, y, method="pearson")
print(correlation)



g <- ggplot(sig_table, aes(x=Gene_log2FoldChange,y=TE_log2FoldChange,colour=TE_Class))
g <- g + geom_point()　#geom_pointは「散布図で書いてね」と指定するため
g=g+xlim(-8,8)+ylim(-8,8)
#ggsave(file = "upsteram_overlap_genelfc_TElfc.png", plot = g)
plot(g,add=TRUE)
x<-sig_table[,"Gene_log2FoldChange"]
y<-sig_table[,"TE_log2FoldChange"]
correlation=cor(x, y, method="spearman")
print(correlation)

###male###########################
#all hisgram
g <- ggplot(maletable, aes(x=Gene_log2FoldChange))
g <- g + geom_histogram(aes(fill=TE_Class))　#geom_pointは「散布図で書いてね」と指定するため
g=g+xlim(-8,8)+scale_fill_manual(values=c("#ff7f50", "orange", "#7cfc00","#6495ed","#ffb6c1","red",'#6b8e23'))
ggsave(file = "upsteram_overlap_histgram_male_.png", plot = g)
plot(g,add=TRUE)

g <- ggplot(maletable, aes(x=TE_Class,y=Gene_log2FoldChange,colour=TE_Class))
g <- g + geom_boxplot()　#geom_pointは「散布図で書いてね」と指定するため
ggsave(file = "upsteram_overlap_boxplot_male.png", plot = g)
plot(g,add=TRUE)

###female###########################
#all hisgram
g <- ggplot(femaletable, aes(x=Gene_log2FoldChange))
g <- g + geom_histogram(aes(fill=TE_Class))　#geom_pointは「散布図で書いてね」と指定するため
g=g+xlim(-8,8)+scale_fill_manual(values=c("#ff7f50", "orange", "#7cfc00"))
ggsave(file = "upsteram_overlap_histgram_female.png", plot = g)
plot(g,add=TRUE)

####all###############
#class
for( i in Class_list){
  
  subset<-all_table[all_table$TE_Class==i & all_table$Strand=="+",]
  if(nrow(femaletable[femaletable$TE_Class==i,])>0){
    print(i)
    g <- ggplot(subset, aes(x=Sexuality_Specificity,y=Gene_log2FoldChange,colour=Sexuality_Specificity))
    g <- g +geom_boxplot()+scale_color_manual(values=c("green", "red", "blue"))
    #title_name<-paste("upstream female ",i)
    g=g+ggtitle(i)
    name<- paste(i, "_upstream_overlap_Class_boxplot.png", sep="")
    plot(g)
    ggsave(file = name, plot = g)
  
   #x<-subset[,"Gene_log2FoldChange"]
   ##y<-subset[,"TE_log2FoldChange"]
   #correlation=cor(x, y, method="spearman")
   #print(correlation)
  }
}

#family
for( i in family_list){
  
  subset<-all_table[all_table$TE_family==i & all_table$Strand=="+",]
  if(nrow(femaletable[femaletable$TE_family==i,])>0){
    print(i)
    g <- ggplot(subset, aes(x=Sexuality_Specificity,y=Gene_log2FoldChange,colour=Sexuality_Specificity))
    g <- g +geom_boxplot()
    #title_name<-paste("upstream female ",i)
    g=g+ggtitle(i)+scale_color_manual(values=c("green", "red", "blue"))
    name<- paste(i, "_upstream_overlap_family_boxplot.png", sep="")
    plot(g)
    ggsave(file = name, plot = g)
    
    x<-subset[,"Gene_log2FoldChange"]
    y<-subset[,"TE_log2FoldChange"]
    correlation=cor(x, y, method="pearson")
    print(correlation)
  }
}

########downstream############
#downstream overlap
table = read.table("/home/smiyake/sho/Fullset/txt/merge_transcript_TE_downstream_overlap_lfc.txt", sep="\t", header=T,encoding="utf-8")
maletable<-table[(table$TE_log2FoldChange>1 & table$TE_pvalue<0.05 ),]
femaletable<-table[(table$TE_log2FoldChange<-1 & table$TE_pvalue<0.05 ),]
sig_table<-table[(table$TE_pvalue<0.05 ),]

g <- ggplot(table, aes(x=Gene_log2FoldChange,y=TE_log2FoldChange,colour=TE_Class))
g <- g + geom_point()　#geom_pointは「散布図で書いてね」と指定するため
g=g+xlim(-8,8)+ylim(-8,8)
#ggsave(file = "upsteram_overlap_histgram_male.png", plot = g)
plot(g,add=TRUE)
x<-table[,"Gene_log2FoldChange"]
y<-table[,"TE_log2FoldChange"]
correlation=cor(x, y, method="spearman")
print(correlation)
