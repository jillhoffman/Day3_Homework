#input.gmt.txt = genes associated to FA
#string1.txt = all possible connections for all pairs of genes

### more lamen terms instead of code language
### add checks that make sure both coneced genes are in first file

#PARSE OUT GENES FROM ASSOCIATED LIST
# with open(input.gmt.txt, 'wr+') as r:
#     for line in r:
#         split(line):
#             for gene:
#                 FA_gene_list.append(gene)
#
#FIND ASSOCIATED GENES IN MASTER LIST
# for gene in FA_gene_list:
#     if gene is in string1.txt:
#WRITE ASSOCIATE GENES IN NEW FILE
#         write line from string1.txt -> string2.txt


associated_gene_file = open("./input.gmt.txt", "r")
gene_connections = open("./STRING1.txt", "r")

FA_connection = []
final_connections = []

FA_all_genes = []
all_connections = []

# def FA_connection_search():


for loci in associated_gene_file:
    split_file = loci.split()
    genes = split_file[7:]
    for gene in genes:
        FA_all_genes.append(gene)

for GCL in gene_connections:
    gene_cons = GCL.split()
    all_connections.append(gene_cons)

def direct_connections(all_connections, FA_gene, FA_all_genes):
    direct_FA_gene_connections = [item for item in all_connections if str(item[0]) == str(FA_gene) and item[1] in FA_all_genes]
    if len(direct_FA_gene_connections) == 0:
        print(f"{FA_gene} has no direct connections, checking indirect connections...")
        FA_gene_connections = [item for item in all_connections if str(item[0]) == str(FA_gene)]
        if len(FA_gene_connections) > 0:
            indirect_connections(FA_gene_connections, all_connections, FA_all_genes)

    else:
        print(f"{FA_gene} has direct connections")
        for conn in direct_FA_gene_connections:
            final_connections.append(conn)

def indirect_connections(FA_gene_connections, all_connections, FA_all_genes):
    indirect_genes = [item[1] for item in FA_gene_connections]
    for indir in indirect_genes:
        indirect_gene_connections = [item for item in all_connections if str(item[0]) == str(indir) and str(item[1]) in FA_all_genes]
        if len(indirect_gene_connections) > 1:
            print(f"{FA_gene} has indirect connection")
            for con in indirect_gene_connections:
                final_connections.append(con)

for FA_gene in FA_all_genes:
    direct_connections(all_connections, FA_gene, FA_all_genes)


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








