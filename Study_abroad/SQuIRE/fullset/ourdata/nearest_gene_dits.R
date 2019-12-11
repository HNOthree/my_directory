library(ggplot2)
directory<-"/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/txt/"
save_dir<-"/home/smiyake/sho/Fullset/SQuIRE/image"
file_name<-paste(directory,"TE_nearest_gene_ref.txt",sep='')
Table = read.table(file_name, sep="\t", header=T,encoding="utf-8")

p<-ggplot(Table, aes(x=Distance))
p <- p +geom_histogram(bins=50,na.rm = TRUE)+xlim(0,100000)
p<-p+theme_bw()
plot(p)
