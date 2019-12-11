library(ggplot2)
library(ggtern)
library(scales)
directory<-'/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis'
file_name<-paste(directory,"/DESeq2_TE_separated.txt",sep='')
for_volcano<-read.table(file_name,head=TRUE)
file_name<-paste(directory,"/family_percentage_enrich_percentage.txt",sep="")
Table = read.table(file_name,  sep="\t", header=T,encoding="utf-8")
percentage<-subset(Table,complete.cases(Table))
file_name<-paste(directory,"/ALLTE_enrichment_Male.txt",sep="")
enrich= read.table(file_name,  sep="\t", header=T,encoding="utf-8")
family_list=c("Olat_rnd-6_family-4702","Olat_rnd-1_family-855","Olat_rnd-1_family-197","Olat_helitron1","Olat_BEL_12","Olat_gypsy_186","Olat_rnd-6_family-2244","Olat_rnd-1_family-315","Olat_BEL_8")

for (family in family_list){
  print(family)
  name<-paste("TE Volcano plot",family)
  sub_con<-for_volcano[for_volcano$Padj>0.05,]
  sub_con<-transform(sub_con,status="non_sig")
  sub_male<-for_volcano[for_volcano$Padj<0.05 & for_volcano$Log2FoldChange>1,]
  sub_male<-transform(sub_male,status="male")
  sub_female<-for_volcano[for_volcano$Padj<0.05 & for_volcano$Log2FoldChange< -1,]
  sub_female<-transform(sub_female,status="female")
  plot_family<-for_volcano[for_volcano$Family==family,]
  plot_family<-transform(plot_family,status=family)
  all<-rbind(sub_con,sub_male)
  all<-rbind(all,sub_female)
  all<-rbind(all,sub_female)
  all<-rbind(all,plot_family)
  
  p <-ggplot(all, aes(x=Log2FoldChange,y=-log10(Pvalue),colour=status))
  p<-p+geom_point(na.rm = TRUE)+theme_bw()+scale_color_manual(values=c("black","blue","red","green"))+ theme(legend.position = 'none')
  save_name<-paste(family,"_volcano.png",sep='')
  ggsave(file = save_name, plot = p,width=9,dpi=300)
  
  name<-c("Male","Female","Other")
  fam<-percentage[percentage$Family==family,]
  famcol<-data.frame(Male=fam$Male)
  famcol<-transform(famcol,Female=fam$Female)
  famcol<-transform(famcol,Other=fam$Other)
  famcol<-transform(famcol,Status=family)
  p_percentage<-percentage[,name]
  p_percentage=transform(p_percentage,Status="family")
  
  #malemean<-mean(p_percentage$Male)
  #femalemean<-mean(p_percentage$Female)
  #Othermean<-mean(p_percentage$Other)
  #meanplot<-data.frame(Male=malemean)
  #meanplot<-transform(meanplot,Female=femalemean)
  #meanplot<-transform(meanplot,Other=Othermean)
  #meanplot<-transform(meanplot,Status="Average")
  #p_percentage<-rbind(p_percentage,meanplot)
  
  p_percentage<-rbind(p_percentage,famcol)
  
  p2 <- ggtern(data = p_percentage, aes(Male, Other, Female,colour=Status))
  p2 <- p2 + geom_point(size=2,na.rm = TRUE)+theme_bw()+ggtitle(family)#+ theme(legend.position = 'none')
  p2<-p2+scale_color_manual(values=c("black","green","blue"))+theme(text = element_text(size=15))+theme_showarrows()
  save_name<-paste(family,"_trigram.png",sep='')
  ggsave(file = save_name, plot = p2,width=9,dpi=300)
  
  
  
  sub<-enrich[enrich$Family==family,]
  sub[1,10]<-family
  f_enrich<-rbind(enrich,sub)
  p3<-ggplot(f_enrich,aes(x=log2(EsC),y=-log10(Pvals),colour=Pchoice))+scale_color_manual(values=c("#101507","green","#bf7340"))
  p3<-p3+geom_point(alpha=0.6) +theme_bw()+xlim(-5,5)+ylim(0,35)+ggtitle(sexuality)
  save_name<-paste(family,"_enrich.png",sep='')
  ggsave(file = save_name, plot = p3,width=9,dpi=300)
}
