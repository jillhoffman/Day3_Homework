import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import networkx as nx
from netgraph import Graph
import json
import pandas as pd

conns_input = open("./input_files/M3_Input.txt", 'r')
loci_dict = "./input_files/FA_loci.json"
gene_scores_file = "./output_file/gene_scores.json"


partition_sizes = []
from_genes = []
to_genes = []
adjusted_scores = {}
edge_weights = []

community_to_color = {
        '1' : 'tab:orange',
        '2' : 'tab:green',
        '3' : 'tab:red',
        '4' : 'tab:purple',
        '5' : 'tab:brown',
        '6' : 'tab:pink',
        '7' : 'salmon',
        '8' : 'tab:olive',
        '9' : 'tab:cyan',
        '10' : 'deeppink',
        '11' : 'darkblue',
        '12' : 'tab:blue'
    }
    #f.close()
node_color = {}

connections = conns_input.readlines()
for conn in connections:
    sconn = conn.split()
    from_gene = sconn[1]
    from_genes.append(from_gene)
    to_gene = sconn[2]
    to_genes.append(to_gene)

with open(gene_scores_file, 'r') as gs:
    gene_scores = json.load(gs)
    for gene, score in gene_scores.items():
        adjusted_scores[gene] = score*100
gs.close()


df = pd.DataFrame({ 'from':from_genes, 'to':to_genes})
G=nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.Graph() )
node_to_community = dict()

with open(loci_dict, 'r') as f:
    FA_loci = json.load(f)
    for loci, genes in FA_loci.items():
        partition = len(FA_loci[loci])
        partition_sizes.append(partition)

        for gene in genes:
            node_to_community[gene] = loci
            node_color = {node: community_to_color[community_id] \
                          for node, community_id in node_to_community.items()}


    fig, ax = plt.subplots()
    #nx.draw(G, with_labels=True, node_color=carac['myvalue'].astype(int), cmap=plt.cm.Blues)
    Graph(G,
          with_labels=True,
          node_color=node_color,  # indicates the community each belongs to
          node_size=adjusted_scores,
          node_edge_width=0,  # no black border around nodes
          edge_width=0.1,  # use thin edges, as they carry no information in this visualisation
          edge_alpha=0.5,  # low edge alpha values accentuates bundles as they appear darker than single edges
          node_layout='community', node_layout_kwargs=dict(node_to_community=node_to_community),
          edge_layout='bundled',
          ax=ax,
          )
    plt.show()
