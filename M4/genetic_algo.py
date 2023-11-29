import random
import json

associated_gene_file = "./inputs/input.gmt.txt"
FA_networks = "./inputs/FA_subnetworks.json"
gene_connections = open("./inputs/M3_Input.txt", 'rb')
FA_loci_dict = open("./inputs/FA_loci.json", 'rb')

FA_loci = json.load(FA_loci_dict)

def random_exclude(other_genes_in_loci, gene_index):
    randInt = random.randint(0, len(other_genes_in_loci) - 1)
    return random_exclude(other_genes_in_loci, gene_index) if randInt == gene_index else randInt

def swap_genes(gene, FA_loci):
    loci_num = [k for k, v in FA_loci.items() if gene in v]
    other_genes_in_loci = FA_loci[loci_num[0]]
    gene_index = other_genes_in_loci.index(gene)
    random_gene_selection = random_exclude(other_genes_in_loci, gene_index)
    random_gene = other_genes_in_loci[random_gene_selection]
    return random_gene

def find_avg_densities(unique_connections_list, subnetwork):
    weights = [float(line[0]) for line in unique_connections_list if line[1] in subnetwork and line[2] in subnetwork]
    if len(weights) == 0:
        avg_density = 0
    else:
        avg_density = sum(weights) / 12
    return avg_density


def mate(densities, FA_loci, mutated_subnetworks, mated_subnetwork):
    population = list(densities.keys())
    weights = list(densities.values())
    p1_index, p2_index = random.choices(population, weights, k=2)

    p1_network = mutated_subnetworks[str(p1_index)]
    p2_network = mutated_subnetworks[str(p2_index)]

    for gene_1, gene_2 in zip(p1_network, p2_network):
        gene_pairs = []
        loci_num_1 = [k for k, v in FA_loci.items() if gene_1 in v]
        loci_num_2 = [k for k, v in FA_loci.items() if gene_1 in v]

        if loci_num_2 == loci_num_1:
            gene_pairs.append(gene_1)
            gene_pairs.append(gene_2)

        picked_gene = random.choice(gene_pairs)
        mated_subnetwork.append(picked_gene)



unique_connections_set = set()
unique_connections_list = []

for GCL in gene_connections:
    gene_cons = GCL.split()
    sort = sorted(gene_cons)
    s = str(sort)
    a = s.replace("'","")
    b = a.replace("[","")
    c = b.replace("]","")
    d = c.replace(",", "")
    e = d.replace("b", "")
    unique_connections_set.add(e)

for x in unique_connections_set:
    split = x.split()
    unique_connections_list.append(split)

max_rounds = 1000
stats_file = open("generational_stats.txt", "a")

f = open(FA_networks, 'rb')
FA_subnetworks = json.load(f)


for i in range(1000):
    pre_mutation_densities = {}
    mutated_subnetworks = {}
    mated_generation_densities = {}
    mutated_densities = {}
    mated_subnetworks = {}

    for FA_key, subnetwork in FA_subnetworks.items():
        d_FA = find_avg_densities(unique_connections_list, subnetwork)
        pre_mutation_densities[str(FA_key)] = d_FA
        mutations = []
        for gene in subnetwork:
            if random.randint(0, 100) <= 5:
                swapped_gene = swap_genes(str(gene), FA_loci)
                mutations.append(swapped_gene)
                #print(gene, swapped_gene)
            else:
                mutations.append(gene)

        mutated_subnetworks[str(FA_key)] = mutations


    for m_key, mut_subnetwork in mutated_subnetworks.items():
        mut_d = find_avg_densities(unique_connections_list, mut_subnetwork)
        mutated_densities[str(m_key)] = mut_d

    for x in range(5000):
        mated_subnetwork = []
        mated_network = mate(pre_mutation_densities, FA_loci, mutated_subnetworks, mated_subnetwork)

        mated_subnetworks[x] = mated_subnetwork


    for mate_key, mated_subnetwork in mated_subnetworks.items():
        mated_density = find_avg_densities(unique_connections_list, mated_subnetwork)
        mated_generation_densities[mate_key] = mated_density

    pmd = sum(pre_mutation_densities.values()) / 5000
    md = sum(mated_generation_densities.values()) / 5000
    print(md, pmd)
    density_increase = md - pmd
    percent_increase = density_increase / pmd

    if percent_increase < 0.5:

        output = f"FINISHED ON GENERATION {i+1} WITH INCREASE OF {percent_increase}%"
        print(output)

        stats_file.write(f"{output}\n")

        with open('./optimized_network.json', 'w') as js:
            json.dump(mated_subnetworks, js, indent=4,
                      separators=(',', ': '))
        break

    else:

        output = f"generation {i+1} had increase of {percent_increase}%"
        print(output)
        stats_file.write(f"{output}\n")

        FA_subnetworks = mated_subnetworks

stats_file.close()











