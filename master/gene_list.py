import pandas as pd

gene=pd.read_csv("/home/shom-research/research/TE_m6A/SQUIRE/squire_fetch/hg38_refGene.gtf",sep="\t",names=("a","b","c","d","e","f","g","h","i"))
gene=gene.i
refgene_list=[]
for i in gene:
    splitted=i.split(" ")[1]
    splitted=splitted.replace('"','')
    splitted=splitted.replace(";","")
    refgene_list.append(splitted)

refgene_list=pd.DataFrame(list(set(refgene_list)),columns=["Gene"])


data=pd.read_csv("/home/shom-research/research/TE_m6A/download/gencode.v34.annotation.gtf",sep="\t",names=("Chromosome","b","Location","Start","End","f","Strand","h","Infomation"))
gene=data.Infomation
gene_list=[]
for i in gene:
    splitted=i.split(";")
    for j in splitted:
        if "gene_name" in j:
            gene_list.append(j.split(" ")[2].replace('"',''))
        else:
            continue
gene_list2=pd.DataFrame(gene_list,columns=["Gene"])
print(len(list(set(gene_list))))
annotation_data=pd.concat([data,gene_list2],axis=1,join="inner")
want_data=pd.merge(annotation_data, refgene_list, on='Gene')

print(want_data)
want_data=want_data.loc[:,['Gene','Chromosome','Start','End','Location','Strand','Infomation']]
want_data.to_csv("/home/shom-research/research/TE_m6A/data/Gene_annotation.txt",sep="\t",index=False)