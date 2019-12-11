#The script to run TEtranscript
#-t and -c  mean treatment and control
TEtranscripts \
 --format BAM \
 -t /mnt/Fullset/bam/Clean4latFAligned.out.bam /mnt/Fullset/bam/Clean5latFAligned.out.bam /mnt/Fullset/bam/Clean6latFAligned.out.bam  \
 -c /mnt/Fullset/bam/Clean1latMAligned.out.bam /mnt/Fullset/bam/Clean2latMAligned.out.bam  /mnt/Fullset/bam/Clean3latMAligned.out.bam \
 --GTF /mnt/scp/Annotation/Latipes_merged_chr1.gtf \
 --TE ~/scp/Annotation/TE_only_Latipes_annotation_file_chr1_purified.gtf \
 --mode multi \
 --project /mnt/TEtranscripts/FvsM_ \
 --minread 1 -i 10 --padj 0.05
