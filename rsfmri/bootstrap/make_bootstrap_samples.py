import os as os
import knicr.fmri.fmri_utils as kfmri

DIR = '/home/genr/data/rsfmri'

nSubs = 40
nSamples = 20
startSample = 0
dirname = 'melodic_component_matching_d20'

mDIR = os.path.join(DIR, dirname)

subj_list = os.path.join(mDIR, 'subj_list.txt')

gbs = kfmri.gen_bootstrap_samples()

gbs.read_subj_list(subj_list)

gbs.gen_samples(startSample, nSamples, nSubs)

gbs.gen_melodic_lisa(startSample, DIR, 'idc_', '_27July2013.feat', mDIR, dirname)

