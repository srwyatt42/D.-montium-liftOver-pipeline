#Pipeline for D montium genomes, phylogenetic analysis

#Ensure that liftOver, chain files, bed files,
#and this script are all in the same folder

input_gene = []       #stores BED gene sequence files
input_chain = []      #stores over.chain files for liftOver


#use glob module to collect .bed and .over.chain files
import glob

#collect .over.chain files
for chainfilename in glob.iglob('*.over.chain'):   #Insert PATH
    input_chain.append('%s' % chainfilename)
print(input_chain)


#collect .bed files
for genefilename in glob.iglob('*.bed'):       #Insert PATH
    input_gene.append('%s' % genefilename)
print(input_gene)

import subprocess   #allows python to run Unix commands

#Pipe to liftOver application to find gene in each genome
#Example Dmel gene sequence would be found in Dmont
from os import rename
from os import listdir
x=0

for name in input_chain:
    with open(name) as f:
        chain_input = open('chain_input.over.chain', 'w')
        chain_input.write(f.read())
        chain_input.close()
    for name in input_gene:
        with open(name) as f:
            bed_input = open('bed_input.bed', 'w')
            bed_input.write(f.read())
            bed_input.close()
            subprocess.call(['./liftOver', '-minMatch=0.1', '-multiple', 'bed_input.bed', 'chain_input.over.chain', 'output.bed', 'output.unMapped.bed'])
            #Rename output.bed to something relevant
            badprefix = 'output'
            fnames = listdir('.')
            print(fnames)
            for fname in fnames:
                if fname.startswith(badprefix):
                    rename(fname, fname.replace(badprefix, ''.join([chainfilename, genefilename])))
    x+=1
#liftOver outputs bed files of the gene in another genome
