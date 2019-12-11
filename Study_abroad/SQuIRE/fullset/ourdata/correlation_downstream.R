library(ggplot2)
library(ggrepel)
Class_list<-c('RC', 'LINE', 'LTR', 'SINE', 'DNA')
family_list<-c('Helitron', 'L1', 'ERV1', 'CR1-Zenon', 'tRNA-Core-L2', 'hAT-Charlie', 'Gypsy', 'L2', 'PIF-Harbinger', 'RTE-BovB', 'tRNA', 'TcMar', 'TcMar-Tc1', 'Ngaro', 'hAT-Ac', 'Polinton', 'Rex-Babar', 'Harbinger', 'PIF-Harbinger?', 'EnSpm-CACTA', 'ERV', 'hAT', 'MITE?', 'BEL-Pao', 'Copia', 'Dong-R4', 'PIF-ISL2EU', 'Helitron?', 'Penelope', 'TcMar-Tc2', 'hAT-Tip100', 'I', 'MIR', 'PiggyBac', 'TcMar-Tigger', 'Gypsy-Cigr', 'Zisupton', 'L1-Tx1', 'Crypton', 'MITE', 'P', 'Proto2', 'TcMar-ISRm11', 'Mariner', 'Gypsy?', 'Pao', 'hAT-Charlie?', 'TcMar-Tc1?', 'Copia?', 'ERVK', 'hAT-Ac?', 'tRNA-L2?', 'Academ', 'RTE-X', 'MuDr', 'hAT-Tol2', 'hAT-hAT5', 'DIRS', 'R2-Hero')

Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/SQ_downstream_TE_lfc.txt", sep="\t", header=T,encoding="utf-8")
table<-subset(Table,complete.cases(Table))

length_seq<-c(1000,5000,10000,25000,50000,100000,500000)
minimum<-0

for(i in length_seq){#length
  ######################all TE with in Distance##########
  subset<-table[table$Distance<i & table$Distance>minimum ,]
  g <- ggplot(subset, aes(x=Gene_log2FoldChange,y=TE_log2FoldChange,colour=TE_Class))
  g <- g +geom_point()+theme_bw()
  g=g+xlim(-15,15)+ylim(-15,15)
  title_name<-paste(minimum,i,sep="_")
  title_name<-paste(title_name,"ALL")
  g=g+ggtitle(title_name)
  name<-paste("/home/smiyake/sho/Fullset/SQuIRE/image/correlation/downstream",i,sep="")
  name<- paste(i, "_downstream_all_between.png", sep="")
  #ggsave(file = name, plot = g)
  plot(g)
  #################super family##############################
  for (j in family_list){#family
    family<-subset[subset$Superfamily==j ,]
    
    if(nrow(family)>1){
      #print(j)
      g <- ggplot(family, aes(x=Gene_log2FoldChange,y=TE_log2FoldChange))
      g <- g +geom_point()+theme_bw()
      g=g+xlim(-15,15)+ylim(-15,15)
      title_name<-paste(minimum,i)
      title_name<-paste(title_name,j)
      name<-paste("/home/smiyake/sho/Fullset/SQuIRE/image/correlation/downstream/GroupByDistance/between/",title_name,sep="")
      g=g+ggtitle(title_name)
      name<- paste(name, "_downstream.png", sep="")
      #ggsave(file = name, plot = g)
      
      #plot(g)
    }
  }
  minimum<-i
}


######calculate correlation efficiency############

