
#use glob to gather files in appropriate pathway
import glob
chain_files2 = []
for filename in glob.iglob('/Users/kopplab/Desktop/Syd_LiftOver_Stuff/*.over.chain'):
    chain_files2.append('%s' % filename)
print(chain_files2)

bed_files = []
for filename in glob.iglob('/Users/kopplab/Desktop/Syd_LiftOver_Stuff/*.bed'):
    bed_files.append('%s' % filename)
print(bed_files)

import subprocess
subprocess.call(['cd', '/Users/kopplab/Desktop/Syd_LiftOver_Stuff'])
print(subprocess.check_output(['pwd']))
#subprocess not changing the directory correctly

for i in chain_files2:
    print(i)
    for i in bed_files:
        print(i)
        subprocess.call(['./liftover', '-minMatch=0.1', '-multiple', 'bed_files[i]', 'chain_files2[i]', 'output_file.bed', 'unMapped'])
#fix the for loop so that it feeds into liftover correctly
#is there a way to get output_file.bed to be filename.bed?
