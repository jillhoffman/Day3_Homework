import json

associated_gene_file = "../input_files/input.gmt.txt"
FA_networks = "../input_files/FA_subnetworks.json"
gene_connections = open("../input_files/M3_Input.txt", 'rb')

unique_connections_set = set()
unique_connections_list = []

FA_all_genes = []
all_connections = []

FA_loci = {}
gene_scores_all = {}
gene_scores_avg = {}

def find_densities(subnetwork):
    weights = [float(line[0]) for line in unique_connections_list if line[1] in subnetwork and line[2] in subnetwork]
    if len(weights) == 0:
        avg_density = 0
    else:
        avg_density = sum(weights) / 12

    return avg_density

with open(associated_gene_file, "r") as associated_genes:
    for i, loci in enumerate(associated_genes):
        loci_num = i + 1
        genes = loci.split()[7:]
        FA_loci[loci_num] = genes
        for gene in genes:
            FA_all_genes.append(gene)

    associated_genes.seek(0)
associated_genes.close()

with open('./FA_loci.json', 'w') as js:
    json.dump(FA_loci, js, indent=4,
                                  separators=(',', ': '))

for GCL in gene_connections:
    gene_cons = GCL.split()
    sort = sorted(gene_cons)
    s = str(sort)
    a = s.replace("'", "")
    b = a.replace("[", "")
    c = b.replace("]", "")
    d = c.replace(",", "")
    e = d.replace("b", "")
    unique_connections_set.add(e)
# print(unique_connections)

for x in unique_connections_set:
    split = x.split()
    unique_connections_list.append(split)

with open(FA_networks, 'rb') as f:
    FA_subnetworks = json.load(f)
    for i, key in enumerate(FA_subnetworks.keys()):
        print(i)
        genes_done = []
        subnetwork = FA_subnetworks[key]
        unchanged_subnetwork_density = find_densities(subnetwork)

        for gene in subnetwork:
            genes_done.append(gene)
            loci_num = [k for k, v in FA_loci.items() if gene in v]
            empty_loci_subnetwork = [x for x in subnetwork if x != gene]
            empty_loci_density = find_densities(empty_loci_subnetwork)

            gene_score_default_network = unchanged_subnetwork_density - empty_loci_density
            other_genes_in_loci = FA_loci[loci_num[0]]

            if gene not in gene_scores_all.keys():
                gene_scores_all[gene] = [float(gene_score_default_network)]
            else:
                gene_scores_all[gene].append(float(gene_score_default_network))

            for other_gene in other_genes_in_loci:
                if other_gene not in genes_done:
                    genes_done.append(other_gene)

                    replaced_loci = list(map(lambda x: x.replace(gene, other_gene),subnetwork))
                    replaced_gene_density = find_densities(replaced_loci)
                    gene_score_new = replaced_gene_density - empty_loci_density

                    if other_gene not in gene_scores_all.keys():
                        gene_scores_all[other_gene] = [float(gene_score_new)]
                    else:
                        gene_scores_all[other_gene].append(float(gene_score_new))

for g_key in gene_scores_all.keys():
    all_scores = gene_scores_all[g_key]
    print(len(all_scores))
    avg_score = sum(all_scores) / len(all_scores)
    gene_scores_avg[g_key] = avg_score

with open('./gene_scores.json', 'w') as js:
    json.dump(gene_scores_avg, js, indent=4,
                                  separators=(',', ': '))
