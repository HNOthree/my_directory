
for i in 1 2 3 4;do
 python svg_enrich.py \
  -e /mnt/result/25k.bed \
  -i /mnt/result/TE_nearest_gene.txt \
  -o /mnt/result/svg_file/25k \
  -t $i \
  -c /mnt/squire_fetch/ourLat_STAR/chrNameLength.txt \
  -p 1
done

for i in 1 2 3 4;do
 python svg_enrich.py \
  -e /mnt/result/100k.bed \
  -i /mnt/result/TE_nearest_gene.txt \
  -o /mnt/result/svg_file/100k \
  -t $i \
  -c /mnt/result/squire_fetch/ourLat_STAR/chrNameLength.txt \
  -p 1
done
