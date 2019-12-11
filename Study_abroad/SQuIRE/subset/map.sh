
squire Map -1 /mnt/subset/Clean1latF_1_20181003_sub.fq.gz \
 -2 /mnt/subset/Clean1latF_2_20181003_sub.fq.gz \
 -o /mnt/squire_map \
 -f /mnt/squire_fetch \
 -r 101 \
 -n Clean1latF_20181003_sub \
 -b oryLat2 \
 -p 6
echo "F1 done"

squire Map -1 /mnt/subset/Clean2latF_1_20181003_sub.fq.gz \
 -2 /mnt/subset/Clean2latF_2_20181003_sub.fq.gz \
 -o /mnt/squire_map \
 -f /mnt/squire_fetch \
 -r 101 \
 -n Clean2latF_20181003_sub \
 -b oryLat2 \
 -p 6
echo "F2 done"

squire Map -1 /mnt/subset/Clean3latF_1_20181003_sub.fq.gz \
 -2 /mnt/subset/Clean3latF_2_20181003_sub.fq.gz \
 -o /mnt/squire_map \
 -f /mnt/squire_fetch \
 -r 101 \
 -n Clean3latF_20181003_sub \
 -b oryLat2 \
 -p 6
echo "F3 done"

squire Map -1 /mnt/subset/Clean4latM_1_20181003_sub.fq.gz \
 -2 /mnt/subset/Clean4latM_2_20181003_sub.fq.gz \
 -o /mnt/squire_map \
 -f /mnt/squire_fetch \
 -r 101 \
 -n Clean4latM_20181003_sub \
 -b oryLat2 \
 -p 6
echo "M1 done"

squire Map -1 /mnt/subset/Clean5latM_1_20181003_sub.fq.gz \
 -2 /mnt/subset/Clean5latM_2_20181003_sub.fq.gz \
 -o /mnt/squire_map \
 -f /mnt/squire_fetch \
 -r 101 \
 -n Clean5latM_20181003_sub \
 -b oryLat2 \
 -p 6
echo "M2 done"


squire Map -1 /mnt/subset/Clean6latM_1_20181003_sub.fq.gz \
 -2 /mnt/subset/Clean6latM_2_20181003_sub.fq.gz \
 -o /mnt/squire_map \
 -f /mnt/squire_fetch \
 -r 101 \
 -n Clean6latM_20181003_sub \
 -b oryLat2 \
 -p 6
echo "M3 done"
