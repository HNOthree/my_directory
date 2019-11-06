#In order to make index 

STAR \
--runThreadN 6 \
--runMode genomeGenerate \
--genomeDir ~/scp/Annotation \
--genomeFastaFiles ~/scp/Annotation/NC_019859.2.fasta \
--sjdbGTFfile ~/scp/Annotation/Latipes_merged_chr1.gtf
