library(ggplot2)
library(scales)

directory="/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis"
file_name<-paste(directory,"/family_nearestgene_count.txt",sep='')

save_dir="/home/smiyake/sho/Fullset/SQuIRE"


myfunc<-function(file_name){
  all_table=read.table(file_name,sep="\t", header=T,encoding="utf-8")
  all_table<-subset(all_table,complete.cases(all_table))
  
  
  for (threshold in c("Morethan1","Morethan2","Morethan3","Morethan4","Morethan5")){
    print(threshold)
    name<-c("Family","Expressing_location",threshold)
    all<- all_table[,name]
    colnames(all)<-c("Family","nCopTot","nCopInReg")
    
    
    
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
    
    txt_name<-paste(save_dir,"/txt/TE_nearest",sep='')
    txt_name<-paste(txt_name,threshold,sep='')
    txt_name<-paste(txt_name,".txt",sep='')
    write.table(all,txt_name,sep="\t")
    
    #sub<-all[all$Family==fam,]
    p<-ggplot(all,aes(x=log2(EsC),y=-log10(Pvals),color=Pchoice))+scale_color_manual(values=c("#101507","#bf7340"))
    p<-p+geom_point(na.rm = TRUE) +theme_bw()+xlim(-5,5)+ylim(0,35)+ggtitle(threshold)#alpha=0.4,
    #p<-p+layer(data=sub, mapping=aes(x=log2(EsC),y=-log10(Pvals),color=fam),geom="point",stat="identity",position="identity")
    plot(p)
    png_name<-paste(save_dir,"/image/TE_nearest_gene",sep='')
    png_name<-paste(png_name,threshold,sep="")
    png_name<-paste(png_name,".png",sep='')
    ggsave(file = png_name, plot = p,dpi=300)
    
  }
}
myfunc(file_name)
