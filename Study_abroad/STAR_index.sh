#In order to make an index 

STAR \
--runThreadN 10 \
--runMode genomeGenerate \
--genomeDir /mnt/Reference \
--genomeFastaFiles /mnt/Reference/GCF_002234675.1_ASM223467v1_genomic.fasta \
--sjdbGTFfile /mnt/Annotation/Latipes_merged.gtf
