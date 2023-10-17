import json

associated_gene_file = open("./input_data/input.gmt.txt", "r")
gene_connections = open("./input_data/STRING1.txt", "r")

all_FA = []
unique_connections_set = set()
unique_connections_list = []
all_genes = []
connection_bins = {}
gene_counts = []

for loci in associated_gene_file:
    split_file = loci.split()
    genes = split_file[7:]
    for gene in genes:
        all_FA.append(gene)

for GCL in gene_connections:
    gene_cons = GCL.split()
    sort = sorted(gene_cons)
    s = str(sort)
    a = s.replace("'","")
    b = a.replace("[","")
    c = b.replace("]","")
    d = c.replace(",", "")
    unique_connections_set.add(d)
# print(unique_connections)

for x in unique_connections_set:
    split = x.split()
    unique_connections_list.append(split)

for line in unique_connections_list:
    if line[1] not in all_genes:
        all_genes.append(line[1])
    if line[2] not in all_genes:
        all_genes.append(line[2])

    gene_counts.append(line[1])
    gene_counts.append(line[2])

for gene in all_genes:
    num_connections = gene_counts.count(gene)
    if num_connections not in connection_bins.keys():
        connection_bins[num_connections] = list(gene)
    else:
        connection_bins[num_connections].append(gene)


sorted_data = sorted(connection_bins.items(), key=lambda x: x[0])
sorted_dict = dict(sorted_data)

with open('./dictionaries/connection_bins.json', 'w') as js_file:
    json.dump(sorted_dict, js_file, separators=(',', ': '))