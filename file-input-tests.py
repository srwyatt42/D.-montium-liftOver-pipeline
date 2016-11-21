
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
