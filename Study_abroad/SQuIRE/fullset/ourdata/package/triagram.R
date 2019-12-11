library(ggtern)
library(ggplot2)
library(ggrepel)
library(scales)

directory = commandArgs(trailingOnly=TRUE)[1]
directory<-"/home/smiyake/sho/Fullset/SQuIRE/txt"

myfunc<-function(directory){
  file_name<-paste(directory,"/family_percentage_enrich_percentage.txt",sep="")
  Table = read.table(file_name,  sep="\t", header=T,encoding="utf-8")
  percentage<-subset(Table,complete.cases(Table))
  name<-c("Male","Female","Other")
  
  #famname<-"Olat_rnd-4_family-200"
  #fam<-percentage[percentage$Family==famname,]
  #famcol<-data.frame(Male=fam$Male)
  #famcol<-transform(famcol,Female=fam$Female)
  #famcol<-transform(famcol,Other=fam$Other)
  #famcol<-transform(famcol,Status=famname)
  
  
  percentage<-percentage[,name]
  percentage=transform(percentage,Status="family")
  
  malemean<-mean(percentage$Male)
  femalemean<-mean(percentage$Female)
  Othermean<-mean(percentage$Other)
  meanplot<-data.frame(Male=malemean)
  meanplot<-transform(meanplot,Female=femalemean)
  meanplot<-transform(meanplot,Other=Othermean)
  meanplot<-transform(meanplot,Status="Average")
  percentage<-rbind(percentage,meanplot)
  
  #percentage<-rbind(percentage,famcol)
  p <- ggtern(data = percentage, aes(Male, Other, Female,colour=Status))
  
  p <- p + geom_point(size=2,na.rm = TRUE)+theme_bw()
  p<-p+theme_showarrows()+scale_color_manual(values=c("black","red","blue"))
  save_name<-paste(directory,"/trigram_ALL.png",sep='')
  plot(p)
  #ggsave(file = save_name, plot = p,width=9,dpi=300)
}

myfunc(directory)
