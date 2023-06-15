def DNA_strand(dna):
    listed_dna = list(dna)
    new_dna = []
    for char in listed_dna:
        if char == 'A':
            new_dna.append('T')
        elif char == 'T':
            new_dna.append('A')
        elif char == 'C':
            new_dna.append('G')
        elif char == 'G':
            new_dna.append('C')
    return "".join(new_dna)
