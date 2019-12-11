#In order to make index 

STAR \
--runThreadN 6 \
--runMode genomeGenerate \
--genomeDir ~/Index/subset/ \
--genomeFastaFiles ~/Index/NC_019859.2.fasta \
--sjdbGTFfile ~/Index/Latipes_merged_chr1.gtf
