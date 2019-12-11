library(ggrepel)
library(scales)
directory<-"/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis"
file_name<-paste(directory,"/DESeq2_TE_separated.txt",sep='')
family_list=c("Olat_rnd-6_family-4702","Olat_rnd-1_family-855","Olat_rnd-1_family-197","Olat_helitron1","Olat_BEL_12","Olat_gypsy_186","Olat_rnd-6_family-2244","Olat_rnd-1_family-315","Olat_BEL_8")
for (family in family_list){
family_name<-family
Table = read.table(file_name, sep="\t", header=T,encoding="utf-8")
table<-subset(Table,complete.cases(Table))
subset<-table[table$Family==family_name,]

p<-ggplot(subset, aes(x=Log2FoldChange))
p <- p +geom_histogram(bins=50,na.rm = TRUE)
p<-p+theme_bw()+ggtitle(family_name)+xlim(-10,10)
plot(p)
}
save_name<-paste(directory,"/TE_lfc_distribution_family.png",sep='')
ggsave(file=save_name,plot=p,
       width = 6, dpi = 300)