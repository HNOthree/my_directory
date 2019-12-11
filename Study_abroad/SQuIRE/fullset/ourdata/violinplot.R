library(ggplot2)
library(ggrepel)
library(gridExtra)
library(vioplot)
Class_list<-c("DNA","LINE","LTR","RC","SINE")
#direcroty="/home/smiyake/sho/Fullset/SQuIRE/image/correlation/nearby/"
family_list=read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/superfamily_list.txt", sep="\t", header=T,encoding="utf-8")

Table=read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/TE_in_enrichregion_25k.txt", sep="\t", header=T,encoding="utf-8")
shortTE<-subset(Table,complete.cases(Table))
Table=read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/TE_in_enrichregion_100k.txt", sep="\t", header=T,encoding="utf-8")
longTE<-subset(Table,complete.cases(Table))


#############TEST################################
status<-c("male","female","Other","ALL")
for (i in status){
  for(j in status){
    if(i==j){
     next
    }
    name<-paste(i,j)
    print(name)
    group1<-shortTE[shortTE$Sexuality==i,]
    group2<-shortTE[shortTE$Sexuality==j,]
    a<-wilcox.test(group1$Log2FoldChange,group2$Log2FoldChange)
    print(a$p.value)
  }
}
for (i in status){
  for(j in status){
    if(i==j){
      next
    }
    name<-paste(i,j)
    print(name)
    group1<-longTE[longTE$Sexuality==i,]
    group2<-longTE[longTE$Sexuality==j,]
    a<-wilcox.test(group1$Log2FoldChange,group2$Log2FoldChange)
    print(a$p.value)
  }
}
#########################################

p<-ggplot(longTE, aes(x=Sexuality,y=Log2FoldChange,colour=Sexuality))
p <- p +geom_violin()+geom_boxplot(width=.1,outer.colour=NA)
p<-p+theme_bw()+coord_flip()
plot(p)
ggsave(file="Enriched_region_violinplot_100k.png",plot=p,

              width = 9, height = 6, dpi = 300)
p<-ggplot(shortTE, aes(x=Sexuality,y=Log2FoldChange,colour=Sexuality))
p <- p +geom_violin()+geom_boxplot(width=.1,outer.colour=NA)
p<-p+theme_bw()+coord_flip()
plot(p)
ggsave(file="Enriched_region_violinplot_25k.png",plot=p,
       width = 9, height = 6, dpi = 300)

p<-ggplot(shortTE, aes(x=Log2FoldChange,fill=Sexuality,colour=Sexuality))
#p<-p+geom_histogram()
p <- p +geom_histogram(position = "dodge", alpha = 0.4)
p<-p+theme_bw()
ggsave(file="Enriched_region_histgram_25k.png",plot=p,
       width = 10, height = 8, dpi = 300 )
plot(p)
p<-ggplot(longTE, aes(x=Log2FoldChange,fill=Sexuality,colour=Sexuality))
#p<-p+geom_histogram()
p <- p +geom_histogram(position = "dodge", alpha = 0.4)
p<-p+theme_bw()
ggsave(file="Enriched_region_histgram_100k.png",plot=p,
       width = 10, height = 8, dpi = 300 )
plot(p)
