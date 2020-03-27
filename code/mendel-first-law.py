# ID: IPRB

sample = "2 2 2"

with open('../datasets/rosalind_iprb.txt', 'r') as file:
    data = file.read()


def prob_dominant_allele(sample: str) -> float:
    k = int(sample.split()[0])
    m = int(sample.split()[1])
    n = int(sample.split()[2])

    population = k + m + n

    hetero_hetero = m/population * (m-1)/(population-1) * 1/4
    hetero_rec = m/population * n/(population-1) * 1/2

    rec_hetero = n/population * m/(population-1) * 1/2
    rec_rec = n/population * (n-1)/(population-1)

    prob = 1 - (hetero_hetero + hetero_rec + rec_hetero + rec_rec)

    return(prob)


print(prob_dominant_allele(data))
