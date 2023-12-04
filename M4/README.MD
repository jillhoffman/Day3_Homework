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

All input files for genetic_algo.py and some for top10values.py are in the input_files folder. For gene_scoring.py the required files are: 

**input.gmt.txt:** All FA genes sorted by loci  
**FA_subnetworks.json:** 5,000 random subnetworks of FA genes with 1 gene per loci  
**M3_Input.txt:** All FA gene connections  

For scores_vis.py the additional files created from the gene_scoring.py are required and present in the output_file folder:

**FA_loci.json:** Dictionary of each FA loci and the genes in the loci  
**gene_scores.json:** Dictionary of each gene and its score
