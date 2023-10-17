# CRISPR-Technology-based-Bioinformatics-Data-Science-Research-Work
## STEPS involved in the experiment:
  
### The Bed_file_generator python script converts the mouse-chromosome-19 guide samples txt file to a Bed file that will be used for customizing sgRNA guides over mouse genome. 
### The output generated from the script, which is a Bed file, has 9 columns.
  --> The first column represent the chromosome number which is 19 for my test case.
  --> The 2nd and 3rd column represents the predicted guide positioning with respect to the genome. 
  --> The 4th column represents all the guide sequences.
  --> The 5th column represents all guide consensus scoring for showing each guide's efficiency.
  --> The 6th column represents whether a guide is having a positive strand or negative strand.
  --> The 7th and 8th column represents the thick start and thick end of each guide which is similar to each guide positioning value. It is a way to display each guide thicker.
  --> The 9th column represents the specificity scoring of each guide. Each guide is depicted with a color for diplaying the specificity.
  
  
### Once the file is generated go to the UCSC browser and select Mouse (GRCm39/mm39) genome. (https://genome.ucsc.edu/cgi-bin/hgTracks?db=mm39&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr12%3A569345%2D869000&hgsid=1499501063_dxOwedM4QF5ATa1tt3VdXCD3vHkk)
  
### Select the add custom tracks tab beneath the display. 
### Then on the custom track page select upload option and choose the bed file generated. 
### Return to the Mouse (GRCm39/mm39) genome page and you can now see the display for each guide along with their specificity and efficiency scoring.
