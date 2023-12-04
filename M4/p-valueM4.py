import json
import random

FA_networks = open("./outputs/optimized_network.json", 'rb')
FA_subnetworks = json.load(FA_networks)

bins = open("./inputs/connection_bins.json", 'rb')
connection_bins = json.load(bins)

gene_connections = open("./inputs/STRING1.txt", 'rb')

od = open("./inputs/optimized_densities.json", 'rb')
optimized_densities = json.load(od)


def randomization(bin, tmp_list):
    bin_length = len(connection_bins[bin])
    random_gene_selection = random.randint(0, bin_length - 1)
    random_gene = connection_bins[bin][random_gene_selection]
    tmp_list.append(random_gene)

def find_avg_densities(unique_connections_list, subnetwork):
    weights = [float(line[0]) for line in unique_connections_list if line[1] in subnetwork and line[2] in subnetwork]
    if len(weights) == 0:
        avg_density = 0
    else:
        avg_density = sum(weights) / 12
    return avg_density

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


optimized_density = sum(optimized_densities.values()) / len(optimized_densities)

permutations_densities = []
## STARTED AROUND 7PM
for i in range(100):
    print(i)
    case_densities = []
    for key in FA_subnetworks.keys():
        permuted_genes_list = []
        og_subnetwork = FA_subnetworks[key]
        for gene in og_subnetwork:
            bin_return = [i for i in connection_bins if gene in connection_bins[i]]
            if len(bin_return) != 0:
                bin = bin_return[0]
                randomization(bin, permuted_genes_list)

            elif len(bin_return) == 0:
                bin = "1"
                randomization(bin, permuted_genes_list)

        ad = find_avg_densities(unique_connections_list, permuted_genes_list)
        case_densities.append(ad)

    permutation_density = sum(case_densities) / len(case_densities)
    permutations_densities.append(permutation_density)


pvalue_values = [x for x in permutations_densities if x >= optimized_density]
p_value = len(pvalue_values) / len(permutations_densities)

with open('./outputs/opt_p.txt', 'w') as fp:
    fp.write(f"{p_value}")

print(p_value)

