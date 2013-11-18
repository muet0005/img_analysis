import os as os
import knicr.fmri.fmri_utils as kfmri

DIR = '/home/genr/data/rsfmri'

nSubs = 50
nSamples = 1000
startSample = 0
dirname = 'melodic_samples_d16_n50_s1000'

mDIR = os.path.join(DIR, dirname)

subj_list = os.path.join(mDIR, 'cbcl_clinical_cutoff_IDC_N486.txt')

gbs = kfmri.gen_bootstrap_samples()

gbs.read_subj_list(subj_list)

gbs.gen_samples(startSample, nSamples, nSubs)

gbs.gen_melodic_lisa(startSample, DIR, 'idc_', '_27July2013.feat', mDIR, dirname)

