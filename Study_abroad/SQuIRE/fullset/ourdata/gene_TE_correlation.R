library(ggplot2)
library(ggrepel)
Class_list<-c('RC', 'LINE', 'LTR', 'SINE', 'DNA')
family_list<-c('Helitron', 'L1', 'ERV1', 'CR1-Zenon', 'tRNA-Core-L2', 'hAT-Charlie', 'Gypsy', 'L2', 'PIF-Harbinger', 'RTE-BovB', 'tRNA', 'TcMar', 'TcMar-Tc1', 'Ngaro', 'hAT-Ac', 'Polinton', 'Rex-Babar', 'Harbinger', 'PIF-Harbinger?', 'EnSpm-CACTA', 'ERV', 'hAT', 'MITE?', 'BEL-Pao', 'Copia', 'Dong-R4', 'PIF-ISL2EU', 'Helitron?', 'Penelope', 'TcMar-Tc2', 'hAT-Tip100', 'I', 'MIR', 'PiggyBac', 'TcMar-Tigger', 'Gypsy-Cigr', 'Zisupton', 'L1-Tx1', 'Crypton', 'MITE', 'P', 'Proto2', 'TcMar-ISRm11', 'Mariner', 'Gypsy?', 'Pao', 'hAT-Charlie?', 'TcMar-Tc1?', 'Copia?', 'ERVK', 'hAT-Ac?', 'tRNA-L2?', 'Academ', 'RTE-X', 'MuDr', 'hAT-Tol2', 'hAT-hAT5', 'DIRS', 'R2-Hero')


Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/Gene_TE_distance_lfc.txt", sep="\t", header=T,encoding="utf-8")
table<-subset(Table,complete.cases(Table))


threshold<-c(1000,5000,10000,25000,50000,100000,500000)
all_data=c("Superfamily","Distance","Data_length","Correlation")
corre_data=c("Superfamily","Distance","Data_length","Correlation")
minimum<-0



for (i in threshold){
  subset<-table[table$Distance<i & table$Distance>minimum ,]
  for (j in family_list){#family
    family<-subset[subset$Superfamily==j ,]
    if(nrow(family)>0){
      name=c("Family","Gene_log2FoldChange","TE_log2FoldChange")
      family_select<-family[,name]
      dup_del_subset=family_select[!duplicated(paste(family_select$Gene_log2FoldChange, family_select$TE_log2FoldChange, sep = ",")), ]
      #################The number of columns is more than 5#########
      if(nrow(dup_del_subset)>=5){
        x<-dup_del_subset[,"Gene_log2FoldChange"]
        y<-dup_del_subset[,"TE_log2FoldChange"]
        correlation=cor(x, y, method="pearson")
        all_data<-rbind(all_data,c(j,minimum,nrow(dup_del_subset),correlation))
        if(abs(correlation)>0.5){
          corre_data<-rbind(corre_data,c(j,minimum,nrow(dup_del_subset),correlation))
        }
      }
    }
    
  }
  minimum<-i
}
write.csv(all_data,"/home/smiyake/sho/Fullset/SQuIRE/csv/nearby_between_correlation_efficiency_list.csv",row.names = FALSE)
write.csv(corre_data,"/home/smiyake/sho/Fullset/SQuIRE/csv/nearby_between_correlation_efficiency_list_sig.csv",row.names = FALSE)


#less than distance
length_seq<-c(1000,5000,10000,25000,50000,100000,500000)

all_data=c("Superfamily","Distance","Data_length","Correlation")
corre_data=c("Superfamily","Distance","Data_length","Correlation")
for (i in length_seq){
  print(i)
  subset<-table[table$Distance<i ,]
  for (j in family_list){#family
    family<-subset[subset$Superfamily==j ,]
    if(nrow(family)>0){
      name=c("Family","Gene_log2FoldChange","TE_log2FoldChange")
      family_select<-family[,name]
      dup_del_subset=family_select[!duplicated(paste(family_select$Gene_log2FoldChange, family_select$TE_log2FoldChange, sep = ",")), ]
      #dup_del_subset<-family_select[!(duplicated(family_select[c("Gene_log2FoldChange","TE_log2FoldChange")]) | duplicated(family_select[c("Gene_log2FoldChange","TE_log2FoldChange")], fromLast = TRUE)), ]
      if(nrow(dup_del_subset)>5){
        x<-dup_del_subset[,"Gene_log2FoldChange"]
        y<-dup_del_subset[,"TE_log2FoldChange"]
        correlation=cor(x, y, method="pearson")
        all_data<-rbind(all_data,c(j,i,nrow(dup_del_subset),correlation))
        if(abs(correlation)>0.5){
          corre_data<-rbind(corre_data,c(j,i,nrow(dup_del_subset),correlation))
        }
      }
    }
    
  }
}
write.csv(all_data,"/home/smiyake/sho/Fullset/SQuIRE/csv/nearby_LessThan_correlation_efficiency_list.csv",row.names = FALSE)
write.csv(corre_data,"/home/smiyake/sho/Fullset/SQuIRE/csv/nearby_LessThan_correlation_efficiency_list_sig.csv",row.names = FALSE)

###SuperFamily
Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/csv/nearby_LessThan_correlation_efficiency_list.csv", sep=",", header=T,encoding="utf-8")
table<-subset(Table,complete.cases(Table))
length_seq<-c(5000,10000,25000,50000,100000,500000)
all_set<-table[table$Distance==1000 ,]
Label=paste("0~",as.character(1000))
all_set<-transform(all_set, distance=Label )
for(i in length_seq){#length
  subset=table[table$Distance==i ,]
  Label=paste("0~",as.character(i))
  subset<-transform(subset, distance=Label )
  all_set=rbind(all_set,subset)
}

g <- ggplot(all_set, aes(x = distance, y = Correlation))
g <- g + geom_boxplot()+theme_bw()+ylim(-1.0,1.0)
plot(g)
ggsave(file = "nearby_lessthan_correlation.png", plot = g)


Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/csv/nearby_between_correlation_efficiency_list.csv", sep=",", header=T,encoding="utf-8")
table<-subset(Table,complete.cases(Table))

length_seq<-c(1000,5000,10000,25000,50000,100000,500000)

all_set<-table[table$Distance==0 ,]
Label=paste(as.character(1),"~")
Label=paste(Label,"1000")
all_set<-transform(all_set, distance=Label )
for(i in c(1,2,3,4,5,6)){#length
  length=length_seq[i]
  subset=table[table$Distance==length ,]
  Label=paste(as.character(length+1),"~")
  Label=paste(Label,as.character(length_seq[i+1]))
  subset<-transform(subset, distance=Label )
  all_set=rbind(all_set,subset)
}
g <- ggplot(all_set, aes(x = distance, y = Correlation))
g <- g + geom_boxplot()+theme_bw()+ylim(-1.0,1.0)
g <- g+theme(axis.text.x=element_text(size=rel(0.7), angle=90))
plot(g)
ggsave(file = "nearby_between_correlation.png", plot = g)

