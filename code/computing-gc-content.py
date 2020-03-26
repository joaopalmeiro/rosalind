sample = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""

with open('../datasets/rosalind_gc.txt', 'r') as file:
    data = file.read()


def highest_gc_content(sample: str) -> str:
    dna_strings = sample.split(">")[1:]

    fasta_id = ""
    gc_content = 0.0

    for dna in dna_strings:
        current_fasta_id = dna.split("\n", 1)[0]
        current_dna_string = dna.split("\n", 1)[1].replace("\n", "")

        current_gc_content = ((current_dna_string.count(
            "G") + current_dna_string.count("C")) / len(current_dna_string)) * 100

        if(current_gc_content > gc_content):
            fasta_id = current_fasta_id
            gc_content = current_gc_content

    return(f"{fasta_id}\n{gc_content}")


print(highest_gc_content(data))
