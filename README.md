# GC Content Analysis of Bacterial Genome

## Project Description
This project calculates and visualizes the GC content distribution of a bacterial genome using a sliding window approach in Python.  
GC content (the percentage of Nitrogenous bases that are either Guanine or Cytosine) is an important genomic feature used in bioinformatics to study genome composition, evolution, and gene prediction. It is important because G-C pairs are held together by 3 Hydrogen bonds (compared to 2 in A-T pairs), regions with high GC content are more thermally stable and chemically robust.

---

## Breakdown of the Code
- Parsing: Uses biopython to read the .fasta file which contains the complete genome data
- Sliding Window: Instead of calculating a single average, the script analyses chunks of 500bp and moves forward by 100bp increments. This allows us to see how the GC percentage fluctuates across the genome
- Visualisation: Uses matplotlib to generate a line graph representing the genomic content distribution

---

## Output
The output graph displays the GC percentage relative to the position in the genome.
The graph shows how the percentage of GC bases changes along the genome. The GC content is not the same everywhere, it goes up and down across different regions. 

GC-rich regions (high GC%) are more stable because GC base pairs have three hydrogen bonds. This means that these parts of the DNA are harder to separate and are more rigid. They are predicted to have higher melting temperatures and enhanced resistance to thermal denaturation. Additionally, these regions exhibit increased base-stacking interactions, resulting in greater mechanical stiffness and reduced conformational flexibility.

AT-rich regions (low GC%) are likely to display reduced thermal stability and increased structural flexibility because AT base pairs have only two hydrogen bonds. It can more easily unwound and bent, facilitating processes such as transcription initiation, activation of origin of replication, and regulatory protein binding. 

In the middle of the genome, there is a strong drop in GC content, at around 50% (the average or the baseline). The observed average GC content of 50% for Enterobacteria phage lambda suggests a balanced distribution of nucleotide pairs, optimised for stability and replication within its host, Escherichia coli, at physiological temperatures. 

---

Genome data downloaded from NCBI (excluded in repository due to size)
