# liftOver Pipeline
#created by Sydney Wyatt
#part of the Kopp Lab at UC Davis

#This pipeline was developed for use in establishing the D montium species group phylogeny. Specifically, this simple python script should allow the user to easily use the liftOver application to convert genome coordinates and annotation files between genome assemblies. The script output includes BED files (mapped and unMapped) from liftOver renamed with the Fasta file name and gene BED file name as well as a Fasta file of the mapped genes with the same naming format.

#The liftOver application requires two inputs: a BED file of the gene of interest from the original assembly, and the appropriate chain file allowing conversion between the original genome assembly and the 'new' genome assembly. For example, in the D montium project, the genes of interest were pulled from FlyBase in the D melanogaster assembly. The chain file then locates the equivalent D melanogaster sequence in another species, say D serrata. liftOver provides the new sequences (in D serrata if we keep with the example) in a BED file. These sequences can then be used for phylogenetic analysis. Documentation of the commands can be found by running liftOver without arguments; more usage information can be found at http://genome.sph.umich.edu/wiki/LiftOver

#The bedtools application is used to create a Fasta file from the liftOver output using the getfasta command. This command takes a Fasta alignment input and the BED file output from liftOver to create a Fasta file of the genes in the new organism. Following the example from above, this code returns a Fasta file of genes in D serrata when given the output BED file and the D serrata Fasta alignment file.

#Some things to note:
#1. It is imperative that this script, BED files, chain files, Fasta files, the liftOver application, and the bedtools application are located in the same directory.
#2. To download liftOver, UCSC Genome Browser offers a Mac OSX application and a Linux application. Please use the one most appropriate to your situtation.
#3. If using this script for Drosophila research, BED files can be obtained from the FlyBase notation on https://www.biotools.fr/drosophila/fbgn_to_bed
#4. Chain files can be downloaded from the UCSC site or align your 'new' genome assembly to the orginal assembly. For example, align the D serrata genome assembly to D melanogaster and generate the chain file.
#5. Finally, UCSC notes that liftOver was only intended to be used between genome builds of the same species; however it can be used between species with acceptable accuracy. Please double check final outputs to ensure success. Additionally, problems may arise if the chain files and BED files were created using different assembly versions. 
