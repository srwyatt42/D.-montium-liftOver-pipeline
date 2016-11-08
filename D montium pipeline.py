#Pipeline for D montium genomes, phylogenetic analysis

#User input genome(s)
genome = input("Enter genome file: ", "r+")

#User input gene sequence(s)
loci = input("Enter gene sequence file: ", "r+")
#Convert file to BED format

#Pipe to liftOver application to find loci in each genome
    #liftOver needs to be installed on user's computer
    #Path will be specified here; include in README
#liftOver outputs chain files of loci in each genome

#Convert files into FASTA format for use in other programs (alignment, etc)