##between each distance
threshold<-c(1000,5000,10000,25000,50000,100000,500000)
all_data=c("Superfamily","Distance","Data_length","Correlation")
corre_data=c("Superfamily","Distance","Data_length","Correlation")
minimum<-0
for (i in threshold){
  subset<-table[table$Distance<i & table$Distance>minimum ,]
  for (j in family_list){#family
    family<-subset[subset$Superfamily==j ,]
    if(nrow(family)>0){
      name=c("TE_name","Gene_log2FoldChange","TE_log2FoldChange")
      family_select<-family[,name]
      dup_del_subset=family_select[!duplicated(paste(family_select$Gene_log2FoldChange, family_select$TE_log2FoldChange, sep = ",")), ]
      #################The number of columns is more than 5#########
      if(nrow(dup_del_subset)>=5){
        x<-dup_del_subset[,"Gene_log2FoldChange"]
        y<-dup_del_subset[,"TE_log2FoldChange"]
        correlation=cor(x, y, method="pearson")
        g <- ggplot(dup_del_subset, aes(x=Gene_log2FoldChange,y=TE_log2FoldChange))
        g <- g +geom_point()+theme_bw() +annotate("text", x=10, y=15, parse=TRUE,label=correlation)+annotate("text", x=0.3, y=15, parse=TRUE,label="Correlation_coefficiency") 
        g=g+xlim(-15,15)+ylim(-15,15)
        title_name<-paste(minimum,i)
        title_name<-paste(title_name,j)
        name<-paste("/home/smiyake/sho/Fullset/SQuIRE/image/correlation/downstream/GroupByDistance/between/",title_name,sep="")
        g=g+ggtitle(title_name)
        name<- paste(name, "_downstream.png", sep="")
        #ggsave(file = name, plot = g)
        all_data<-rbind(all_data,c(j,minimum,nrow(dup_del_subset),correlation))
        if(abs(correlation)>0.5){
          print(minimum)
          print(j)
          print(correlation)
          print(nrow(dup_del_subset))
          g <- ggplot(dup_del_subset, aes(x=Gene_log2FoldChange,y=TE_log2FoldChange,colour=TE_name))
          g <- g +geom_point()+theme_bw()+annotate("text", x=10, y=14, parse=TRUE,label=correlation)+annotate("text", x=0.3, y=15, parse=TRUE,label="Correlation_coefficiency") 
          g=g+xlim(-15,15)+ylim(-15,15)
          title_name<-paste(minimum,i)
          title_name<-paste(title_name,j)
          name<-paste("/home/smiyake/sho/Fullset/SQuIRE/image/correlation/downstream/GroupByDistance/between/corre_",title_name,sep="")
          g=g+ggtitle(title_name)
          name<- paste(name, "_downstream.png", sep="")
          #ggsave(file = name, plot = g)
          plot(g)
          corre_data<-rbind(corre_data,c(j,minimum,nrow(dup_del_subset),correlation))
        }
      }
    }
    
  }
  minimum<-i
}
write.csv(all_data,"/home/smiyake/sho/Fullset/SQuIRE/csv/downstream_between_correlation_efficiency_list.csv",row.names = FALSE)
write.csv(corre_data,"/home/smiyake/sho/Fullset/SQuIRE/csv/downstream_between_correlation_efficiency_list_sig.csv",row.names = FALSE)

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
      name=c("TE_name","Gene_log2FoldChange","TE_log2FoldChange")
      family_select<-family[,name]
      dup_del_subset=family_select[!duplicated(paste(family_select$Gene_log2FoldChange, family_select$TE_log2FoldChange, sep = ",")), ]
      #dup_del_subset<-family_select[!(duplicated(family_select[c("Gene_log2FoldChange","TE_log2FoldChange")]) | duplicated(family_select[c("Gene_log2FoldChange","TE_log2FoldChange")], fromLast = TRUE)), ]
      if(nrow(dup_del_subset)>5){
        x<-dup_del_subset[,"Gene_log2FoldChange"]
        y<-dup_del_subset[,"TE_log2FoldChange"]
        correlation=cor(x, y, method="pearson")
        #print(correlation)
        g <- ggplot(dup_del_subset, aes(x=Gene_log2FoldChange,y=TE_log2FoldChange))
        g <- g +geom_point()+theme_bw()+annotate("text", x=10, y=15, parse=TRUE,label=correlation)+annotate("text", x=0.3, y=15, parse=TRUE,label="Correlation_coefficiency") 
        g=g+xlim(-15,15)+ylim(-15,15)
        title_name<-paste(i,j)
        name<-paste("/home/smiyake/sho/Fullset/SQuIRE/image/correlation/downstream/GroupByDistance/lessthan/LessThan",title_name,sep="")
        g=g+ggtitle(title_name)
        name<- paste(name, "_downstream.png", sep="")
        #ggsave(file = name, plot = g)
        all_data<-rbind(all_data,c(j,i,nrow(dup_del_subset),correlation))
        #plot(g)
        if(abs(correlation)>0.5){
          g <- ggplot(dup_del_subset, aes(x=Gene_log2FoldChange,y=TE_log2FoldChange,colour=TE_name))+theme_bw()
          g <- g +geom_point()+theme_bw()+annotate("text", x=10, y=14, parse=TRUE,label=correlation)+annotate("text", x=0.3, y=15, parse=TRUE,label="Correlation_coefficiency") 
          g=g+xlim(-15,15)+ylim(-15,15)
          title_name<-paste(i,j)
          name<-paste("/home/smiyake/sho/Fullset/SQuIRE/image/correlation/downstream/GroupByDistance/lessthan/corre_LessThan",title_name,sep="")
          g=g+ggtitle(title_name)
          name<- paste(name, "_downstream.png", sep="")
          #ggsave(file = name, plot = g)
          #plot(g)
          corre_data<-rbind(corre_data,c(j,i,nrow(dup_del_subset),correlation))
        }
      }
    }
    
  }
}
write.csv(all_data,"/home/smiyake/sho/Fullset/SQuIRE/csv/downstream_LessThan_correlation_efficiency_list.csv",row.names = FALSE)
write.csv(corre_data,"/home/smiyake/sho/Fullset/SQuIRE/csv/downstream_LessThan_correlation_efficiency_list_sig.csv",row.names = FALSE)

