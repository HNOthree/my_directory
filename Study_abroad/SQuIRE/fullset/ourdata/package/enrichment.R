library(ggplot2)
library(scales)
directory = commandArgs(trailingOnly=TRUE)[1]
#directory="/home/smiyake/sho/Fullset/SQuIRE/txt"
file_name<-paste(directory,"/family_percentage_enrich_count.txt",sep='')



myfunc<-function(file_name){
 #fam<-"Olat_rnd-6_family-6001"
 all_table=read.table(file_name,sep="\t", header=T,encoding="utf-8")
 all_table<-subset(all_table,complete.cases(all_table))
 for (sexuality in c("Male","Female","Other")){
  print(sexuality)
  name<-c("Family","Superfamily","Class","Count",sexuality)
  all<- all_table[,name]
  colnames(all)<-c("Family","Superfamily","Class","nCopTot","nCopInReg")



# PlanTEnrichment :

 all$ratC <- all$nCopInReg/all$nCopTot
 all$EsC <- all$ratC/mean(all$ratC)

 pvals <- c()
 Es <- c()
 for (i in 1:dim(all)[1]){
  a=all[i,"nCopInReg"]
  b=all[i,"nCopTot"]
  c=sum(all$nCopInReg)
  d=sum(all$nCopTot)
  rdy = matrix(c(a,c,b,d),nrow=2)
  pvals <- c(pvals,fisher.test(rdy)$p.value)
  Es <- c(Es,(a/b)/(c/d))
  }             
 all$Pvals <- pvals
 all$Es <- Es            

 all$Pchoice <- all$Pvals<0.05/dim(all)[1]
 all <- all[order(all$Pvals,decreasing = F),]
 head(all)

 txt_name<-paste(directory,"/ALLTE_enrichment_",sep='')
 txt_name<-paste(txt_name,sexuality,sep='')
 txt_name<-paste(txt_name,".txt",sep='')
 write.table(all,txt_name,sep="\t")

 #sub<-all[all$Family==fam,]
 p<-ggplot(all,aes(x=log2(EsC),y=-log10(Pvals),color=Pchoice))+scale_color_manual(values=c("#101507","#bf7340"))
 p<-p+geom_point(alpha=0.4,na.rm = TRUE) +theme_bw()+xlim(-5,5)+ylim(0,35)+ggtitle(sexuality)
 #p<-p+layer(data=sub, mapping=aes(x=log2(EsC),y=-log10(Pvals),color=fam),geom="point",stat="identity",position="identity")
 plot(p)
 png_name<-paste(directory,"/ALLTEenrichment_",sep='')
 png_name<-paste(png_name,sexuality,sep="")
 png_name<-paste(png_name,".png",sep='')
 #ggsave(file = png_name, plot = p,dpi=300)
 
}
}
myfunc(file_name)

