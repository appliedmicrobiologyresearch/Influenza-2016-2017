# Influenza-2016-2017
This repository contains the scripts for the analysis of Samples collected in the Influenza season 2016/2017

# make_SNP_clusters.py

This script clusters aligned sequences based on a SNP distance cutoff.

Usage: python make_SNP_clusters.py alignment.fasta snp_difference(int) 

# permutation_test_influenza_cluster.py

This script counts the number of samples that are in the same cluster (from make_SNP_clusters.py) between two quartiers. Additionally it performs a permutation test that randomly assignes quartiers to the different samples. The output is intended to be visualised using Circos.

Usage: python permutation_test_influenza_cluster.py Cluster_information_file.txt
