#!/usr/bin/env python

#import numpy as np
import subprocess
import sys
import os
import random
import networkx as nx
 
inputOptions = sys.argv[1:]
 
#usage: python permutation_test_influenza_cluster.py Cluster_information_file.txt
 
 
def main():


	initial_result=calculte_connections(bool(0))
	
	randomiced_results=[]
	
	colors={1:"ffe6e6",0.05:"ff9999",0.01:"ff4d4d",0.005:"ff0000",0.001:"800000"}
	
	
	connection_count={}
	
	repetitions=10000
	for i in range(1,repetitions):
		randomiced_results.append(calculte_connections(bool(1)))
	
	
	to_test_blocks=initial_result.keys()
	coordinate_counter={}
	for i in to_test_blocks:
		coordinate_counter[i]=0
	
	for block in initial_result.keys():
		
		for block2 in to_test_blocks:

			counter=0
			for repetation in randomiced_results:
				

				if initial_result[block][block2]+initial_result[block2][block] <= repetation[block][block2]+repetation[block2][block]:
					counter+=1		
					
			pval=float(counter)/float(repetitions)
					
					
			for color_value in sorted(colors.keys(),reverse=True):

				if pval <= color_value:
					color=colors[color_value]
			
			if block!=block2:
				if initial_result[block][block2] != 0 and initial_result[block2][block] != 0:
					print block.replace(" ","_").replace(".","") +"\t"+str(coordinate_counter[block])+"\t"+str(coordinate_counter[block]+initial_result[block][block2])+"\t"+block2.replace(" ","_").replace(".","") +"\t"+str(coordinate_counter[block2])+"\t"+str(coordinate_counter[block2]+initial_result[block2][block])+"\t"+"color="+color+",thickness="+str(pval)+"p"

			coordinate_counter[block]+=initial_result[block][block2]
			coordinate_counter[block2]+=initial_result[block2][block]
	

		to_test_blocks.remove(block)# avoid double comparisons

	for block in coordinate_counter.keys():
	
		counter=0
		for repetation in randomiced_results:
				

			if initial_result[block][block] <= repetation[block][block]:
				counter+=1

					
		pval=float(counter)/float(repetitions)
					
					
		for color_value in sorted(colors.keys(),reverse=True):
			if pval <= color_value:
				color=colors[color_value]
	
		print "chr\t-\t"+block.replace(" ","_").replace(".","")+"\t"+block.replace(" ","_").replace(".","")+"\t0\t"+str(coordinate_counter[block]+1)+"\t"+color+"\t"+str(pval)

def calculte_connections(shuffle):

	#read input

	samples=[]
	blocks=[]
	clusters=[]

	with open(inputOptions[0],'r') as input_file:
		

		for raw_line in input_file:

			line=raw_line.replace("\n","").replace("\r","")
 			
 			samples.append(line.split("\t")[0])
			blocks.append(line.split("\t")[1])
			clusters.append(line.split("\t")[3])
 	
 	
 	clusters2samples={}
	blocks2samples={}
	clusters2blocks={}
	sample2cluster={}
	sample2block={}	
 			
 	if shuffle==bool(1):		
 		random.shuffle(blocks)		
 			
 	for sample_id,block,cluster in zip(samples,blocks,clusters):		
		
			if (block in blocks2samples.keys()) == bool(0):
				blocks2samples[block]=[]
			blocks2samples[block].append(sample_id)
			sample2block[sample_id]=block

			if cluster != "#N/A":
				if (cluster in clusters2samples.keys()) == bool(0):
					clusters2samples[cluster]=[]
					clusters2blocks[cluster]=[]

				clusters2blocks[cluster].append(block)
				sample2cluster[sample_id]=cluster

	cluster_directed_connections={}

	#compare blocks
	for block in blocks2samples.keys():
	
		block_count={}
		for block2 in blocks2samples.keys():
			block_count[block2]=0
			
		for sample_id in blocks2samples[block]:
			
			if (sample_id in sample2cluster.keys()) == bool(1):
				
				for block2 in block_count.keys():
				
					if block2== block: # If to connected block are counter, the self count must be avoided
						if clusters2blocks[sample2cluster[sample_id]].count(block2) >= 2:						
							block_count[block2]+=1
														
					else:
						if clusters2blocks[sample2cluster[sample_id]].count(block2) >= 1:						
							block_count[block2]+=1
					
		cluster_directed_connections[block]=	block_count								

	return cluster_directed_connections

main()			
