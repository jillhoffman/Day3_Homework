# Fanconi Anemia Gene Connections

### Description
This code is designed to take a gmt format file of disease genes and find all possible subnetworks between the genes, creating a new file to be used as an input to create a visualization network.

### Requirements
Python 3.10    
Git Bash or Linux (optional)

No additional packages or specific environment is needed.

### Inputs and other files
The input_files.zip include a file with all known FA genes and STRING file containing all disease genes and their connections.

**STRING1.txt** = all disease genes  
**input.gmt.txt** = list of FA genes  
**Day3_Visualization.py** = main script to run code  

### Example Outputs
The expected output file and example of the visualization can be found under the example_outputs folder

### How to Run
Clone this repo in desired directory:

    git clone https://github.com/jillhoffman/Day3_Homework.git
  
Unzip Input Files In Terminal: (Can also do manually outside of terminal)

    sudo-apt get unzip
    unzip ./Input
  
Run code in terminal:

    python3 ./Day3_Visualization

#### Time to Run = 10-15 minutes
#### Link to Report:
https://docs.google.com/document/d/1e8ZQCesrbiJ1mgCTEJDuNWUF45mB7toNUg1ro98OwjA/edit?usp=sharing 
