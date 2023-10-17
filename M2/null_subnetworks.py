import json
import random

null_subnetworks = {}
FA_networks = "./dictionaries/FA_subnetworks.json"
bins = "./dictionaries/connection_bins.json"

def randomization(bin, tmp_list):
    bin_length = len(connection_bins[bin])
    random_gene_selection = random.randint(0, bin_length - 1)
    random_gene = connection_bins[bin][random_gene_selection]
    tmp_list.append(random_gene)

with open(FA_networks, 'rb') as f:
    FA_subnetworks = json.load(f)
    with open(bins, 'rb') as x:
        connection_bins = json.load(x)
        for key in FA_subnetworks.keys():
            tmp_list = []
            og_subnetwork = FA_subnetworks[key]
            for gene in og_subnetwork:
                bin_return = [i for i in connection_bins if gene in connection_bins[i]]
                if len(bin_return) != 0:
                    bin = bin_return[0]
                    randomization(bin, tmp_list)

                elif len(bin_return) == 0:
                    bin = "1"
                    randomization(bin, tmp_list)

            null_subnetworks[key] = tmp_list


with open('./dictionaries/null_subnetworks.json', 'w') as js_file:
    json.dump(null_subnetworks, js_file, indent=4,
              separators=(',', ': '))