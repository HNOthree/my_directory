squire Fetch --build oryLat2 \
 --fetch_folder /mnt/squire_fetch \
 --fasta --rmsk  --chrom_info  --index  --gene \
 --pthreads 10

squire Clean --build oryLat2 \
 --fetch_folder /mnt/squire_fetch \
 --clean_folder /mnt/squire_clear

squire Map --read1 /mnt/subset/Clean1latF_1_20181003_sub.fq.gz \
 --read2 /mnt/subset/Clean1latF_2_20181003_sub.fq.gz \
 --map_folder /mnt/squire_map \
 --read_length 101 \
 --fetch_folder /mnt/squire_fetch \
 --pthreads 10 --build oryLat2 \
 --name Clean1latF_20181003_sub

squire Count --map_folder /mnt/squire_map \
 --clean_folder /mnt/squire_clear \
 --count_folder /mnt/squire_count \
 --temp_folder /mnt/count_folder \
 --name Clean1latF_20181003_sub \
 --build oryLat2

