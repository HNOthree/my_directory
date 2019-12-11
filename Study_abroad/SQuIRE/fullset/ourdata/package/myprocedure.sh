output_directory="/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis"
DESeq_from_SQUIRE="/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/squire_call/DESeq2_TE_only.txt"
gene_exp_data="/home/smiyake/shares/Sho/Latipes_Expression_table.csv"
TE_annotationdata="/home/smiyake/shares/Sho/Results/SQuIRE/SQUIRE_data/squire_fetch/TE_only_Latipes_annotation_file_modified_unknown.txt"
Enrichment_data="/home/smiyake/shares/Sho/Bedfiles/25k.bed"
gtf_file_of_gene="/home/smiyake/shares/Sho/data/Annotation/Latipes_merged.gtf"
Chromosome_lengthdata="/home/smiyake/shares/Sho/Results/SQuIRE/SQUIRE_data/squire_fetch/ourLat_STAR/chrNameLength.txt" # It is from STAR index

echo "make transcript data start"
echo `date`
#python make_transcript_txt.py \
#	-g $gtf_file_of_gene \
#	-d $output_directory
echo "make transcript data end"
echo `date`

echo "############################################"
echo "make gene data start"
echo `date`
#python gene_length.py \
#        -d $output_directory
echo "make gene data end"
echo `date`

echo "############################################"
echo "DESeq_purify.py start"
echo `date`
#python DESeq_purify.py \
#	-i $DESeq_from_SQUIRE \
#	-o $output_directory
echo "DESeq_purify.py end"
echo `date`

echo "make a volcano plot and histgram"
#Rscript volcanoplot.R \
# $output_directory

#Rscript TE_lfc_distribution.R \
# $output_directory
echo "############################################"
echo "gene_TE_number start"
echo `date`
#python gene_TE_number_connect.py \
#	-d $output_directory \
#	-e $gene_exp_data
echo "gene_TE_number end"
echo `date`

echo "##############################################"
echo "gene_TE_distance start"
#python gene_TE_distance_connect.py \
#	-d $output_directory \
 #       -e $gene_exp_data

echo "gene_TE_number end"
echo `date`

echo "##############################################"
echo "nearest_gene start"
echo `date`
python nearest_gene.py \
	-i $output_directory
echo "nearest_gene end"
echo `date`

echo "##############################################"
echo "svg start"
echo `date`
directory="${output_directory}/svg_file"
echo $directory
mkdir $directory
mkdir $directory/png
for i in 1 2 3 4;do
# python svg_enrich.py \
#  -e $Enrichment_data \
#  -i $output_directory"/TE_nearest_gene.txt" \
#  -o $output_directory \
#  -t $i \
#  -c $Chromosome_lengthdata \
#  -p 1
done
#mv $output_directory/*.svg $output_directory/svg_file/
#mv $output_directory/*.png $output_directory/svg_file/png

echo "svg end"
echo `date`

echo "##############################################"
echo "enrich region start"
echo `date`
#python enrich_region_TE.py \
#	-t $TE_annotationdata \
#	-e $Enrichment_data\
#	-o $output_directory
#echo "enrich region end"
echo `date`

echo "make a violin plot and histgran of lfc"
#Rscript violinplot.R \
# $output_directory

echo "##############################################"
echo "devide_chrom start"
echo `date`
#python devide_chrom.py \
#	-e $Enrichment_data \
#	-i $output_directory 
echo "devide_chrom end"
echo `date`

echo "##############################################"
echo "high low start"
echo `date`
#python high_low.py \
#	-d $output_directory \
#	-e $Enrichment_data 
echo "high low end"
echo `date`

echo "calculate correlation coefficiency grouped by superfamily"
#python calculate_cc.py \
# -d $output_directory
 
echo "make box plot of correlation coefficiency"
Rscript boxplot_correlation.R \
 $output_directory
echo "##############################################"
echo "TE_enrich percentage start"
echo `date`
python TE_enrich_percentage.py \
	-d $output_directory 
echo "TE_enrich percentage end"
echo `date`

echo 'make a trigram'
Rscript triagram.R \
 $output_directory

echo "make a volcanoplot of enrichment region"
Rscript enrichment.R \
 $output_directory
