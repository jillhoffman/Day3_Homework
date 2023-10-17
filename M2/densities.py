import json

gene_connections = open("./input_data/STRING1.txt", 'rb')
FA_networks = "./dictionaries/FA_subnetworks.json"
null_networks = "./dictionaries/null_subnetworks.json"

unique_connections_set = set()
unique_connections_list = []

null_subnetwork_densities = {}
FA_subnetwork_densities = {}

def find_densities(subnetworks, key):
    subnetwork = subnetworks[key]
    densities = [float(line[0]) for line in unique_connections_list if line[1] in subnetwork and line[2] in subnetwork]
    if len(densities) == 0:
        avg_density = 0
    else:
        avg_density = sum(densities) / 12

    return avg_density


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

with open(FA_networks) as f:
    FA_subnetworks = json.load(f)
    for key in FA_subnetworks.keys():
        avg_density = find_densities(FA_subnetworks, key)
        null_subnetwork_densities[key] = avg_density

with open(null_networks) as y:
    null_subnetworks = json.load(y)
    for key in null_subnetworks:
        avg_density = find_densities(null_subnetworks, key)
        FA_subnetwork_densities[key] = avg_density


with open('./dictionaries/FA_subnetwork_densities.json', 'w') as js_file:
    json.dump(FA_subnetwork_densities, js_file, indent=4,
                                  separators=(',', ': '))

with open('./dictionaries/null_subnetwork_densities.json', 'w') as js:
    json.dump(null_subnetwork_densities, js, indent=4,
                                  separators=(',', ': '))




