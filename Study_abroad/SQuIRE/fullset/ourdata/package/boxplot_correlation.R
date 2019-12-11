library(ggplot2)
#directory<-commandArgs(trailingOnly=TRUE)[1] #directory where you did "myprocedure.sh"
directory<-"/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis"
myfunc<-function(load_directory,save_directory){
  name<-paste(directory,"/correlation_coefficiency_between_ornon.txt",sep='')
  
  Table = read.table(name, sep="\t", header=T,encoding="utf-8")
  table<-subset(Table,complete.cases(Table))
  #table<-table[table$Region!="ALL",]
  
  length_seq<-c(1000,5000,10000,25000,50000,100000,500000)
 
  all_set<-table[table$Distance==1000 ,]
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
  g <- ggplot(all_set, aes(x = distance, y = Correlation_coefficiency,colour=Region))
  g <- g + geom_boxplot(na.rm = TRUE)+theme_bw()+ylim(-1.0,1.0)
  g <- g+theme(axis.text.x=element_text(size=rel(0.7), angle=90))
  figname<-paste(directory,"/correlation_boxplot_between_region.png",sep='')
  plot(g)
  #ggsave(file = figname, plot = g)
  
  suball<-all_set[all_set$Region=="ALL",]
  g <- ggplot(suball, aes(x = distance, y = Correlation_coefficiency))
  g <- g + geom_boxplot(na.rm = TRUE)+theme_bw()+ylim(-1.0,1.0)
  g <- g+theme(axis.text.x=element_text(size=rel(0.7), angle=90))
  figname<-paste(directory,"/correlation_boxplot_between.png",sep='')
  plot(g)
  #ggsave(file = figname, plot = g,width = 9,dpi=300)
  
  
  name<-paste(directory,"/correlation_coefficiency_lessthan_ornon.txt",sep='')
  Table = read.table(name, sep="\t", header=T,encoding="utf-8")
  table<-subset(Table,complete.cases(Table))
  #table<-table[table$Region!="ALL",]
  
  
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
  
  g <- ggplot(all_set, aes(x = distance, y = Correlation_coefficiency,colour=Region))
  g <- g + geom_boxplot(na.rm = TRUE)+theme_bw()+ylim(-1.0,1.0)+theme(axis.text.x=element_text(size=rel(0.7), angle=90))
  figname<-paste(directory,"/correlation_boxplot_lessthan_region.png",sep='')
  plot(g)
  #ggsave(file = figname, plot = g,width = 9,dpi=300)
  
  suball<-all_set[all_set$Region=="ALL",]
  g <- ggplot(suball, aes(x = distance, y = Correlation_coefficiency))
  g <- g + geom_boxplot(na.rm = TRUE)+theme_bw()+ylim(-1.0,1.0)
  g <- g+theme(axis.text.x=element_text(size=rel(0.7), angle=90))
  figname<-paste(directory,"/correlation_boxplot_lessthan.png",sep='')
  plot(g)
  #ggsave(file = figname, plot = g,width = 9,dpi=300)
  
}


myfunc(directory)

