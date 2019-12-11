Table = read.table("/home/smiyake/sho/Fullset/txt/merge_transcript_TE_upstream_50000_lfc.txt", sep="\t", header=T,encoding="utf-8")
up_table<-subset(Table,complete.cases(Table))
up_male_specific_table<-up_table[up_table$TE_log2FoldChange> 1 & up_table$TE_pvalue<0.05 & up_table$Distance<1000 ,]
up_female_specific_table<-up_table[up_table$TE_log2FoldChange< -1 & up_table$TE_pvalue<0.05 & up_table$Distance<1000,]
down_table = read.table("/home/smiyake/sho/Fullset/txt/downstream_Gene_TE_merge_data.txt", sep="\t", header=T,encoding="utf-8")
down_male_specific_table<-down_table[down_table$TE_log2FoldChange> 1 & down_table$TE_pvalue<0.05 ,]
down_female_specific_table<-down_table[down_table$TE_log2FoldChange< -1 & down_table$TE_pvalue<0.05 ,]



#upstream
#all distance vs count
g <- ggplot(up_table, aes(x=Distance,fill=TE_Class))
#g <- g +  geom_histogram(position = "fill",bins=40)
g <- g +  geom_histogram(position = "stack",bins=20)
g<-g+xlim(0,50000)+ggtitle("The distribution of TE located upstram of gene")
plot(g)


Class_list<-c("DNA","DNA?","LINE","LTR","nonLTR","RC","Retro","SINE","Unknown","Unspecified")
for( i in Class_list){
  subset<-up_male_specific_table[up_male_specific_table$TE_Class==i,]
  if(nrow(subset)>0){
   g <- ggplot(subset, aes(x=Distance,y=Gene_log2FoldChange,colour=TE_family))
   name<- paste("Distance vs Gene LFC in ",i, sep="")
   name<- paste(name," (upstream)", sep="")
   g <- g + geom_point()+ggtitle(name)　#geom_pointは「散布図で書いてね」と指定するため
   name<- paste(name,"_male.png", sep="")
   g=g+xlim(0,1000)+ylim(-8,8)
   ggsave(file = name, plot = g)
   plot(g,add=TRUE)
   
  }
}

for( i in Class_list){
  subset<-up_female_specific_table[(up_female_specific_table$TE_Class==i & up_female_specific_table$Distance<100000),]
  if(nrow(subset)>0){
    g <- ggplot(subset, aes(x=Distance,y=Gene_log2FoldChange,colour=TE_family))
    name<- paste("Distance vs Gene LFC in ",i, sep="")
    name<- paste(name," (upstream)", sep="")
    g <- g + geom_point()+ggtitle(name)　#geom_pointは「散布図で書いてね」と指定するため
    name<- paste(name,"_female.png", sep="")
    g=g+xlim(0,1000)+ylim(-8,8)
    ggsave(file = name, plot = g)
    plot(g,add=TRUE)
    
  }
}


#downstream
for( i in Class_list){
  subset<-down_male_specific_table[(down_male_specific_table$TE_class==i & down_male_specific_table$Distance<100000),]
  if(nrow(subset)>0){
    g <- ggplot(subset, aes(x=Distance,y=Gene_log2FoldChange,colour=TE_family))
    name<- paste("Distance vs Gene LFC in ",i, sep="")
    name<- paste(name," (downstream)", sep="")
    g <- g + geom_point()+ggtitle(name)　#geom_pointは「散布図で書いてね」と指定するため
    name<- paste(name,"_male.png", sep="")
    g=g+xlim(0,100000)+ylim(-8,8)
    ggsave(file = name, plot = g)
    plot(g,add=TRUE)
    
  }
}

for( i in Class_list){
  subset<-down_female_specific_table[(down_female_specific_table$TE_class==i & down_female_specific_table$Distance<100000),]
  if(nrow(subset)>0){
    g <- ggplot(subset, aes(x=Distance,y=Gene_log2FoldChange,colour=TE_family))
    name<- paste("Distance vs Gene LFC in ",i, sep="")
    name<- paste(name," (downstream)", sep="")
    g <- g + geom_point()+ggtitle(name)　#geom_pointは「散布図で書いてね」と指定するため
    name<- paste(name,"_female.png", sep="")
    g=g+xlim(0,100000)+ylim(-8,8)
    ggsave(file = name, plot = g)
    plot(g,add=TRUE)
    
  }
}

