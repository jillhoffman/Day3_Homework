import random
import json

associated_gene_file = "./input_data/input.gmt.txt"

FA_subnetwork_genes = {}
num_subnetworks = 5000


def randomization(selected_genes, loci):
    genes = loci.split()[6:]
    loci_length = len(genes)
    randomization = random.randint(0, loci_length)
    loci_gene = genes[randomization]
    selected_genes.append(loci_gene)


with open(associated_gene_file, "r") as associated_genes:
    for i in range(num_subnetworks):
        selected_genes = []
        for loci in associated_genes:
            genes = loci.split()[6:]
            # print(genes)
            loci_length = len(genes)
            randomization = random.randint(0, loci_length)
            loci_gene = genes[randomization]
            # print(loci_gene)
            selected_genes.append(loci_gene)

        associated_gene_file.seek(0)

        if selected_genes not in FA_subnetwork_genes.values():
            FA_subnetwork_genes[i + 1] = selected_genes


with open('./dictionaries/FA_subnetworks.json', 'w') as js_file:
    json.dump(FA_subnetwork_genes, js_file, indent=4,
                                  separators=(',', ': '))


