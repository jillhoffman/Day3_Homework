# Day3_Homework

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

### How to Run
Clone this repo in desired directory:

    git clone https://github.com/jillhoffman/Day3_Homework.git
  
Unzip Input Files In Terminal: (Can also do manually outside of terminal)

    sudo-apt get unzip
    unzip ./Input
  
Run code in terminal:

    python3 ./Day3_Visualization
