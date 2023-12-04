import json

FA_networks = open("./outputs/optimized_network.json", 'rb')
FA_subnetworks = json.load(FA_networks)

gs = open("./inputs/gene_scores_new.json", 'rb')
gene_scores = json.load(gs)

for key, network in FA_subnetworks.items():
    first_thing = f"GeneSet{key}"
    all_pairs = []

    for gene in network:
        score = gene_scores[gene]
        if score == "NA":
            pair = [gene, -1]
            all_pairs.append(pair)
        else:
            pair = [gene, score]
            all_pairs.append(pair)

    sorted_pairs = sorted(all_pairs, reverse = True, key = lambda x: x[1])

    file = open("./outputs/with_scores.gmt", "a")
    if key == "0":
        file.write(f"{first_thing}")
    else:
        file.write(f"\n{first_thing}")

    for pair in sorted_pairs:
        p1 = pair[0]
        if pair[1] == -1:
            p2 = "NA"
        else:
            p2 = str(pair[1])

        p3 = [p1, p2]
        j = " ".join(p3)
        file.write(f"\t{j}\t")
    file.close()


    file1 = open("./outputs/without_scores.gmt", "a")
    if key == "0":
        file1.write(f"{first_thing}")
    else:
        file1.write(f"\n{first_thing}")

    for pair in sorted_pairs:
        file1.write(f"\t{pair[0]}\t")
    file1.close()
