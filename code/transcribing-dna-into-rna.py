sample = "GATGGAACTTGACTACGTAAATT"

with open('../datasets/rosalind_rna.txt', 'r') as file:
    data = file.read()


def dna_to_rna(sample: str) -> str:
    rna = sample.replace("T", "U")

    return(rna)


print(dna_to_rna(data))
