def proteins(strand):
    protein = []
    
    for i in range(0,len(strand),3):
        codon = strand[i]+strand[i+1]+strand[i+2]
        if codon == 'AUG':
            protein.append('Methionine')
        elif codon == 'UUU' or codon == 'UUC':
            protein.append('Phenylalanine')
        elif codon == 'UUA' or codon == 'UUG':
            protein.append('Leucine')
        elif codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG':
            protein.append('Serine')
        elif codon == 'UAU' or codon == 'UAC':
            protein.append('Tyrosine')
        elif codon == 'UGU' or codon == 'UGC':
            protein.append('Cysteine')
        elif codon == 'UGG':
            protein.append('Tryptophan')
        else:
            break

    return protein
