library(ggplot2)
library(ggrepel)
###SuperFamily
Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/csv/upstream_LessThan_correlation_efficiency_list.csv", sep=",", header=T,encoding="utf-8")
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
ggsave(file = "upstream_lessthan_correlation.png", plot = g)


Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/csv/upstream_between_correlation_efficiency_list.csv", sep=",", header=T,encoding="utf-8")
table<-subset(Table,complete.cases(Table))

length_seq<-c(1000,5000,10000,25000,50000,100000,500000)
for (i in c(1,2,3,4,5,6)){
  print(length_seq[i])
}
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
ggsave(file = "upstream_between_correlation.png", plot = g)


###########Family
Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/upstream_family_CC_LessThan.txt", sep="\t", header=T,encoding="utf-8")
table<-subset(Table,complete.cases(Table))
table$Distance<-factor(table$Distance,levels=c("0 ~ 1000","0 ~ 5000","0 ~ 10000","0 ~ 25000","0 ~ 50000","0 ~ 100000","0 ~ 500000"))

g <- ggplot(table, aes(x = Distance, y = Correlation_coefficient))
g <- g + geom_boxplot()+theme_bw()+ylim(-1.0,1.0)
g <- g+theme(axis.text.x=element_text(size=rel(0.7), angle=90))
plot(g)
ggsave(file = "upstream_lessthan_correlation_family.png", plot = g)


Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/upstream_family_CC_between.txt", sep="\t", header=T,encoding="utf-8")
table<-subset(Table,complete.cases(Table))

table$Distance<-factor(table$Distance,levels=c("1 ~ 1000","1001 ~ 5000","5001 ~ 10000","10001 ~ 25000","25001 ~ 50000","50001 ~ 100000","100001 ~ 500000"))
g <- ggplot(table, aes(x = Distance, y = Correlation_coefficient))
g <- g + geom_boxplot()+theme_bw()+ylim(-1.0,1.0)
g <- g+theme(axis.text.x=element_text(size=rel(0.7), angle=90))
plot(g)
ggsave(file = "upstream_between_correlation_family.png", plot = g)
######################################################################


###SuperFamily
Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/csv/downstream_LessThan_correlation_efficiency_list.csv", sep=",", header=T,encoding="utf-8")
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
ggsave(file = "downstream_lessthan_correlation.png", plot = g)


Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/csv/downstream_between_correlation_efficiency_list.csv", sep=",", header=T,encoding="utf-8")
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
ggsave(file = "downstream_between_correlation.png", plot = g)

###########Family
Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/downstream_family_CC_LessThan.txt", sep="\t", header=T,encoding="utf-8")
table<-subset(Table,complete.cases(Table))
table$Distance<-factor(table$Distance,levels=c("0 ~ 1000","0 ~ 5000","0 ~ 10000","0 ~ 25000","0 ~ 50000","0 ~ 100000","0 ~ 500000"))

g <- ggplot(table, aes(x = Distance, y = Correlation_coefficient))
g <- g + geom_boxplot()+theme_bw()+ylim(-1.0,1.0)
g <- g+theme(axis.text.x=element_text(size=rel(0.7), angle=90))
plot(g)
ggsave(file = "downstream_lessthan_correlation_family.png", plot = g)


Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/downstream_family_CC_between.txt", sep="\t", header=T,encoding="utf-8")
table<-subset(Table,complete.cases(Table))
table$Distance<-factor(table$Distance,levels=c("1 ~ 1000","1001 ~ 5000","5001 ~ 10000","10001 ~ 25000","25001 ~ 50000","50001 ~ 100000","100001 ~ 500000"))

g <- ggplot(table, aes(x = Distance, y = Correlation_coefficient))
g <- g + geom_boxplot()+theme_bw()+ylim(-1.0,1.0)
g <- g+theme(axis.text.x=element_text(size=rel(0.7), angle=90))
plot(g)
ggsave(file = "downstream_between_correlation_family.png", plot = g)

