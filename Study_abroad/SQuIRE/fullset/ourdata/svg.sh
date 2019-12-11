for i in 1 2 3 4;do
 python svg_enrich.py \
  -e /home/smiyake/shares/Sho/Bedfiles/25k.bed \
  -i /home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis/TE_nearest_gene.txt \
  -o /home/smiyake/sho/Fullset/SQuIRE/image \
  -t $i \
  -c /home/smiyake/shares/Sho/Annotation/oryLat2_STAR/chrNameLength.txt \
  -p 1
done

#for i in 1 2 3 4;do
# python svg_enrich.py \
#  -e /home/smiyake/shares/Sho/Bedfiles/100k.bed \
#  -i /home/smiyake/sho/Fullset/SQuIRE/txt/TE_nearest_gene.txt \
#  -o /home/smiyake/sho/Fullset/SQuIRE/image/nearby_tendency/TE_enrich/100k \
#  -t $i \
#  -c /home/smiyake/shares/Sho/Annotation/oryLat2_STAR/chrNameLength.txt \
#  -p 1
#done
