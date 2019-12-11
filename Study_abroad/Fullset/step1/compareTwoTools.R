#The script to compare the results from TEtranscripts and TEtools

table = read.table("/home/smiyake/shares/Sho/Results/TEtranscripts/step1/two_results_merge.txt", sep="\t", header=T,encoding="utf-8")
library(ggplot2)
library(ggrepel)
x<-table[,"Log2FoldChange_TEtranscripts"]
y<-table[,"Log2FoldChange_TEtools"]
correlation=cor(x, y, method="pearson")
print(correlation)
#Colored by Class
g <- ggplot(table, aes(x=Log2FoldChange_TEtools,y=Log2FoldChange_TEtranscripts,colour=Class))
g <- g + geom_point()+geom_abline(slope=1,colour="red")+theme_bw()　#geom_pointは「散布図で書いてね」と指定するため
g=g+xlim(-8,8)+ylim(-8,8)
ggsave(file = "Correlation.png", plot = g)
plot(g,add=TRUE)

Class_list<-c("DNA","DNA?","LINE","LTR","nonLTR","RC","Retro","SINE","Unknown","Unspecified")

#each Class and coloured group by superfamily
for( i in Class_list){
  print(i)
  
  subset<-table[table$Class==i,]
 
  g <- ggplot(subset, aes(x=Log2FoldChange_TEtools,y=Log2FoldChange_TEtranscripts,colour=Family))
  g <- g + geom_point()+geom_abline(slope=1,colour="red")
  g=g+xlim(-8,8)+ylim(-8,8)
  name<- paste(i, ".png", sep="")
  ggsave(file = name, plot = g)
  
  x<-subset[,"Log2FoldChange_TEtranscripts"]
  y<-subset[,"Log2FoldChange_TEtools"]
  correlation=cor(x, y, method="pearson")
  print(correlation)
  }
