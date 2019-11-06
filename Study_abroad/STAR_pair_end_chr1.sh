#In order to run STAR with pair end reads

STAR --runThreadN 12 \
 --genomeDir ~/scp/Annotation/ \
 --sjdbGTFfile ~/scp/Annotation/Latipes_merged_chr1.gtf \
 --sjdbOverhang  100 \
 --readFilesIn  ~/scp/Subset/Clean1latF_1_20181003_sub.fq.gz ~/scp/Subset/Clean1latF_2_20181003_sub.fq.gz \
 --readFilesCommand zcat \
 --outSAMtype BAM Unsorted \
 --winAnchorMultimapNmax  200 \
 --outFilterMultimapNmax  100  \
 --outFileNamePrefix ~/subset/bam/Clean1latF_chr1

echo "F1 is done"

STAR --runThreadN 12 \
  --genomeDir ~/scp/Annotation/ \
  --sjdbGTFfile ~/scp/Annotation/Latipes_merged_chr1.gtf \
 --sjdbOverhang  100 \
 --readFilesIn  ~/scp/Subset/Clean2latF_1_20181003_sub.fq.gz ~/scp/Subset/Clean2latF_2_20181003_sub.fq.gz \
 --readFilesCommand zcat \
 --outSAMtype BAM Unsorted \
 --winAnchorMultimapNmax  200 \
 --outFilterMultimapNmax  100  \
 --outFileNamePrefix ~/subset/bam/Clean2latF_chr1

echo "F2 is done" 

STAR --runThreadN 12 \
 --genomeDir ~/scp/Annotation/ \
 --sjdbGTFfile ~/scp/Annotation/Latipes_merged_chr1.gtf \
 --sjdbOverhang  100 \
 --readFilesIn  ~/scp/Subset/Clean3latF_1_20181003_sub.fq.gz ~/scp/Subset/Clean3latF_2_20181003_sub.fq.gz \
 --readFilesCommand zcat \
 --outSAMtype BAM Unsorted \
 --winAnchorMultimapNmax  200 \
 --outFilterMultimapNmax  100  \
 --outFileNamePrefix ~/subset/bam/Clean3latF_chr1

echo "F3 is done"

STAR --runThreadN 12 \
 --genomeDir ~/scp/Annotation/ \
 --sjdbGTFfile ~/scp/Annotation/Latipes_merged_chr1.gtf \
 --sjdbOverhang  100 \
 --readFilesIn  ~/scp/Subset/Clean4latM_1_20181003_sub.fq.gz ~/scp/Subset/Clean4latM_2_20181003_sub.fq.gz \
 --readFilesCommand zcat \
 --outSAMtype BAM Unsorted \
 --winAnchorMultimapNmax  200 \
 --outFilterMultimapNmax  100  \
 --outFileNamePrefix ~/subset/bam/Clean4latM_chr1

echo "M1 is done" 


STAR --runThreadN 12 \
 --genomeDir ~/scp/Annotation/ \
 --sjdbGTFfile ~/scp/Annotation/Latipes_merged_chr1.gtf \
 --sjdbOverhang  100 \
 --readFilesIn  ~/scp/Subset/Clean5latM_1_20181003_sub.fq.gz ~/scp/Subset/Clean5latM_2_20181003_sub.fq.gz \
 --readFilesCommand zcat \
 --outSAMtype BAM Unsorted \
 --winAnchorMultimapNmax  200 \
 --outFilterMultimapNmax  100  \
 --outFileNamePrefix ~/subset/bam/Clean5latM_chr1

echo "M2 is done"

STAR --runThreadN 12 \
 --genomeDir ~/scp/Annotation/ \
 --sjdbGTFfile ~/scp/Annotation/Latipes_merged_chr1.gtf \
 --sjdbOverhang  100 \
 --readFilesIn  ~/scp/Subset/Clean6latM_1_20181003_sub.fq.gz ~/scp/Subset/Clean6latM_2_20181003_sub.fq.gz \
 --readFilesCommand zcat \
 --outSAMtype BAM Unsorted \
 --winAnchorMultimapNmax  200 \
 --outFilterMultimapNmax  100  \
 --outFileNamePrefix ~/subset/bam/Clean6latM_chr1

echo "M3 is done"
