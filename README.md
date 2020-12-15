# Influenza-2016-2017
This repository contains the scripts for the analysis of Samples collected in the Influenza season 2016/2017

# make_SNP_clusters.py

This script clusters aligned sequences based on a SNP distance cutoff.

    Usage: python make_SNP_clusters.py alignment.fasta snp_difference(int) 

    Example: python make_SNP_clusters.py whole_genome_alignment.aln 10 > clustered_strains.txt

# permutation_test_influenza_cluster.py

This script counts the number of samples that are in the same cluster between any two groups. Additionally it performs a permutation test that randomly assigns groups to the different samples.
The input can be the output from make_SNP_clusters.py, which is a table with the sequence identifers from the initial alignment in the first coloum and the cluster ID in the second coloumn (cluster:XXX). Alternatively, any output from a clustering software can be used, e.g. Cluster Picker (https://hiv.bio.ed.ac.uk/software.html), which infers clusters based on a genetic divergence threshold and also results in a table with the sequence identifier and cluster identifier. 
Either of those outputs (clusters defined by SNP distance or clusters defined by divergence) need to be amended with ancillary information, which define the groups to which each sequence belongs (e.g. a city quarter). The final input file should contain four coloumns: sequence ID, group, colour code for visualising group, cluster ID. The output is intended to be visualised using Circos (http://www.circos.ca/).

    Usage: python permutation_test_influenza_cluster.py table_file_with_information.txt

    Example: python permutation_test_influenza_cluster.py Strain_cluster_information_file.txt > analysis.txt

# visualisation using circos
The output file from permutation_test_influenza_cluster.py, e.g. called analysis.txt contains two sections, which need to be separated into links.tab and BacteriaContigs.txt, to be run with ciros. 

Circos requires three input files
 * circos.conf -- is the configuration file, contains names of input files and colour codes among other settings  
 * links.tab -- is upper part of analysis.txt; contains the between-group links as well as the line thinkness and colour for between-group shared clusters  
 * BacteriaContigs.txt -- is lower part of analysis.txt and starts with "chr -"; contains the groups (e.g. quarter) and the within-group size (number sequences in this group), p-value for group-specific clusters compared to randomly assigned clusters to the groups, as well as the colour code for visualisation.
 
Execute circos in the folder that contains your input files.

    Usage: ~/software/circos-0.69-9/bin/circos 

Please refer to the software manuals for details.
