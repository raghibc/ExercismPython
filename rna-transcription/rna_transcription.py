def to_rna(dna_strand):
    rna = ''
    D = {'G':'C','C':'G','T':'A','A':'U'}

    for i in dna_strand:
        rna += D.get(i)
        
    return rna
