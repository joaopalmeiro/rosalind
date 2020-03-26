sample = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

with open('../datasets/rosalind_dna.txt', 'r') as file:
    data = file.read()


def count_nucleotides(sample: str) -> str:
    nucleotides = {
        "A": sample.count("A"),
        "C": sample.count("C"),
        "G": sample.count("G"),
        "T": sample.count("T")
    }

    count = f'{nucleotides["A"]} {nucleotides["C"]} {nucleotides["G"]} {nucleotides["T"]}'

    return(count)


print(count_nucleotides(data))
