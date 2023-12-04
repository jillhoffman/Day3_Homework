# Implementing Genetic Algorithm on Fanconi Anemia (FA) Genes

### Link to Report 
https://docs.google.com/document/d/160GWf9QyagfB_oe2Wh6ttiEZRKH_kXuJQjP2WPjkPHU/edit?usp=sharing 

### Requirements
Python 3.10  

### Packages Required for Visualization
matplotlib: https://matplotlib.org/  
networkx: https://networkx.org/  
netgraph: https://netgraph.readthedocs.io/    
pandas: https://pandas.pydata.org/ 

### Set Up 
Clone this repo in desired directory and go to folder:

    git clone https://github.com/jillhoffman/Day3_Homework.git/
    cd Day3_Homework/M4

### Input/Output Files  

All input files for genetic_algo.py and some for top10values.py, p-valueM4.py, scores_vis.py and gene_score_files.py are in the inputs folder. For genetic_algo.py the required files are: 

**input.gmt.txt:** All FA genes sorted by loci  
**FA_subnetworks.json:** 5,000 random subnetworks of FA genes with 1 gene per loci  
**M3_Input.txt:** All FA gene connections
**FA_loci.json:** Dictionary of each FA loci and its genes
**STRING.gmt:** All gene connections
**connection_bins.json:** Each gene from STRING sorted in bins by number of connections
**optimized_null_network.json:** 5,000 subnetworks of null gene cases, created using ../M2/null_subnetworks.py
**optimized_null_densities.json:** Densities of each optimized null subnetwork, created using densities.py in ../M2/densities.py
**optimized_densities.json:** Densities of optimized network after genetic alogrithm, created using ../M2/densities.py


For top10values.py, p-valueM4.py, scores_vis.py and gene_score_files.py the additional files are required and present in the outputs folder:

**optimized_network.json:** Dictionary of optimized subnetworks, created from genetic_algo.py 
**gene_scores_new.json:** Gene scores based on optimized_network.json, created from ../M3/gene_scoring.py

## Run genetic_algo.py
### Create optimized subnetwork and save stats on each generation in outputs/generational_stats.txt

    python genetic_algo.py

## Run gene_score_files.py
### Create GMT tab-delimeted file for each subnetwork where genes are ordered by decreasing gene score. Creates outputs/with_score.gmt, which includes the specific gene scores and outputs/without_scores.gmt, which only includes the gene.

    python gene_score_files.py

## Run top10values.py
### Create cytoscape input files of top 10 most dense subnetworks with p-value. All outputs in outputs folder.

    python top10values.py

## Run p-valueM4.py
### Calculate p-value on whole optimized population using t-test.

    python p-valueM4.py
