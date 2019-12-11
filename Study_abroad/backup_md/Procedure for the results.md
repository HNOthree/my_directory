# Procedure for the results

## Data purify
1. calculated which TE is upstream of each gene
    * **Fullset/step1/data_purify/merge_TE_transcript_upstream.py**
    ![](https://i.imgur.com/oHuPoXr.png)
2. combine upstream data and log2 fold change data
    * **Fullset/SQuIRE/fullset/ourdata/merge_upstream.py**
    
    *TE and gene data*
    ![](https://i.imgur.com/K2raCQx.png)
    
    *TEdata*
    ![](https://i.imgur.com/HWm3wLs.png)
    
    *gene data*
    ![](https://i.imgur.com/k1xz8cU.png)

## TEtranscripts
I used this tool to estimate where each TE comes from.

1. made a STAR index file 
    * **Fullset/step1/STAR_index.sh**
2. ran STAR
    * **Fullset/step1/STAR_pair_end.sh**
3. ran TEtranscripts with the result from STAR bam file
    * **Fullset/step1/TE_transcript_Fullset.sh**
4. compared the result from TEtranscript and TEtools
    * **Fullset/step1/compareTwoTools.R**
    ![](https://i.imgur.com/cxOLJIl.png)

5. made a volcano plot
    * **Fullset/sig_diff_analysis/volcanoplot.R**
    ![](https://i.imgur.com/TVil3uk.png)
6. calculate TE coverage in each distance 
    * **Fullset/step2/coverage_upstream.py** 
    ![](https://i.imgur.com/ko2bbk3.png)
7. made a scatter plot (I merged TE log2 fold change in family)
    * **Fullset/step2/upstream_overlap_by_family_lfc.py**
    * **upstream_overlap_scatterplot.R**
    ![](https://i.imgur.com/Vcmi6Ka.png)
    ![](https://i.imgur.com/xq7UBYK.png)
    ![](https://i.imgur.com/IH0IcOd.png)

8. made a boxplot
    * **Fullset/step1/gene_vs_TE_lfc/gene_TE_lfc.R**
## SQuIRE
1. ran SQuIRE
    1. **SQuIRE/fullset/ourdata/clean.sh**
    2. **SQuIRE/fullset/ourdata/map.sh**
    3. **SQuIRE/fullset/ourdata/count.sh**
    4. **SQuIRE/fullset/ourdata/call.sh**
    * in squire_fetch file, we need
        * reference genome data
        * TE annotation data
        * gene annotation data
            * gtf,bed
        * chromInfo
            * chromosome name,length,someinformation
        * STAR index
    * You can see how I set the data at (~/shares/Sho/Results/SQuIRE/SQUIRE_data/squire_fetch)
    * all file must be named properly.
    * You ought not to use gtf that contains single exon data.
    →If you use, you have to re-write script
    (the detail is written in my dialog on **10/23**)
    * I had to change the SQuIRE/squire/Count.py script
    line 497 and 540
```python
joincommand_list = ["join", "-j", "12", "-t", "$\\t", "-o", "1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,1.10,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,2.10", newread_1_v2, newread_2_v2, ">" , matched_file_10k_v2]

```
to
```python
tab="'"+"\t"+"'"
joincommand_list = ["join", "-j", "12", "-t", tab, "-o", "1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,1.10,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,2.10", newread_1_v2, newread_2_v2, ">" , matched_file_10k_v2]
```
* Also, I had do change some script if you want to use a certain subclass such as "Unknown"
    1. SQuIRE/squire/Clean.py line 167
        * eliminate unwantedClass
    2. SQuIRE/squire/Call.py line 158
        * add subclass you want
    3. SQuIRE/squire/flag_newmi.py line 237
        * add subclass you want  

2. made a volcano plot
    * **SQuIRE/fullset/ourdata/volcanoplot.R**
    ![](https://i.imgur.com/LkEtnuY.png)
3. extracted TOP 100 TE in both male and female
    * **SQuIRE/data_purify/top_bottom.py**
5. made a histgram
    * **SQuIRE/fullset/ourdata/histgram.py**
    ![](https://i.imgur.com/u4t9Evl.png)
    * **SQuIRE/fullset/ourdata/make_sample_hist.py**
    ![](https://i.imgur.com/RBYr4UN.png)
        * compare mixture gaussian model
6. calculated correlation coefficiency in each family
    *  **SQuIRE/fullset/ourdata/correlation_by_family.py**
    
5. made a scatter plot using Data purify .2
    * **SQuIRE/fullset/ourdata/correlation_upstream.R**
    ![](https://i.imgur.com/UeF5icz.png)
    ![](https://i.imgur.com/rOpE851.png)
    ![](https://i.imgur.com/WzQQg9t.png)
    ![](https://i.imgur.com/r7b6LGz.png)

6. made a box plot using the data in SQuIRE 5
    * **SQuIRE/fullset/ourdata/box_plot.R**  
    ![](https://i.imgur.com/1YvOF1S.png)
    ![](https://i.imgur.com/lihTNgQ.png)
    ![](https://i.imgur.com/Nj5GI1l.png)
    ![](https://i.imgur.com/I8i1h4g.png)
    
    *Gene level*
    ![](https://i.imgur.com/Wg1kbI0.png)
    ![](https://i.imgur.com/EV5nOgA.png)

7. grouped by transcripts to gene and calculated Delta_LFC and log10 distance
    * **sh_datapurify.sh**
        * **grouped_by_gene.py**
        * **grouped_gene_number.py**
        * **purify_SQ_gene_TE_number.py**
8. saw a relationship between distance and Delta_LFC
    * **nearby_correlation.R**
    ![](https://i.imgur.com/Q2FYuz2.png)
    ![](https://i.imgur.com/6zqCEZV.png)

### Compare the enrichment
* **svg_enrich.py**
![](https://i.imgur.com/w7Lrs8F.png)
![](https://i.imgur.com/mmzVBFr.png)

In order to run it, following input is needed.
```javascript
python svg_enrich.py \
  -e /home/smiyake/shares/Sho/Bedfiles/25k.bed \
  -i /home/smiyake/sho/Fullset/SQuIRE/txt/TE_nearest_gene.txt \
  -o /home/smiyake/sho/Fullset/SQuIRE/image/nearby_tendency/TE_enrich/25k \
  -t 2 \
  -c /home/smiyake/shares/Sho/Annotation/oryLat2_STAR/chrNameLength.txt \
  -p 1

```
:::info
-e: bed file written enrichment region
-i: the intersction data
 The following columns are needed
 Chr
 Gene_start
 Gene_end
 TE_start
 TE_end
 TE_log2FoldChange
 Gene_log2FoldChange
-o: the directory you want to put the svg file
-t: threshold of lFC (float can be uesd)
-c: I used STAR index (No header is needed)
-p: optional if you want png file(maybe any letter is fine) If you use it, you must make "png" file at output directory
:::
### Calculated correlation coefficiency  again **in two regions**
 **enrich_analysis.R**
 ![](https://i.imgur.com/fP9Ci7f.png)
 In biassed region, correlation coefficiency tend to be higher than non biased region.
 
## SQUIRE (Including unknown)

### volcano plot 
It shows which TE is male-biased or female-biased.

**ourdata/package/volcanoplot.R**
![](https://i.imgur.com/hq8Ub8R.png)
* colored TE whose |lfc| is more than 1 and pvalue<0.05

The number of TE.
| Male | Female | other |
| -------- | -------- | -------- |
| 13325     | 3842     | 19941     |



### histgram
It shows the distribution of LFC
X axis: Log2FoldChange. The more lfc is, the more male biased the TE is. The less lfc is, the more female biased the TE is.
:::info
$Log2FoldChange=\frac{ExpressionInTestis}{ExpressionInOvary}$  
:::
Y axis: The number of TE whose lfc is between each threshold.

**ourdata/package/TE_lfc_distribution.R**
![](https://i.imgur.com/AYBr3Zt.png)
* seems three peaks which are male_biased(around5),neutral(around1.5),female_biased(around -4.5)
* if you use **ourdata/TE_distribution_family.R**, you can see each distribution of lfc.
    * You can find some families are sexuality-biased.
### violinplot
It shows the violin plot of lfc in each region using bed file which is described enrich region.

**ourdata/package/violinplot**
![](https://i.imgur.com/7JzyVlt.png)
* Expression of TE is shifted in both male and female region
* you can also see the histgram of lfc
![](https://i.imgur.com/L4ApWXu.png)

### TE region

* You can see the expression of each TE visually.
* The darker the color is, the more TE tend to be expressing.
:::info
blue: TE is male-biased.
red: TE is female-biased.
green: TE is netral.
:::

**ourdata/TE_svg.py**
![](https://i.imgur.com/nvT4Uwv.png)
![](https://i.imgur.com/fORYekB.png)

### TE-gene region

It shows the region whose both TE and gene lfc is more than threshold.I this case, the pair between TE and gene is only the closest one.

**ourdata/package/svg_enrich.py**
![](https://i.imgur.com/e9q7Mdj.png)



### Triagram
It shows where each family is enriched using bed file.

**ourdata/package/triagram.R**
![](https://i.imgur.com/kmg6puK.png)
![](https://i.imgur.com/Di763qc.jpg)
1 Olat_rnd-6_family-4702
2 Olat_rnd-1_family-855
3 Olat_rnd-1_family-197
4 Olat_helitron1,Olat_gypsy_203
5 Olat_BEL_12
6 Olat_gypsy_186
7 Olat_rnd-6_family-2244
8 Olat_rnd-1_family-315
9 Olat_BEL_8

* some family tend to be located in male/female region

#### Triagram with only expressd TE

It shows where each family is located compare to only expressing TE.

**ourdata/package/triagram_express.R**
![](https://i.imgur.com/GFRY4sl.png)

Most of TE is neutral from triagram [result above](https://hackmd.io/z7vhKNaEQ-m94y6EX01bsg?view#Triagram0) but expressing TE tends to be male-biased

### statistic test about enrich region
![](https://i.imgur.com/wHQBW4X.png)
![](https://i.imgur.com/cf1el7c.png)
![](https://i.imgur.com/RSne3YH.png)

![](https://i.imgur.com/bBknu7Q.png)
![](https://i.imgur.com/m1r8t2K.png)
![](https://i.imgur.com/aylVvrY.png)
![](https://i.imgur.com/skenTEo.png)

Some of TE family is significantlly appeared in male region

### volcanoplot of 9 family
Olat_BEL_8
![](https://i.imgur.com/Qcw1C54.png)
Olat_BEL_12
![](https://i.imgur.com/qmta5JX.png)
Olat_gypsy_186
![](https://i.imgur.com/ibEg0Fi.png)
Olat_helitron1
![](https://i.imgur.com/6xVmjku.png)
Olat_rnd-1_family-855
![](https://i.imgur.com/Ku8Wlu7.png)
Olat_rnd-1_family-315
![](https://i.imgur.com/fpuHurY.png)
Olat_rnd-1_family-197
![](https://i.imgur.com/tQvr6ID.png)
Olat_rnd-6_family-2244
![](https://i.imgur.com/AKtbW10.png)
Olat_rnd-6_family-4702
![](https://i.imgur.com/B5s7iWi.png)

Olat_helitron1,Olat_rnd-1_family-197 are also significantlly appeared in male region.
Olat_BEL_8 is a bit appeared in male and female region.

### statistic test of TE-gene region

counted TE-gene pair whose both gene and TE |lFC| is more than threshold grouped by family.The pair is TE and the closest gene.
The more lfc is, The more high-lfc-pair of TE and gene exist frequently. 

**ourdata/TE-gene_region_appeared_frequently.R**
I set threshold between 1~5
More than 3 means both |TE-lfc| and |gene-lfc| is more than3
![](https://i.imgur.com/nkks8kg.png)



### boxplot of correlation coefficiency
**ourdata/package/boxplot_correlation.R**
25k
![](https://i.imgur.com/ZwkqJJl.png)
![](https://i.imgur.com/wkUgWZX.png)

The correlation coefficiency(CC) in biased_region is always higher than that of all.However the CC in only male and female is lower than that of all.
It can be because of the number of matched data. I only calculated CC when the number of TE is more than 5.Threfore the possibility that the number is more than 5 in biasedregion tends to be higher.

100k
![](https://i.imgur.com/BEC7X98.png)
**Pvalue**
~1000
|| male | female | non_biased |
|---| -------- | -------- |---|
|male|----|0.16227|0.27859|
|female|0.16227|---|0.44475|
~5000
|| male | female | non_biased |
|---| -------- | -------- |---|
|male|----|0.013056|0.025168|
|female|0.013056|---|0.362279|
~10000
|| male | female | non_biased |
|---| -------- | -------- |---|
|male|----|0.0071908|0.0013778|
|female|0.0071908|---|0.378047|
![](https://i.imgur.com/NGzzArZ.png)


