# Results about Orat_helitron1

## My results
### The expression of helitron1 is male-biased.
I made a volcano plot with the result from SQuIRE.
![](https://i.imgur.com/wq3xVHT.png)
**(tetranscript_scrpts/SQuIRE/fullset/ourdata/package/volcanoplot.R)**
It shows the expression of helitron1 is male-biased. So I tested whether this bias is significant or not.

matrix of each number
||male|female|neutral|
|--|--|--|--|--|
|ALL|15492|4167|17449|
|Helitron1|23|0|2|
X-squared test
*pvalue=2.259×10^-6^*

**(/home/smiyake/src/tetranscript_scrpts/SQuIRE/fullset/ourdata/mosaicplot.R)**
This table suggests that helitron1 significantly express in male.


From these results, Helitron1 is male-biassed TE family.


### Helitron1 tends to be located near male-biased gene

Mr.Corentin made a bed file about male or female gene enrich region from the analysis.
![](https://i.imgur.com/Bzx5uv9.png)
![](https://i.imgur.com/2lfsSVP.png)

I counted how many each TE is located in this region grouped by male,female,and other region.
![](https://i.imgur.com/1W5eqhe.png)
**(/home/smiyake/src/tetranscript_scrpts/SQuIRE/fullset/ourdata/TE_svg.py)**
After counting it,I made a triangular diagram.
It shows that some family tend to be located male or female region.

![](https://i.imgur.com/pMYGj0V.png)
**(/home/smiyake/src/tetranscript_scrpts/SQuIRE/fullset/ourdata/package/triagram.R)**
From this figure, Heritron1 seems to be located male region.

I tested whether this behavior is significant or not.
![](https://i.imgur.com/MtzbQPQ.png)
**(/home/smiyake/src/tetranscript_scrpts/SQuIRE/fullset/ourdata/enrichment.R)**
It shows that Helitron1 is significantly appeared in male-biased-gene region.

### The expression of genes close to helitron1 is also male biased.
I saw the Log2FoldChange expression between TE and gene which is closest to TE.
**(/home/smiyake/src/tetranscript_scrpts/SQuIRE/fullset/ourdata/package/nearest_gene.py)**
**(/shares/Sho/Results/SQuIRE/include_unknown/analysis/TE_nearest_gene_ref.txt)**
|TE|Gene|TE_LFC|Gene_LFC|distance|
|--|--|--|--|--|
|TE1|Gene4|1.4|2.5|1300bp|
|TE2|Gene5|-1|-5|15000bp|
|TE5|Gene6|5|4.3|200bp|
|...|...|...|...|...|

The distribution of the nearest gene was like this.
![](https://i.imgur.com/2Slgh4H.png)
1-100000bp
![](https://i.imgur.com/8VfzSwx.png)

**(/home/smiyake/src/tetranscript_scrpts/SQuIRE/fullset/ourdata/package
/high_low.py)**
**(/shares/Sho/Results/SQuIRE/include_unknown/analysis/family_nearestgene_count_ref.txt)**
I counted the number whose both |TElfc| and |genelfc| are more than threshold.
|Family|expressing TE|morethan1|morethan2|...|
|--|--|--|--|--|
|family1|100|30|23|...|
|family2|50|30|2|...|
|family3|30|20|18|...|
|...|...|...|...|...|

I tested whether the number of combination is significantly higher than average.
![](https://i.imgur.com/J94GuxP.png)
![](https://i.imgur.com/5SP7sb1.png)
![](https://i.imgur.com/mKW3L1a.png)
![](https://i.imgur.com/R73Opa9.png)
![](https://i.imgur.com/uE4P01v.png)

These figures suggest that if Helitron1 is expressing, the expression of the closest gene get biased. 

### The expression between Helitron1 and its neighbourhood gene is correlated.

I saw lfc of Helitron and lfc of gene which is located within each distance.
![](https://i.imgur.com/dczHa9v.png)
![](https://i.imgur.com/CJMwE5w.png)
![](https://i.imgur.com/qj3T6rC.png)
![](https://i.imgur.com/Z4XriL9.png)

In the close region, it seems to have a correlation.Pvaue is enough low suggesting that helitron1 and its neighbourhood gene have some relation.

## The paper Mr.Corentin wrote([URL](https://mobilednajournal.biomedcentral.com/articles/10.1186/s13100-019-0185-0) )
1. It is known that MSL increases neighboring gene expression to compensate for the absence of one X chromosome in XY male of **Drosophia**.
:::info
MSL:Male Specific Lethal.
It is a male specific complex that recognizes MRE(MSL Recognition Elements)
:::
2. MREs are found at multiple loci interspersed on the X chromosome.
3. MREs are carried by **Helitron** and helitron regulate cis genes close to their insertion sites.

From these facts,Helitron can be also related to male-specific gene control.

## The paper about Helitron(Mr.Jean-Nicolas is one of authors [URL](https://www.liebertpub.com/doi/pdf/10.1089/zeb.2006.3.39))

### Introduction
Helitron has two domains(Replication protein domain and Helicase domain)
It is results of platyfish.

### Constitution of Helitron 
First,Helitron in platyfish lacks introns, they contain 8448 nucleotides encoding conceitual 2816 amino acid protein.
Helitron has not only replication domain and helicase domain, but also OTU-like domain and apurinic-apyrymidinic-like endonuclease(Fig1).
:::info
OTU:Essential for female fertility; germ cell division and differentiation([URL](https://www.uniprot.org/uniprot/P10383))
:::

### Organization and expression of Helitron
In sexuality chromosome, there are about 10 insertion of Helitron. 
And the number of Helitron in Y chromosome is more than that in X chromosome.(Fig4)
:::success
I confirmed that in Medaka, Helitron tends to be located in male-biased-gene region.
:::
They also did RT-PCR of RNA with Helitron in diferrent tissue.
They comfirmed that the RNA level is higher in males than that in females.
Also, they comfirmed that the band is light in testis while there is not band in ovary.(Fig5)
:::success
This is matched with my result (volcanoplot of LFC).
:::

### Preservation inter-species.
Helitron in Medaka also has four domain(replication domain,helicase domain,AP-endonuclease domain,and OTU-like domains)(Fig1).
They made two philogenetic tree. One is about helicase protein domain in helitlon.
The other one is about OTU-like domain in helitron. Both results suggest that helitron in platy fish is quite similar to that in Medaka.

### Other (This result doesn't seems to be related to my results.)
Thay also confirmed that almost all poeciliids has helitron with OTU-like domain, helicase domain,replication domain and endonulease domain.



## My opinion
1. Helitron1 is male_biased TE family.
2. One of following two things seems to be applied.
    1. Once Helitron1 is inserted,its neighbourhood genes become male biased.
    2. Helitron1 prefer male-biased gene region. 
3. Some paper seem to support my result.
    1. Helitron plays an important role in Platyfish,and the sequence in Madeka is quite similar to that in Platyfish 
    2. In Platyfish,the RNA expression.which has Helitron seems to be male-biased. 
5. Helitron1 can regulate gene by...
    1. MREs also exist in *Orizia Latipes* and MSL recognize them.
    2. Helitron can recruit transcript factor
    3. Noncoding RNA which has helitron binds neighbourhood gene, and promotes ｔranscription
    4. something related to OTU-like domain.
 