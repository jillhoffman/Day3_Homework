# Scoring Fanconi Anemia (FA) Genes

### Description
This repository scores FA genes based on the connections they have to other FA genes.

### Link to Report
https://docs.google.com/document/d/1hzQlDRdp8NHvUiILaMTNbizzYiQlVIMj2bqs_jOXA7U/edit?usp=sharing 

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
    cd Day3_Homework/M3
    
### Input/Output Files  
All input files for gene_scoring.py and scores_vis.py and in the input_files folder. For gene_scoring.py the required files are:  
**input.gmt.txt:** All FA genes sorted by loci  
**FA_subnetworks.json:** 5,000 random subnetworks of FA genes with 1 gene per loci  
**M3_Input.txt:** All FA gene connections  

For scores_vis.py the additional files created from the gene_scoring.py are required and present in the output_file folder:
**FA_loci.json:** Dictionary of each FA loci and the genes in the loci  
**gene_scores.json:** Dictionary of each gene and its score  

### Run gene_scoring.py

    python gene_scoring.py

### Run scores_vis.py

    python scores_vis.py
