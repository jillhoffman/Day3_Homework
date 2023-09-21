associated_gene_file = open("./input.gmt.txt", "r")
gene_connections = open("./STRING1.txt", "r")

FA_connection = []
final_connections = []

FA_all_genes = []
all_connections = []

for loci in associated_gene_file:
    split_file = loci.split()
    genes = split_file[7:]
    for gene in genes:
        FA_all_genes.append(gene)

for GCL in gene_connections:
    gene_cons = GCL.split()
    all_connections.append(gene_cons)

def dup_check(conn, final_connections):
    dup_check_l = [item for item in final_connections if item[0] == conn[0] and item[1] == conn[1] or item[0] == conn[1] and item[1 == conn[0]]]
    if len(dup_check_l) == 0:
        final_connections.append(conn)

def direct_connections(all_connections, FA_gene, FA_all_genes, final_connections):
    direct_FA_gene_connections = [item for item in all_connections if str(item[0]) == str(FA_gene) and item[1] in FA_all_genes]
    if len(direct_FA_gene_connections) == 0:
        print(f"{FA_gene} has no direct connections, checking indirect connections...")
        FA_gene_connections = [item for item in all_connections if str(item[0]) == str(FA_gene)]
        if len(FA_gene_connections) > 0:
            indirect_connections(FA_gene_connections, all_connections, FA_all_genes, final_connections)

    else:
        print(f"{FA_gene} has direct connections")
        for conn in direct_FA_gene_connections:
            dup_check(conn, final_connections)


def indirect_connections(FA_gene_connections, all_connections, FA_all_genes, final_connections):
    indirect_genes = [item[1] for item in FA_gene_connections]
    for indir in indirect_genes:
        indirect_gene_connections = [item for item in all_connections if str(item[0]) == str(indir) and str(item[1]) in FA_all_genes]
        if len(indirect_gene_connections) > 1:
            print(f"{FA_gene} has indirect connection")
            for conn in indirect_gene_connections:
                dup_check(conn, final_connections)

for FA_gene in FA_all_genes:
    direct_connections(all_connections, FA_gene, FA_all_genes, final_connections)


print(final_connections)
print(len(final_connections))

with open("./newInput.txt", 'w') as fp:
    for connection in final_connections:
        sc = str(connection)
        r1 = sc.replace("'", "")
        r2 = r1.replace(",", "")
        r3 = r2.replace("]", "")
        r4 = r3.replace("[", "")
        fp.write(f"{r4}\n")

fp.close()







