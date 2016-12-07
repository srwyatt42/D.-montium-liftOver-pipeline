# liftOver Pipeline
#created by Sydney Wyatt
#part of the Kopp Lab at UC Davis

#This pipeline was developed for use in establishing the D montium subgroup phylogeny. Specifically, this simple python script should allow the user to easily use the liftOver application to convert gene coordinates between genome assemblies. The script output includes BED files (mapped and unMapped) from liftOver renamed with the Fasta file name and gene BED file name as well as a Fasta file of the mapped genes with the same naming format.

#The liftOver application requires two inputs: a BED file of the gene of interest from the original assembly, and the appropriate chain file allowing conversion between the original genome assembly and the 'new' genome assembly. In the D montium project, the genes of interest were pulled from FlyBase in the D melanogaster assembly. The chain files were generated in a program like BLASTZ by aligning the D melanogaster genome assembly to each species in the subgroup. The chain files contain blocks of the best/longest syntenic regions linked together. liftOver acts similar to BLAST with the gene BED file input on the chain file, returning a BED file containing coordinates from each species in the subgroup. These sequences can then be used for phylogenetic analysis. For example, the pipeline can take a BED file of D melanogaster gene coordinates and a chain file of D melanogaster to D serrata alignment and return a BED file of D serrata gene coordinates. Documentation of the commands can be found by running liftOver without arguments; more usage information can be found at http://genome.sph.umich.edu/wiki/LiftOver

#The bedtools application is used to create a Fasta file from the liftOver output using the getfasta command. This command takes a Fasta genome assembly input and the BED file output from liftOver to create a Fasta file of the gene sequences in the new organism. Following the example from above, this code returns a Fasta file of D serrata gene sequences when given the D serrata BED file and the D serrata Fasta genome assembly file.

#Some things to note:
#1. It is imperative that this script, BED files, chain files, Fasta files, the liftOver application, and the bedtools application are located in the same directory.
#2. To download liftOver, UCSC Genome Browser offers a Mac OSX application and a Unix application. I would suggest using the Linux application because it comes with many other Unix applications that may be useful for other research.
#3. If using this script for Drosophila research, BED files can be obtained from the FlyBase notation on https://www.biotools.fr/drosophila/fbgn_to_bed
#4. Chain files can be downloaded from the UCSC site or new ones can be generated as described above.
#5. Finally, UCSC notes that liftOver was only intended to be used between genome builds of the same species; however it can be used between species with acceptable accuracy. Please double check final outputs to ensure success. Additionally, problems may arise if the chain files and BED files were created using different assembly versions. 
