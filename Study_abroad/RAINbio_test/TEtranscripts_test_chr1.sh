
TEtranscripts \
 --format BAM \
 -t ~/subset/bam/Clean1latF_chr1Aligned.out.bam ~/subset/bam/Clean2latF_chr1Aligned.out.bam ~/subset/bam/Clean3latF_chr1Aligned.out.bam  \
 -c ~/subset/bam/Clean4latM_chr1Aligned.out.bam ~/subset/bam/Clean5latM_chr1Aligned.out.bam  ~/subset/bam/Clean6latM_chr1Aligned.out.bam \
 --GTF ~/scp/Annotation/Latipes_merged_chr1.gtf \
 --TE ~/scp/Annotation/TE_only_Latipes_annotation_file_chr1_purified.gtf \
 --mode multi \
 --project ~/FvsM_test \
 --minread 1 -i 10 --padj 0.05
