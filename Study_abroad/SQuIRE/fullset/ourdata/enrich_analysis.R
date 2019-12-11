library(ggplot2)
library(ggrepel)
library(scales)
Table=read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/probability.txt", sep="\t", header=T,encoding="utf-8")
prob<-subset(Table,complete.cases(Table))

p<-ggplot(prob, aes(x=Same_frequency,y=Different_frequency,colour=Sexuality))
p <- p +geom_point()+xlim(0,15)+ylim(0,15)
p<-p+theme_bw()
plot(p)
ggsave(file="frequency.png",plot=p,
       width = 9, height = 6, dpi = 300)

###########highcontent
Table=read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/DESeq2_TE_separated.txt", sep="\t", header=T,encoding="utf-8")
control<-subset(Table,complete.cases(Table))
control<-transform(control,Status="ALL")
Table=read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/male_region_TE.txt", sep="\t", header=T,encoding="utf-8")
male<-subset(Table,complete.cases(Table))
male<-transform(male,Status="Male region")

ALL<-rbind(control,male)
p<-ggplot(ALL, aes(x=Status,fill=Class))
p<-p+geom_bar(position = "fill")
p<-p+theme_bw()+ scale_y_continuous(labels = percent)
plot(p)
ggsave(file="count.png",plot=p,
       width = 9, height = 6, dpi = 300)

##########correlation_coefficiency

Table = read.table("/home/smiyake/shares/Sho/Results/SQuIRE/txt/Gene_TE_distance_bias.txt", sep="\t", header=T,encoding="utf-8")
table<-subset(Table,complete.cases(Table))
family_list=read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/superfamily_list.txt", sep="\t", header=T,encoding="utf-8")
###Calculate
threshold<-c(1000,5000,10000,25000,50000,100000,500000)
all_data=c("Superfamily","Distance","Data_length","Correlation","Status")
enrich_data=c("Superfamily","Distance","Data_length","Correlation","Status")
minimum<-0
for (i in threshold){
  print(i)
  subset<-table[table$Distance<i & table$Distance>minimum ,]
  for (j in family_list$Superfamily){#family

    family<-subset[subset$Superfamily==j ,]
    if(nrow(family)>0){
      biased<-family[family$Region=="biased_region",]
      control<-family[family$Region=="non_biased_region",]
      #################The number of columns is more than 5#########
      if(nrow(biased)>=3){
        x<-biased[,"Gene_log2FoldChange"]
        y<-biased[,"TE_log2FoldChange"]
        correlation=cor(x, y, method="pearson")
        enrich_data<-rbind(enrich_data,c(j,minimum,nrow(biased),correlation,"Biased_region"))
      }
      if(nrow(control)>=3){
        x<-control[,"Gene_log2FoldChange"]
        y<-control[,"TE_log2FoldChange"]
        correlation=cor(x, y, method="pearson")
        all_data<-rbind(all_data,c(j,minimum,nrow(control),correlation,"Non_biased_region"))
      }
    }
    
  }
  minimum<-i
}
csv_data<-rbind(all_data,enrich_data)
write.csv(csv_data,"/home/smiyake/sho/Fullset/SQuIRE/csv/Nearby_between_correlation_efficiency_list_enrich.csv",row.names = FALSE)

##################################################################
#less than distance
length_seq<-c(1000,5000,10000,25000,50000,100000,500000)

all_data=c("Superfamily","Distance","Data_length","Correlation","Status")
enrich_data=c("Superfamily","Distance","Data_length","Correlation","Status")
for (i in length_seq){
  print(i)
  subset<-table[table$Distance<i ,]
  for (j in family_list$Superfamily){#family
    family<-subset[subset$Superfamily==j ,]
    if(nrow(family)>0){
      biased<-family[family$Region=="biased_region",]
      control<-family[family$Region=="non_biased_region",]
      if(nrow(biased)>=3){
        x<-biased[,"Gene_log2FoldChange"]
        y<-biased[,"TE_log2FoldChange"]
        correlation=cor(x, y, method="pearson")
        enrich_data<-rbind(enrich_data,c(j,i,nrow(biased),correlation,"Biased_region"))
      }
      if(nrow(control)>=3){
        x<-control[,"Gene_log2FoldChange"]
        y<-control[,"TE_log2FoldChange"]
        correlation=cor(x, y, method="pearson")
        all_data<-rbind(all_data,c(j,i,nrow(control),correlation,"Non_biased_region"))
      }
    }
    
  }
}
csv_data<-rbind(all_data,enrich_data)
write.csv(csv_data,"/home/smiyake/sho/Fullset/SQuIRE/csv/Nearby_LessThan_correlation_efficiency_list_enrich.csv",row.names = FALSE)

