#Pipeline for D montium genomes, phylogenetic analysis

input_gene = []       #stores GenBank gene sequence files
input_chain = []      #stores over.chain files for liftOver

#User input gene sequence(s); sequences need to be in known genome like Dmel
gene = input("Enter gene sequence file: ")
input_gene.append(gene)
more_gene = input("Add another? ")
#to add mutliple gene sequence files
if more_gene == "y":
    y = input("Enter gene sequence file: ")
    input_gene.append(y)
    more_gene = input("Add another? ")
if more_gene == "n":
    print("File(s) added")
    print(input_gene)

#User input over.chain file(s); example Dmel_to_Dmontium.over.chain
chain = input("Enter over.chain file: ")
input_chain.append(chain)
more_chain = input("Add another? ")
#to add mutliple over.chain files
if more_chain == "y":
    y = input("Enter chain file: ")
    input_chain.append(y)
    more_chain = input("Add another? ")
if more_chain == "n":
    print("File(s) added")
    print(input_chain)

import subprocess   #allows python to run Unix commands
#cd to folder with all the files
subprocess.call(['cd', 'C:\Users\Sydney\Desktop']) #INSERT REAL PATH LATER
#GenBank to GFF in Unix
gff_gene = []
for file in input_gene:
    filename.gbk = input_gene[file]
    gff_gene.append(subprocess.call(['perl', 'genbank2gff3.pl', '-f', 'GenBank', 'filename.gbk', '-out', 'stdout', '>', 'filename.gff3']))
#perl genbank2gff3.pl -f GenBank filename.gbk -out stdout > filename.gff3
print(gff_gene)

#GFF to Bed in Unix
bed_gene = []
for file in gff_gene:
    inputfile.gff = gff_gene[file]
    bed_gene.append(subprocess.call(['gff2bed', '<', 'inputfile.gff', '>', 'outputfile.bed']))
#gff2bed < inputfile.gff > outputfile.bed
print(bed_gene)




#Pipe to liftOver application to find gene in each genome; example Dmel gene sequence would be found in Dmontium 
    #liftOver needs to be installed on user's computer
    #Path will be specified here; include in README
    #All sequence and chain files should be included in the same place as liftOver
liftOver_output = []        #Stores lifted output BED files
for file in input_chain:
    input_file.over.chain = input_chain[file]
    for file in bed_gene:
        input_file.bed = bed_gene[file]
        #feed to liftover via subprocess
        liftOver_output.append(subprocess.call(['liftover', '-minMatch=0.1', '-multiple', 'input_file.bed', 'input_file.over.chain', 'output_file.bed', 'unMapped']))
print(liftOver_output)
    
#liftOver outputs bed files of the gene in another genome
