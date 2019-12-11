import pandas as pd
upstream=pd.read_csv("/mnt/Results/merge_transcript_TE_upstream_overlap_lfc.txt",sep='\t')
downstream=pd.read_csv("/mnt/Results/merge_transcript_TE_downstream_overlap_lfc.txt",sep='\t')

upstream_plus=upstream[upstream.Strand=="+"]
upstream_minus=upstream[upstream.Strand=="-"]
downstream_plus=upstream[upstream.Strand=="+"]
downstream_minus=upstream[upstream.Strand=="-"]

upstream_merge=upstream_plus.append(downstream_minus)
downstream_merge=upstream_minus.append(downstream_plus)

upstream_merge.to_csv("/mnt/upstream_transcripts_TE_overlap_lfc.txt",sep='\t',index=False)
downstream_merge.to_csv("/mnt/downstream_transcripts_TE_overlap_lfc.txt",sep='\t',index=False)

