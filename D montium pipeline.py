#Pipeline for D montium genomes, phylogenetic analysis

#Ensure that liftOver, chain files, bed files,
#and this script are all in the same folder

input_gene = []       #stores BED gene sequence files
input_chain = []      #stores over.chain files for liftOver

#use glob module to collect .bed and .over.chain files
import glob

#collect .over.chain files
for filename in glob.iglob('PATH/*.over.chain'):    #Insert PATH
    input_chain.append('%s' % filename)
print(input_chain)

#collect .bed files
for filename in glob.iglob('PATH/*.bed'):       #Insert PATH
    input_gene.append('%s' % filename)
print(input_gene)

import subprocess   #allows python to run Unix commands

#Pipe to liftOver application to find gene in each genome
#Example Dmel gene sequence would be found in Dmont

liftOver_output = []        #Stores lifted output BED files

for i in input_chain:
    for i in bed_files:
       subprocess.call(['./liftover', '-minMatch=0.1', '-multiple', 'bed_files[i]', 'chain_files2[i]', 'output_file.bed', 'unMapped'])

#fix the for loop so that it feeds into liftover correctly
#is there a way to get output_file.bed to be filename.bed? 

#liftOver outputs bed files of the gene in another genome
