import json

FA_networks = open("./outputs/optimized_network.json", 'rb')
FA_subnetworks = json.load(FA_networks)

null_networks = open("./inputs/optimized_null_networks.json", 'rb')
connection_bins = json.load(null_networks)

nd = open("./inputs/optimized_null_densities.json")
null_densities = json.load(nd)

od = open("./inputs/optimized_densities.json", 'rb')
optimized_densities = json.load(od)

gene_connections = open("./inputs/M3_Input.txt", 'rb')

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

top_10_densities = {}
sorted_densities = dict(sorted(optimized_densities.items(), key=lambda item: item[1]))
top_10_densities_key = list(sorted_densities)[-10:]

permutation_densities = list(null_densities.values())


for net in top_10_densities_key:
    top_10_densities[net] = optimized_densities[net]


for i, nk in enumerate(top_10_densities):
    nd = top_10_densities[nk]
    pvalue_values = [x for x in permutation_densities if x >= nd]
    p_value = len(pvalue_values) / len(permutation_densities)

    print(nk, p_value)

    subnetwork = list(FA_subnetworks[nk])

    connections = [line for line in unique_connections_list if line[1] in subnetwork and line[2] in subnetwork]

    with open(f"./Network{10 - i}_pval{p_value}.txt", 'w') as fp:
        for conn in connections:
            sc = str(conn)
            r1 = sc.replace("'", "")
            r2 = r1.replace(",", "")
            r3 = r2.replace("]", "")
            r4 = r3.replace("[", "")

            fp.write(f"{r4[1]}\t{r4[2]}\t{r4[0]}\n")

    fp.close()
