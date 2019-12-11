
# Sho Dialog
## Goal
Identifying which TE is male or female specific expressed.
Investigating whether a certain TE contributes to gene expression or not.
## TEtranscript
It is a tool to estimate gene expression without ignoring TEs.
### What is needed for TEtranscript
- Alignment File
    - BAM or SAM
- Gene Annotation data
    - GTF
- TE Annotation file
    - GTF

if you have not BAM,SAM file
- Read data (KD and control) 
    - fasta
- Reference Genome
    - fa
### output data
- KDvsControl.cntTable
    - contains estimated raw abundance counts for all genes and TEs as **Tab-delimited table**
- KDvsControl_DESeq.R
    - R script used by TEtranscripts for differential expression analysis
- KDvsControl_gene_TE_analysis.txt
    - Differential expression results from Deseq for all genes and TEs
- KDvsControl_sigdiff_gene_TE.txt
    - a subset of the differential expression analysis table for only those genes and TEs **that passed the-Pvalue significance criteria**
## SQuIRE
It is a tool to estimate gene expression without ignoring TEs.
In addition, we can estimate **loci-specific TE** from results
### In order to run SQuIRE
we don't need reference and annotation data because *SQuIRE fetch* can download the data.
However if we use our data, we have to do folloing things.
1. define spicies
    * in my case I define *ourLat* 
2. prepare reference data
    * GCF_00~.fasta-> ourLat.chromFa/ourLat.Fa
        * ourLat.chromFa is a **directory**
3. prepare TE annotation data
   * we can define TE annotation data in SQuIRE clean
