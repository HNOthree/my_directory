#In order to run STAR with pair end reads

STAR --runThreadN 12 \
 --genomeDir /mnt/Reference/ \
 --sjdbGTFfile /mnt/Annotation/Latipes_merged.gtf \
 --sjdbOverhang  100 \
 --readFilesIn  /mnt/Fullset/Clean1latF_1_20171002_sub.fq.gz /mnt/Fullset/Clean1latF_2_20171002_sub.fq.gz \
 --readFilesCommand zcat \
 --outSAMtype BAM Unsorted \
 --winAnchorMultimapNmax  200 \
 --outFilterMultimapNmax  100  \
 --outFileNamePrefix /mnt/Fullset/bam/Clean1latF

echo "F1 is done"

STAR --runThreadN 12 \
 --genomeDir /mnt/Reference/ \
 --sjdbGTFfile /mnt/Annotation/Latipes_merged.gtf \
 --sjdbOverhang  100 \
 --readFilesIn  /mnt/Fullset/Clean2latF_1_20171002_sub.fq.gz /mnt/Fullset/Clean2latF_2_20171002_sub.fq.gz \
 --readFilesCommand zcat \
 --outSAMtype BAM Unsorted \
 --winAnchorMultimapNmax  200 \
 --outFilterMultimapNmax  100  \
 --outFileNamePrefix /mnt/Fullset/bam/Clean2latF

echo "F2 is done"

STAR --runThreadN 12 \
 --genomeDir /mnt/Reference/ \
 --sjdbGTFfile /mnt/Annotation/Latipes_merged.gtf \
 --sjdbOverhang  100 \
 --readFilesIn  /mnt/Fullset/Clean3latF_1_20171002_sub.fq.gz /mnt/Fullset/Clean3latF_2_20171002_sub.fq.gz \
 --readFilesCommand zcat \
 --outSAMtype BAM Unsorted \
 --winAnchorMultimapNmax  200 \
 --outFilterMultimapNmax  100  \
 --outFileNamePrefix /mnt/Fullset/bam/Clean3latF

echo "F3 is done"

STAR --runThreadN 12 \
 --genomeDir /mnt/Reference/ \
 --sjdbGTFfile /mnt/Annotation/Latipes_merged.gtf \
 --sjdbOverhang  100 \
 --readFilesIn  /mnt/Fullset/Clean4latM_1_20171002_sub.fq.gz /mnt/Fullset/Clean4latM_2_20171002_sub.fq.gz \
 --readFilesCommand zcat \
 --outSAMtype BAM Unsorted \
 --winAnchorMultimapNmax  200 \
 --outFilterMultimapNmax  100  \
 --outFileNamePrefix /mnt/Fullset/bam/Clean4latM

echo "M1 is done"

STAR --runThreadN 12 \
 --genomeDir /mnt/Reference/ \
 --sjdbGTFfile /mnt/Annotation/Latipes_merged.gtf \
 --sjdbOverhang  100 \
 --readFilesIn  /mnt/Fullset/Clean5latM_1_20171002_sub.fq.gz /mnt/Fullset/Clean5latM_2_20171002_sub.fq.gz \
 --readFilesCommand zcat \
 --outSAMtype BAM Unsorted \
 --winAnchorMultimapNmax  200 \
 --outFilterMultimapNmax  100  \
 --outFileNamePrefix /mnt/Fullset/bam/Clean5latM

echo "M2 is done"

STAR --runThreadN 12 \
 --genomeDir /mnt/Reference/ \
 --sjdbGTFfile /mnt/Annotation/Latipes_merged.gtf \
 --sjdbOverhang  100 \
 --readFilesIn  /mnt/Fullset/Clean6latM_1_20171002_sub.fq.gz /mnt/Fullset/Clean6latM_2_20171002_sub.fq.gz \
 --readFilesCommand zcat \
 --outSAMtype BAM Unsorted \
 --winAnchorMultimapNmax  200 \
 --outFilterMultimapNmax  100  \
 --outFileNamePrefix /mnt/Fullset/bam/Clean6latM

echo "M3 is done"

