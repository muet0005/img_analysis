import os as os
import sys as sys
import knicr.fmri.fmri_utils as kfmriu
import getopt 


featDir = False; mni_brain = False; subj = False

opts, args = getopt.getopt(sys.argv[1:], "s:f:m:h", ["feat_dir=", "mni_brain=", "help"])

for o, a in opts:
	if o in ('-h', '--help'):
		print 'Help information here!'
	elif o in ('-f', '--feat_dir'):
		featDir = a
	elif o in ('-m', '--mni_brain'):
		mni_brain = a
	elif o in ('-s', '--subject'):
		subj = a

if not featDir or not mni_brain or not subj:
	print 'Please pass the following arguments:'
	print 'python ./mk_fsf_files.py -f featdir -m mni_brain -s subject'
	sys.exit(0)


subjs = os.listdir(featDir)

fmrinii_pfix = 'rs-160_idc_'

featdir_sfix = '_22May2013.feat'

tr = 2.0; te = 30; cluster = True

fsfFile = os.path.join(featDir, subj, 'idc_' + str(subj) + featdir_sfix + '.fsf')
genFSF = kfmriu.genFSLfsf(fsfFile, featDir, subj, fmrinii_pfix, featdir_sfix, tr, te, mni_brain, cluster)
genFSF.genPreStatsfsf()
