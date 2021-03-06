squire Count --map_folder /mnt/squire_map \
 --clean_folder /mnt/squire_clean \
 --count_folder /mnt/squire_count \
 --temp_folder /mnt/count_folder \
  --fetch_folder /mnt/squire_fetch \
 --name Clean1latF_Fullset \
 --build oryLat2 \
 --pthreads 8 \
 -r 100 \
 -v
echo "F1 done"

squire Count --map_folder /mnt/squire_map \
 --clean_folder /mnt/squire_clean \
 --count_folder /mnt/squire_count \
 --temp_folder /mnt/count_folder \
  --fetch_folder /mnt/squire_fetch \
 --name Clean2latF_Fullset \
 --build oryLat2 \
 --pthreads 8 \
 -r 100
echo "F2 done"

squire Count --map_folder /mnt/squire_map \
 --clean_folder /mnt/squire_clean \
 --count_folder /mnt/squire_count \
 --temp_folder /mnt/count_folder \
  --fetch_folder /mnt/squire_fetch \
 --name Clean3latF_Fullset \
 --build oryLat2 \
 --pthreads 8 \
 -r 100
echo "F3 done"

squire Count --map_folder /mnt/squire_map \
 --clean_folder /mnt/squire_clean \
 --count_folder /mnt/squire_count \
 --temp_folder /mnt/count_folder \
  --fetch_folder /mnt/squire_fetch \
 --name Clean4latM_Fullset \
 --build oryLat2 \
 --pthreads 8 \
 -r 100
echo "M1 done"

squire Count --map_folder /mnt/squire_map \
 --clean_folder /mnt/squire_clean \
 --count_folder /mnt/squire_count \
 --temp_folder /mnt/count_folder \
  --fetch_folder /mnt/squire_fetch \
 --name Clean5latM_Fullset \
 --build oryLat2 \
 --pthreads 8 \
 -r 100
echo "M2 done"

squire Count --map_folder /mnt/squire_map \
 --clean_folder /mnt/squire_clean \
 --count_folder /mnt/squire_count \
 --temp_folder /mnt/count_folder \
  --fetch_folder /mnt/squire_fetch \
 --name Clean6latM_Fullset \
 --build oryLat2 \
 --pthreads 8 \
 -r 100
echo "M3 done"

