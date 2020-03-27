# ID: HAMM

sample = """GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT"""

with open('../datasets/rosalind_hamm.txt', 'r') as file:
    data = file.read()


def hamming_distance(sample: str) -> int:
    dna_s = sample.split()[0]
    dna_t = sample.split()[1]

    d_H = 0

    for s1, s2 in zip(dna_s, dna_t):
        if s1 != s2:
            d_H += 1

    return(d_H)


print(hamming_distance(data))
