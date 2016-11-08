#Pipeline for D montium genomes, phylogenetic analysis

genomes = []    #stores genome sequence files
loci = []       #stores loci sequence files

#User input genome(s)
genome = input("Enter genome file: ")
genomes.append(genome)
more_genomes = input("Add another? ")
#to add multiple genome files
if more_genomes == "y":
    y = input("Enter genome file: ")
    genomes.append(y)
    more_genomes = input("Add another? ")
if more_genomes == "n":
    print("File(s) added")
    print(genomes)

#User input gene sequence(s)
locus = input("Enter gene sequence file: ")
loci.append(locus)
more_loci = input("Add another? ")
#to add mutliple gene sequence files
if more_loci == "y":
    y = input("Enter genome file: ")
    loci.append(y)
    more_loci = input("Add another? ")
if more_loci == "n":
    print("File(s) added")
    print(loci)


#Convert file to BED format

#Pipe to liftOver application to find loci in each genome
    #liftOver needs to be installed on user's computer
    #Path will be specified here; include in README
#liftOver outputs chain files of loci in each genome

#Convert files into FASTA format for use in other programs (alignment, etc)
