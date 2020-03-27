# ID: PROT

# import pprint

sample = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

with open('../datasets/rna_codon_table.txt', 'r') as file:
    table = file.read().split()

rna_codon_table = dict(zip(table[::2], table[1::2]))

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(rna_codon_table)

with open('../datasets/rosalind_prot.txt', 'r') as file:
    data = file.read()


def translate_rna(rna_codon_table: dict, sample: str) -> str:
    length = int(len(sample) / 3)

    protein = ""

    for i in range(length):
        amino = rna_codon_table[sample[i*3:i*3+3]]

        if(amino.lower() != "stop"):
            protein = protein + amino

    return(protein)


print(translate_rna(rna_codon_table, data))