###################################################################################

Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/csv/Nearby_between_correlation_efficiency_list_enrich.csv", sep=",", header=T,encoding="utf-8")
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
g <- ggplot(all_set, aes(x = distance, y = Correlation,colour=Status))
g <- g + geom_boxplot()+theme_bw()+ylim(-1.0,1.0)
g <- g+theme(axis.text.x=element_text(size=rel(0.7), angle=90))
plot(g)
ggsave(file = "nearby_between_correlation_enrich.png", width = 8, height = 6,plot = g)


Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/csv/Nearby_LessThan_correlation_efficiency_list_enrich.csv", sep=",", header=T,encoding="utf-8")
table<-subset(Table,complete.cases(Table))
length_seq<-c(1000,5000,10000,25000,50000,100000,500000)
all_set<-table[table$Distance==1000 ,]
Label=paste("0~",as.character(1000))
all_set<-transform(all_set, distance=Label )
for(i in length_seq){#length
  subset=table[table$Distance==i ,]
  Label=paste("0~",as.character(i))
  subset<-transform(subset, distance=Label )
  all_set=rbind(all_set,subset)
}

g <- ggplot(all_set, aes(x = distance, y = Correlation,colour=Status))
g <- g + geom_boxplot()+theme_bw()+ylim(-1.0,1.0)
plot(g)
ggsave(file = "nearby_lessthan_correlation_enrich.png", width =8, height = 6,plot = g)

#######percentage
library(ggtern)
Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/family_percentage_enrich_25k_all.txt",  sep="\t", header=T,encoding="utf-8")
percentage<-subset(Table,complete.cases(Table))
name<-c("Male","Female","Other")
percentage<-percentage[,name]
percentage=transform(percentage,Status=1)

malemean<-mean(percentage$Male)
femalemean<-mean(percentage$Female)
othermean<-mean(percentage$Other)
meanplot<-c(malemean,femalemean,othermean,0)
percentage<-rbind(percentage,meanplot)
p <- ggtern(data = percentage, aes(Male, Other, Female,colour=Status))

#p <- p+stat_density_tern(geom = "polygon",aes(fill=..level..),base = "ilr")
p <- p + geom_point(size=2)+theme_bw()
p<-p+theme_showarrows()+ theme(legend.position = 'none')
ggsave(file = "/home/smiyake/sho/Fullset/SQuIRE/image/nearby_tendency/TE_enrich/25k/TE_bias/trigram_ALL.png", plot = p)
plot(p)


bias<-percentage[(percentage$Male>0.5 | percentage$Female>0.5) & percentage$Count>=5,]

Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/DESeq2_TE_separated.txt",  sep="\t", header=T,encoding="utf-8")
TE<-subset(Table,complete.cases(Table))

Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/Gene_TE_number_purified.txt", sep="\t", header=T,encoding="utf-8")
Distance<-subset(Table,complete.cases(Table))
#Distance<-Distance[Distance$Number<10,]
Distance$Direction_number<-as.factor(Distance$Direction_number)
Distance$Number<-as.factor(Distance$Number)
for(i in bias$Family){
  family_subset<-TE[TE$Family==i,]
  g <- ggplot(family_subset, aes(x = Log2FoldChange ))
  g <- g + geom_histogram(bins=25)
  g <- g +ggtitle(i)+xlim(-10,10)
  g <- g+theme_bw()#+theme(legend.key.size =unit(0.5,"line"))
  g <- g#+theme(axis.text =element_text(size=rel(0.7), angle=90))
  name<-paste("/home/smiyake/sho/Fullset/SQuIRE/image/nearby_tendency/TE_enrich/25k/TE_bias/",i,sep='')
  name<-paste(name,"_histgram.png")
  ggsave(file = name, plot = g)
  plot(g)
  if(i=="Olat_rnd-5_family-2353" | i=="Olat_rnd-1_family-197"){
    print(i)
   family_subset<-Distance[Distance$Family==i,]
   g <- ggplot(family_subset, aes(x=Distance,y=Gene_log2FoldChange))
   g <- g +geom_point()+theme_bw()
  name<-paste("/home/smiyake/sho/Fullset/SQuIRE/image/nearby_tendency/TE_enrich/100k/TE_bias/",i,sep='')
  name<-paste(name,"_scatter.png")
  ggsave(file = name, plot = g)
  plot(g)
  }
}
