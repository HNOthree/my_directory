library(ggtern)
Table = read.table("/home/smiyake/sho/Fullset/SQuIRE/txt/TE_percentage_family.txt", sep="\t", header=T,encoding="utf-8")
table<-subset(Table,complete.cases(Table))
Class_list<-c('RC', 'LINE', 'LTR', 'SINE', 'DNA')
family_list<-c('Helitron', 'L1', 'ERV1', 'CR1-Zenon', 'tRNA-Core-L2', 'hAT-Charlie', 'Gypsy', 'L2', 'PIF-Harbinger', 'RTE-BovB', 'tRNA', 'TcMar', 'TcMar-Tc1', 'Ngaro', 'hAT-Ac', 'Polinton', 'Rex-Babar', 'Harbinger', 'PIF-Harbinger?', 'EnSpm-CACTA', 'ERV', 'hAT', 'MITE?', 'BEL-Pao', 'Copia', 'Dong-R4', 'PIF-ISL2EU', 'Helitron?', 'Penelope', 'TcMar-Tc2', 'hAT-Tip100', 'I', 'MIR', 'PiggyBac', 'TcMar-Tigger', 'Gypsy-Cigr', 'Zisupton', 'L1-Tx1', 'Crypton', 'MITE', 'P', 'Proto2', 'TcMar-ISRm11', 'Mariner', 'Gypsy?', 'Pao', 'hAT-Charlie?', 'TcMar-Tc1?', 'Copia?', 'ERVK', 'hAT-Ac?', 'tRNA-L2?', 'Academ', 'RTE-X', 'MuDr', 'hAT-Tol2', 'hAT-hAT5', 'DIRS', 'R2-Hero')

p <- ggtern(data = table, aes(Male, Female, Neutral,colour=Class))
#p <- p+stat_density_tern(geom = "polygon",aes(fill=..level..),base = "ilr")
p <- p + geom_point()+theme_bw()
p<-p+theme_showarrows()
ggsave(file = "/home/smiyake/sho/Fullset/SQuIRE/image/tridiagram/ALL.png", plot = p)
plot(p)

for(i in Class_list){
  class_subset<-table[table$Class==i,]
  p <- ggtern(data = class_subset, aes(Male, Female, Neutral,colour=Superfamily))
  p <- p + geom_point()+theme_bw()
  p <- p +ggtitle(i)
  p<-p+theme_showarrows()
  name<-"/home/smiyake/sho/Fullset/SQuIRE/image/tridiagram/"
  name<-paste(name,i,sep='')
  name<-paste(name,'.png')
  ggsave(file = name, plot = p)
  plot(p)
  
}


for(i in family_list){
  family_subset<-table[table$Superfamily==i,]
  p <- ggtern(data = family_subset, aes(Male, Female, Neutral,colour=Data_count))
  p <- p + geom_point()+theme_bw()
  p <- p +ggtitle(i)
  p<-p+theme_showarrows()
  name<-"/home/smiyake/sho/Fullset/SQuIRE/image/tridiagram/"
  name<-paste(name,i,sep='')
  name<-paste(name,'.png')
  ggsave(file = name, plot = p)
  plot(p)
  
}
