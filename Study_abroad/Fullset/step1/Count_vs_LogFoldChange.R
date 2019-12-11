table = read.table("/home/smiyake/sho/Fullset/txt/lfc_groupedby_family.txt", sep="\t", header=T,encoding="utf-8")
library(ggplot2)
library(ggrepel)
g <- ggplot(table, aes(x=Counts,y=Log2FoldChange_ave,colour=Class))
g <- g + geom_point()　#geom_pointは「散布図で書いてね」と指定するため
ggsave(file = "Count_vs_lfc.png", plot = g)
plot(g)


g <- ggplot(table, aes(x=Counts,y=Log2FoldChange_ave,label=Family,colour=Class))
g <- g + geom_point()+ geom_text_repel()　#geom_pointは「散布図で書いてね」と指定するため
ggsave(file = "Count_vs_lfc_labeled.png", plot = g)
plot(g)
