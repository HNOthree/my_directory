import random
def generate_seq(length):
    sequence=''
    DNA=["A","T","G","C"]
    for i in range(length):
        sequence+=random.choice(DNA)
    return sequence

def search(ref,sequence):
    count=0
    for i in range(len(ref)-len(sequence)+1):
        compare_seq=ref[i:i+len(sequence)]
        if(compare_seq==sequence):
            count=1
            break
        
    return count

def probability(search_seq,genome_length):
    loop=1000
    match_count=0
    for i in range(loop):
        ref=generate_seq(genome_length)
        match_count+=search(ref,search_seq)
        #if(i%10==0):
           # print(i,"times")
    prob=match_count/loop
    return prob

def main():
    search_seq="ACGCGCGA"
    genome_length=4873567
    prob=probability(search_seq,genome_length)
    path_w = 'prob.txt'

    with open(path_w, mode='w') as f:
        f.write(str(prob))

main()