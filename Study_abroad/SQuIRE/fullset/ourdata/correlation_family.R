library(ggplot2)

directory<-"/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis"
save_dir<-"/home/smiyake/sho/Fullset/SQuIRE/image"
file_name<-paste(directory,"/Gene_TE_distance_bias.txt",sep='')
Table = read.table(file_name, sep="\t", header=T,encoding="utf-8")
family="Olat_helitron1"
family_table<-Table[Table$Family==family,]

for(dist in c(1000,5000,10000,50000,100000,500000)){
  sub<-family_table[family_table$Distance<dist,]
  x<-sub[,"TE_log2FoldChange"]
  y<-sub[,"Gene_log2FoldChange"]

  correlation=cor.test(x, y, method="pearson")
  print(dist)
  print(correlation$estimate)
  print(correlation$p.value)
  
  name<-paste(family,"~")
  name<-paste(name,dist,sep='')
  
  g<-ggplot(sub,aes(x=TE_log2FoldChange,y=Gene_log2FoldChange))
  g<-g+geom_point()+theme_bw()+xlim(-10,10)+ylim(-10,10)+ggtitle(name)+geom_abline(slope=1,colour="red")
  g<-g+ annotate("text", x=-5, y=-4, parse=TRUE,label=correlation$estimate)+annotate("text", x=-7, y=-3, parse=TRUE,label="Correlation_coefficiency")
  g<-g+ annotate("text", x=-5, y=-6, parse=TRUE,label=correlation$p.value)+annotate("text", x=-6, y=-5, parse=TRUE,label="pvalue")
  plot(g)
  save_name<-paste(save_dir,family,sep='/')
  save_name<-paste(save_name,dist,sep="_")
  save_name<-paste(save_name,".png",sep='')
  print(save_name)
  ggsave(file=save_name,plot=g,dpi=300)
}
