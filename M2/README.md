# Finding Significance of Fanconi Anemia Gene Connections

### Description
This repository finds the significane of Fanconi Anemia (FA) gene connections. By generating 5,000 subnetworks of 12 FA genes, 1 from each locus, a permutation test was preformed to determine the signifigance of the connections.

### Link to Report:
https://docs.google.com/document/d/1E2g8Mg1jo5_NV71LYsiTDda8vqYYXyRoC2QrMDKpQlM/edit?usp=sharing 

### Note on Scripts
The main script in this repo is p-value_calc.py. This is the script that compares the average edge weights from the FA and null set of subnetworks via a permutation test, returning a p-value. This script uses a json dictionary of each subnetworks average edge weight for both the FA and null subnetworks. The other four scripts in this repo were used to create supporting files to generate the input data. All scripts and usages will be outlined below.

### Requirements
Python 3.10    
Git Bash or Linux (optional)

No additional packages or specific environment is needed.

### Set Up 
Clone this repo in desired directory and go to folder:

    git clone https://github.com/jillhoffman/Day3_Homework.git
    cd Day3_Homework/W2
  
Unzip Input Files In Terminal: (Can also do manually outside of terminal)

    sudo-apt get unzip
    unzip ./input_data/input_files.zip
  
### Run main code: p-value_calc.py

**Input Files:** Dictionaries of average edge weights for both null and FA subnetwork sets.
**Input File Locations:** /densities/null_subnetwork_densities.json, /densities/FA_subnetwork_densities.json

All input files are provided. To run copy and paste:

    python p-value_calc.py

**Run Time = 10-20 minutes**

### Other scripts description and running

#### connection_bins.py

**Input Files:** gmt input file of all FA genes sorted by loci, string file of every known gene connetion.
**Input File Locations:** input_data/input.gmt.txt, input_data/STRING1.txt
**Output Files:** This script generates a json dictionary of genes sorted into connection bins based on total number of occurances in STRING file. The dictionary is in dictionaries/connection_bins.json and is used in the null_subnetworks.py script.

All input files are provided. To run copy and paste:

    python connection_bins.py

**Run Time = 30-60 minutes**

#### FA_subnetworks.py

**Input Files:** gmt input file of all FA genes sorted by loci, located at input_data/input.gmt.txt
**Output Files:** This script generates a json dictionary of 5,000 unique FA subnetworks of 12 genes each, 1 gene from each loci. The dictionary is in dictionaries/FA_subnetworks.json and is used in null_subnetworks.py and densities.py. The number of subnetworks generated can be editied by changing line 7 in the script.

All input files are provided. To run copy and paste:

    python FA_subnetworks.py

**Run Time = 5-10 minutes**

#### null_subnetworks.py

**Input Files:** FA_subnetworks.json dictionary, connection_bins.json dictionary
**Output Files:** This script generates a json dictionary of 5,000 unique random gene subnetworks of 12 genes each. Genes from the FA_subnetworks are replaced by random genes in the same connection bin. The dictionary is in dictionaries/null_subnetworks.json and is used in densities.py.

All input files are provided. To run copy and paste:

    python null_subnetworks.py
    
**Run Time = 5-10 minutes**

#### densities.py

**Input Files:** STRING.txt, FA_subnetworks.json dictionary, null_subnetworks.json dictionary
**Output Files:** This script generates a json dictionary of average edge weights for each subnetwork in both the FA and null set. The outputs are densities/FA_subnetwork_densities.json and densities/null_subnetwork_densities.json, which are used in p-value.py.

All input files are provided. To run copy and paste:

    python densities.py

**Run Time = 30-45 minutes**
    

                  



