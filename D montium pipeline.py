#Pipeline for D montium genomes, phylogenetic analysis

#Ensure that liftOver, chain files, bed files,
#and this script are all in the same folder

input_gene = []       #stores BED gene sequence files
input_chain = []      #stores over.chain files for liftOver
input_alignment = []  #stores Fasta files for conversion after liftOver


#use glob module to collect .bed and .over.chain files
import glob

#collect .over.chain files
for chainfilename in glob.iglob('*.over.chain'):
    input_chain.append('%s' % chainfilename)

#collect .bed files
for genefilename in glob.iglob('*.bed'):
    input_gene.append('%s' % genefilename)

#collect .fa files
for fafilename in glob.iglob('*.fa'):
    input_alignment.append('%s' % fafilename)

import subprocess   #allows python to run Unix commands

#Pipe to liftOver application to find gene in each genome
#Example: Dmel gene sequence would be found in Dserr
from os import rename
from os import listdir

#Loop: for a given chain file and fa file, find all the genes from the bed files

for faname, chainname in zip(input_alignment, input_chain):
    with open(faname) as f:
        alignment = open('alignment.fa', 'w')
        alignment.write(f.read())
        alignment.close()
    with open(chainname) as f:
        chain_input = open('chain_input.over.chain', 'w')
        chain_input.write(f.read())
        chain_input.close()
    for genename in input_gene:
        with open(genename) as f:
            bed_input = open('bed_input.bed', 'w')
            bed_input.write(f.read())
            bed_input.close()
            subprocess.call(['./liftOver', '-minMatch=0.1', '-multiple', 'bed_input.bed', 'chain_input.over.chain', 'output.bed', 'output.unMapped.bed'])
        #liftOver outputs a bed file with the genes found in new alignment/species
        #Convert output.bed to output.fa using bedtools
        subprocess.call(['./bedtools', 'getfasta', '-fi', 'alignment.fa', '-bed', 'output.bed', '-name', '-fo', 'output.fa'])
        #Delete .fai file so bedtools will write a new one each time
        files = [i for i in glob.iglob('*.fai')]
        subprocess.call(['rm', '-r'] + files)
        #Rename output.fa to include fa and gene names
        badprefix = 'output'
        fnames = listdir('.')
        for fname in fnames:
            if fname.startswith(badprefix):
                rename(fname, fname.replace(badprefix, ''.join([faname, genename])))
