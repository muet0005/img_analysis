import os as os
import knicr.fmri.fmri_utils as kfmri

DIR = '/home/genr/data/rsfmri'

nSubs = 40
nSamples = 20
startSample = 10

mDIR = os.path.join(DIR, 'melodic_component_matching_d16')

subj_list = os.path.join(mDIR, 'subj_list.txt')

gbs = kfmri.gen_bootstrap_samples()

gbs.read_subj_list(subj_list)

gbs.gen_samples(nSamples, nSubs)

gbs.gen_melodic_lisa(startSample, DIR, 'idc_', '_27July2013.feat', mDIR, 'melodic_component_matching_d16')

