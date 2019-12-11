from Bio import SeqIO

for seq_record in SeqIO.parse("/home/smiyake/Index/GCF_002234675.1_ASM223467v1_genomic.fasta", "fasta"):
	print(seq_record.id)
	name=seq_record.id.split(" ")
	name=name[0]
	with open("{}.fasta".format(name),"w") as f:
		f.write(">"+str(seq_record.id) + "\n")
		f.write(str(seq_record.seq)+"\n")

