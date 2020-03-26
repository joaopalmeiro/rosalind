sample = "AAAACCCGGT"

with open('../datasets/rosalind_revc.txt', 'r') as file:
    data = file.read()


def reverse_complement(sample: str) -> str:
    reverse = sample[::-1]

    mapping = str.maketrans("ACGT", "TGCA")

    complement = reverse.translate(mapping)

    return(complement)


print(reverse_complement(data))
