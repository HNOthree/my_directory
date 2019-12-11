#In order to run STAR with pair end reads

STAR --runThreadN 6 \
 --genomeDir ~/Index/ \
 --sjdbGTFfile ~/Index/Latipes_merged_chr1.gtf \
 --sjdbOverhang  100 \
 --readFilesIn  ~/Test_data/Clean1latF_1_20181003_sub.fq.gz ~/Test_data/Clean1latF_2_20181003_sub.fq.gz \
 --readFilesCommand zcat \
 --outSAMtype BAM Unsorted \
 --winAnchorMultimapNmax  200 \
 --outFilterMultimapNmax  100  \
 --outFileNamePrefix ~/Test_data/Clean1latF_chr1

echo "F1 is done"

STAR --runThreadN 6 \
 --genomeDir ~/Index/ \
 --sjdbGTFfile ~/Index/Latipes_merged_chr1.gtf \
 --sjdbOverhang  100 \
 --readFilesIn  ~/Test_data/Clean2latF_1_20181003_sub.fq.gz ~/Test_data/Clean2latF_2_20181003_sub.fq.gz \
 --readFilesCommand zcat \
 --outSAMtype BAM Unsorted \
 --winAnchorMultimapNmax  200 \
 --outFilterMultimapNmax  100  \
 --outFileNamePrefix ~/Test_data/Clean2latF_chr1

echo "F2 is done"

STAR --runThreadN 6 \
 --genomeDir ~/Index/ \
 --sjdbGTFfile ~/Index/Latipes_merged_chr1.gtf \
 --sjdbOverhang  100 \
 --readFilesIn  ~/Test_data/Clean3latF_1_20181003_sub.fq.gz ~/Test_data/Clean3latF_2_20181003_sub.fq.gz \
 --readFilesCommand zcat \
 --outSAMtype BAM Unsorted \
 --winAnchorMultimapNmax  200 \
 --outFilterMultimapNmax  100  \
 --outFileNamePrefix ~/Test_data/Clean3latF_chr1

echo "F3 is done"

STAR --runThreadN 6 \
 --genomeDir ~/Index/ \
 --sjdbGTFfile ~/Index/Latipes_merged_chr1.gtf \
 --sjdbOverhang  100 \
 --readFilesIn  ~/Test_data/Clean4latM_1_20181003_sub.fq.gz ~/Test_data/Clean4latM_2_20181003_sub.fq.gz \
 --readFilesCommand zcat \
 --outSAMtype BAM Unsorted \
 --winAnchorMultimapNmax  200 \
 --outFilterMultimapNmax  100  \
 --outFileNamePrefix ~/Test_data/Clean4latM_chr1

echo "M1 is done"

STAR --runThreadN 6 \
 --genomeDir ~/Index/ \
 --sjdbGTFfile ~/Index/Latipes_merged_chr1.gtf \
 --sjdbOverhang  100 \
 --readFilesIn  ~/Test_data/Clean5latM_1_20181003_sub.fq.gz ~/Test_data/Clean5latM_2_20181003_sub.fq.gz \
 --readFilesCommand zcat \
 --outSAMtype BAM Unsorted \
 --winAnchorMultimapNmax  200 \
 --outFilterMultimapNmax  100  \
 --outFileNamePrefix ~/Test_data/Clean5latM_chr1
                                       
echo "M2 is done"

STAR --runThreadN 6 \
 --genomeDir ~/Index/ \
 --sjdbGTFfile ~/Index/Latipes_merged_chr1.gtf \
 --sjdbOverhang  100 \
 --readFilesIn  ~/Test_data/Clean6latM_1_20181003_sub.fq.gz ~/Test_data/Clean6latM_2_20181003_sub.fq.gz \
 --readFilesCommand zcat \
 --outSAMtype BAM Unsorted \
 --winAnchorMultimapNmax  200 \
 --outFilterMultimapNmax  100  \
 --outFileNamePrefix ~/Test_data/Clean6latM_chr1
       
