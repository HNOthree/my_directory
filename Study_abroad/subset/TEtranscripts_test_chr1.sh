
TEtranscripts \
 --format BAM \
 -t ~/Test_data/Clean1latF_chr1Aligned.out.bam ~/Test_data/Clean2latF_chr1Aligned.out.bam ~/Test_data/Clean3latF_chr1Aligned.out.bam  \
 -c ~/Test_data/Clean4latM_chr1Aligned.out.bam ~/Test_data/Clean5latM_chr1Aligned.out.bam  ~/Test_data/Clean6latM_chr1Aligned.out.bam \
 --GTF ~/Index/Latipes_merged.gtf \
 --TE ~/Index/TE_only_Latipes_annotation_file_chr1_purified.gtf \
 --mode multi \
 --project ~/FvsM_test \
 --minread 1 -i 10 --padj 0.05