4. prepare gtf/bed/chromInfo data
    * chromInfo data contains 
        1. chromosome name
        2. the length of chromosome
        3. some infomation(I don't know exactly)
* You ought to run SQuIRE call in the parent directory of squire_call because you cannot specify　absolute path.
* Besides, some error may occur.
    * KeyError
## 9/27
### What I did today
* Explanation about the project
* Read about TEtranscript
* install pysam,samtool,TEtoolkit
* Try making Index using STAR
    * Spend much time


### Difficulty
* I could not deal with the error "python setup.py install --prefix=$HOME" 
    * cannot deal with PATH 

## 9/30
### What I did today
* separate Reference genome to each chromosome because running STAR needs huge amount of memory
* I made a STAR Index of chr1
    **STAR_index_chr1.sh**
* I runned STAR with two subset-data
    **STAR_pair_end_chr1.sh**
    * Clean1latF_1_20181003_sub.fq.gz
    * Clean1latF_2_20181003_sub.fq.gz
    * Clean2latF_1_20181003_sub.fq.gz
    * Clean2latF_2_20181003_sub.fq.gz
    * Clean3latF_1_20181003_sub.fq.gz
    * Clean3latF_2_20181003_sub.fq.gz
    * Clean4latM_1_20181003_sub.fq.gz
    * Clean4latM_2_20181003_sub.fq.gz
    * Clean5latM_1_20181003_sub.fq.gz
    * Clean5latM_2_20181003_sub.fq.gz
    * Clean6latM_1_20181003_sub.fq.gz
    * Clean6latM_2_20181003_sub.fq.gz
* made GTF file from TE_only_Latipes_annotation_file.ucsc
**ucsc_to_GTF.py**
    * TE_only_Latipes_annotation_file_chr1.gtf
    * TE_only_Latipes_annotation_file_chr1_purified.gtf
* Tried running TEtranscripts
    * Seems to run well
    * But I couldn't distinguish which TE comes from in copy level
* Send data to RAINbio with scp 
    * Full dataset
    * Gene Annotation
    * TE Annotation
* Confirmed that STAR can run in Virtual Machine

## 10/1
### What I did today
* tried to run TEtranscripts im subset
* dealed with error about installing pysam
* sent fullset data to cloud
* Run the scripts to make index with STAR on fullset data
* gzip Fullset data
### Difficulty
* Dealing with error was so hard
    * pip was wrong because once pip was conducted, module went to python3 library.
* Storage is filled with data
    * move Fullset data to /mnt/... to avoid this problem 

## 10/2
### What I did today
* Runned STAR on Fullset data
* Runned TEtranscripts with Fullset data
    * took much time to finish .
* Compared two tools between TEtranscripts and TEtools
    * TEtranscripts tended to estimate Log2fc higher than TEtools.
* Chacked correlation separated by class  
 
![](https://i.imgur.com/AgJbO38.png)
  
## 10/3
### What I did today
* Calculated the average of log2-fold-change
    * selected top/bottom 50 each
* Made one R script to see the relationship between counts and log fold change 

## 10/4
### What I did today
* Made transcripts/exon annotation file from Latipes_merged.gtf
* Calculated whether each TE is upstream/downstream each gene or not

## 10/7
### What I did today
* Saw a correlation between LFC of Gene and LFC of TE which is located upstream or downstream gene.
    * seemed no correlation globally.
![](https://i.imgur.com/xizPkW4.png)
 upstream
![](https://i.imgur.com/eWXGKAk.png)
downstream
* modified python script
    * added a distance between TE and transcripts
* counted the number of the combination of TE and transcript which were located with in 500000bps
    * TcMar-Tc1 seems to have a peak. So I need to check more cafully.
![](https://i.imgur.com/zf48L6W.png)
 The histgram of TcMar-Tc1
 
 ## 10/8
 ### What I did today
 * made an intron file of Latipes
 * searched TE which is located in intron
 * saw a relationship
     * Distance and Gene lfc
     seems nothing interesting.
     ![](https://i.imgur.com/QfsebR7.png)
     ![](https://i.imgur.com/ID4UkhQ.png)        The figure of downstream was messy because the number of TE which is located downstream with in 500000 bp was very small.

     * Intron number and Gene lfc
         * not completed because making file about TE and intron need a lot of time.
    
* try to investigate above research with only significantly different TE

## 10/9
### What I did today
* made a volcano plot
    * many TE tend to express in male.
![](https://i.imgur.com/0do6Pyz.png)
* made an annotation file of TE which is male or female specific.
* make a TE list which is across transcript start site.
### Difficulty
* I found to have make a eIIIatal mistake
    * Inequality was opposite.
  	    * As a result, I have to much more calculate.
		* It takes too much time so I have to change some scripts.
		* **So What I did on 10/7 and 10/8 was useless.**

## 10/10
### What I did today
* made some scripts to calculate whether each TE is upstream of gene
    * re-make
    * merge_TE_transcript_upstream.py
    * merge_TE_transcript_downstream.py
    * merge_TE_transcript_upstream_overlap.py
    * merge_TE_transcript_downstream_overlap.py
* saw the relationship TE lfc and gene lfc on these TE.

## 10/11
### What I did today
* counted the number of TE which is expressed significantly different
* compare gene log2 fold change groupby sexuality specific TE.
male

![](https://i.imgur.com/jFdieRL.png)

female

![](https://i.imgur.com/pWMBSFk.png)

family
![](https://i.imgur.com/UiwP5Ao.png)
* tried to investigate relationship between TE LFC which is located upstream of gene and gene LFC
    * In terms of distance, there seems a peak around 500bp from Transcript start site.
![](https://i.imgur.com/fR5s9lJ.png)
![](https://i.imgur.com/OadvNCq.png)
    * But there seems no relationship between distance and gene LFC

![](https://i.imgur.com/0EgNdU5.png)
* I noticed that when female specific ERV1 is located upstream of gene, almost all gene expresstion increased in female. 
![](https://i.imgur.com/0PNtRnX.png)

## 10/14
### What I did today
* refined some figures
* made a presentation slide.

## 10/15
### What I did today
* made a presentation slide.

## 10/16
### What I did today
* Meeting
* calculate mean gene expression group by family

## 10/17
### What I did today
* calculated genome coverage
![](https://i.imgur.com/NnapuJ6.png)
* read a paper about SQuIRE.

## 10/18
### What I did today
* read a paper about SQuIRE.
* tried to run SQuIRE.

### Difficulty
* I cant deal with the error *UnboundLocalError: local variable 'prev_TE_ID' referenced before assignment*
    * I don't know whether its error is due to me or python script.

## 10/21
### What I did today
* tried to run SQuIRE with subset
    * subset/( map.sh/ count.sh/ call.sh)

* sent fullset data to RAINbio 


## 10/22
### What I did today
* tried to run SQuIRE with fullset data
    * clear,map,count
        * took much time
    * used data from ucsc
* To create STAR file with OUR reference genome
* To create gtf data
* To create bed data
* To create chromInfo data
* extract genes from list
* completed to run SQUIRE with subset data
* tried to SQuIRE clean with our data
* tried to SQuIRE map,count,call with our data

## 10/23
### What I did today
* tried to ru SQuIRE with fullset data
    * Count ,Call
* re-built STAR index 

### What I have difficulty
* When I run squire count, the key error was always ocurred.
    * That's because squire misunderstood strand when it recognize mono-exon gene.
    *  I have to change the scripts (SQuIRE/squire/Count.py)

line 219-225
```javascript
 if len(line) == 9:
  if gtf_line.category=="exon":
   transcribed_length=int(gtf_line.stop) - int(gtf_line.start)
   counts = gtf_line.coverage*transcribed_length/int(read_length)
   if counts > 0:
    gene_dict[(gtf_line.Gene_ID,gtf_line.strand)].add_counts(counts)
    gene_dict[(gtf_line.Gene_ID,gtf_line.strand)].add_tx(gtf_line.transcript_id)  
 else:
    ref_line=gtfline(line[9:18])
    gene_dict[(ref_line.Gene_ID,ref_line.strand)].add_tx(gtf_line.transcript_id)
```
to
```javascript
try:
 if len(line) == 9:
  if gtf_line.category=="exon":
   transcribed_length=int(gtf_line.stop) - int(gtf_line.start)
   counts = gtf_line.coverage*transcribed_length/int(read_length)
   if counts > 0:
    gene_dict[(gtf_line.Gene_ID,gtf_line.strand)].add_counts(counts)
    gene_dict[(gtf_line.Gene_ID,gtf_line.strand)].add_tx(gtf_line.transcript_id)  
 else:
    ref_line=gtfline(line[9:18])
    gene_dict[(ref_line.Gene_ID,ref_line.strand)].add_tx(gtf_line.transcript_id)
 except KeyError:
  continue
```
add `try` and `except` 


## 10/24
### What I did today
* searched the cause why the number of columns in DESeq2_TE_only.txt id much smaller than the number of TE annotation
    * they eliminate TEs which is NOT expressed in either male or female
*  saw correlation between TE and gene
    * can separate 4 pattarns
        1. have a sorrelation
        2. Only TE is sexuality speciic
        3. Only gene is sexuality specific 
        4. Both TE and gene are sexuality specific
    
    
## 10/25
### What I did today
* saw a distribution of TEs
![](https://i.imgur.com/pjq4ZXi.png)
![](https://i.imgur.com/V66hvbz.png)
![](https://i.imgur.com/cFxYhxK.png)

* investigated the correlation between gene LFC and LFC of TE,which is upstream of gene
![](https://i.imgur.com/9zuJK4X.png)
![](https://i.imgur.com/aVsQoPB.png)

* investigate why the number of TE in squire call is much smaller than that in squire fetch

## 10/28
### What I did today
* make a correlation coefficient list that is more than 0.5 or less than -0.5 and the number of data is more than 5.
* tried to find the reason why the number of TE in Squire Call is decreased.
    * They defined cutoff, which is calculated from TE_counttable
        * the average of the number (exclude 0) is more than 5
        →ignore TE with low expression 
* re-do SQuIRE with an another TE annotation file
    * convert TE whose Class and suprefamily is same to Unknown.

## 10/29
### What I did today
* Arrengement of data
* compared TE distribution and Gaussian mixture model
    * make_sample_hist.py
* ran SQuIRE count,call
* made a script which calculate correlation efficiency grouped by family
    * correlation_by_family.py
* re-calculated which TE is upstream of gene and combined these log2 fold change
    * merge_upstream.py
    * merge_downstream.py 

## 10/30
### What I did today
* made a box plot about correlation coeficiency
![](https://i.imgur.com/859TZZs.png)
![](https://i.imgur.com/dITi7pt.png)

* organized scripts to README.md

## 11/1
### What I did today
* Discussed about results
* made bar praph abount TE log2FC
* Tested correlation coefficiency

## 11/4
### What I did today
* make a ｔriangular diagram about TE 
![](https://i.imgur.com/izTTXsj.png)
* made a presentation slide

## 11/6
### What I did today
* calculate the distance between TE start site and Transctipt start site
* add liner regression to R scripts


## 11/8
### What I did today
* tried to investigate the relationship between distance and delta log2 fold change
    * prepared data
        **grouped_by_gene.py** 
        

## 11/13
### What I did today
* saw the relationship between distance and delta TE

![](https://i.imgur.com/cnR5vAJ.png)
### Difficulty
* I found a bug in the script
    * When I calculated the length of gene, I eliminated almost all information about the relationship between TE and gene

## 11/14
### What I did today
* wrote scripts to investigate TE and gene which is adjacent to TE

## 11/15
### What I did today
* organized the data
* organized the procedure
* prepare the scripts for the number and distance of gene
    * I have to wait until the programs, which are Gene_TE_number_connect.py and Gene_TE_distance_connect.py, are ended. 

## 11/18
### What I did today
* see delta_LFC
![](https://i.imgur.com/Axs18Zx.png)

* see the TE tendency where they are male/female biased region 
![](https://i.imgur.com/6cBXKlf.png)

## 11/19
### What I did today
* compared TE-gene biassed region and sexuality biassed active region
![](https://i.imgur.com/SoR2Vz6.png)

## 11/20
### What I did today
* tried to devided to two groups(TE-gene enrich region and non region)
![](https://i.imgur.com/P41VmOF.png)
* calculated the percentage
![](https://i.imgur.com/7lWE5Wa.png)

* calculated correlation coefficiency again but I separated biased region and non_biased region(bed file)
![](https://i.imgur.com/ix4LDN5.png)
* investigated whether some motif is existing or not

## 11/21 
### What I did today
* made a trigram
![](https://i.imgur.com/OiFReTx.png)

* made a volcanoplot
![](https://i.imgur.com/WLkHVoF.png)

## 11/22 
### What I did today
* Ran SQuIRE with unknown TE annotation data
* made pipeline to analize what I did in this internship

## 11/25
### What I did today
* Ran SQuIRE with unknown TE annotation data
* made pipeline to analize what I did in this internship

## 11/29
### What I did today
* analized in male region and female region with unknown family


![](https://i.imgur.com/kmg6puK.png)
![](https://i.imgur.com/wHQBW4X.png)
![](https://i.imgur.com/hq8Ub8R.png)
![](https://i.imgur.com/7JzyVlt.png)
![](https://i.imgur.com/L4ApWXu.png)
![](https://i.imgur.com/BEC7X98.png)
![](https://i.imgur.com/685CPxY.png)

## 12/2
### What I did today
* organized the results about Olat_helitron1
https://hackmd.io/@sho/S1A6Ktfpr