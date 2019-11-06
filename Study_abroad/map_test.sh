
squire Map -1 /mnt/Subset/Clean1latF_1_20181003_sub.fq.gz \
 -2 /mnt/Subset/Clean1latF_2_20181003_sub.fq.gz \
 -o /mnt/squire_map \
 -f /mnt/squire_fetch \
 -r 101 \
 -n Clean1latF_Subset \
 -b ourLat \
 -p 6
echo "F1 done"

squire Map -1 /mnt/Subset/Clean2latF_1_20181003_sub.fq.gz \
 -2 /mnt/Subset/Clean2latF_2_20181003_sub.fq.gz \
 -o /mnt/squire_map \
 -f /mnt/squire_fetch \
 -r 101 \
 -n Clean2latF_Subset \
 -b ourLat \
 -p 6
echo "F2 done"

squire Map -1 /mnt/Subset/Clean3latF_1_20181003_sub.fq.gz \
 -2 /mnt/Subset/Clean3latF_2_20181003_sub.fq.gz \
 -o /mnt/squire_map \
 -f /mnt/squire_fetch \
 -r 101 \
 -n Clean3latF_Subset \
 -b ourLat \
 -p 6
echo "F3 done"

squire Map -1 /mnt/Subset/Clean4latM_1_20181003_sub.fq.gz \
 -2 /mnt/Subset/Clean4latM_2_20181003_sub.fq.gz \
 -o /mnt/squire_map \
 -f /mnt/squire_fetch \
 -r 101 \
 -n Clean4latM_Subset \
 -b ourLat \
 -p 6
echo "M1 done"

squire Map -1 /mnt/Subset/Clean5latM_1_20181003_sub.fq.gz \
 -2 /mnt/Subset/Clean5latM_2_20181003_sub.fq.gz \
 -o /mnt/squire_map \
 -f /mnt/squire_fetch \
 -r 101 \
 -n Clean5latM_Subset \
 -b ourLat \
 -p 6
echo "M2 done"


squire Map -1 /mnt/Subset/Clean6latM_1_20181003_sub.fq.gz \
 -2 /mnt/Subset/Clean6latM_2_20181003_sub.fq.gz \
 -o /mnt/squire_map \
 -f /mnt/squire_fetch \
 -r 101 \
 -n Clean6latM_Subset \
 -b ourLat \
 -p 6
echo "M3 done"
