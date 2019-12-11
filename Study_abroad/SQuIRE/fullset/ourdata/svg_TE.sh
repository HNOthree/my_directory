for i in 1 2 3 4;do
 python TE_svg.py \
  -e /home/smiyake/shares/Sho/Bedfiles/25k.bed \
  -i /home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis/DESeq2_TE_separated.txt \
  -o /home/smiyake/sho/Fullset/SQuIRE/image \
  -t $i \
  -c /home/smiyake/shares/Sho/Annotation/oryLat2_STAR/chrNameLength.txt \
  -p 1
done
