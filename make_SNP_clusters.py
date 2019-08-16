#!/usr/bin/env python

#import numpy as np
import subprocess
import sys
import os
import networkx as nx
 
inputOptions = sys.argv[1:]
 
#usage: alignment.fasta snp_difference (int) 
 
def main():

	edges=[]
	sequences={}
	with open(inputOptions[0],'r') as input_file:
		

		for raw_line in input_file:

			line=raw_line.replace("\n","").replace("\r","")

			if line[0:1]!=">":
				sequences[header]+=line.lower() 
			else:
				header = line[1:]
				sequences[header]=""
   
	counter=0
	
	for sequence1 in sequences.keys():
		counter+=1
		#print counter
		for sequence2 in sequences.keys():
			pair_count=0
			for i in range(0,len(sequences[sequence1])):
				
				if sequences[sequence1][i] != "n" and sequences[sequence2][i] != "n" :
					if sequences[sequence1][i]  != sequences[sequence2][i] :
						pair_count+=1
							
			if pair_count <= int(inputOptions[1]) and sequence1 != sequence2 :
				edges.append([sequence1,sequence2])	
					
	cluster_counter=0
	graph=nx.Graph()
	graph.add_edges_from(edges)
	for cluster in nx.connected_components(graph):
		cluster_counter+=1
		for strain in cluster:
			print strain.split(":")[0] +"\tcluster:"+str(cluster_counter)
			
	strains = 	set(sequences.keys())
	for connected in nx.connected_components(graph):
		strains=strains-set(connected)
		
	for strain in strains:
		cluster_counter+=1
		print strain.split(":")[0] +"\tcluster:"+str(cluster_counter)
					
main()		
