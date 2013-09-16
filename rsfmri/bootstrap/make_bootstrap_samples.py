import os as os
import knicr.fmri.fmri_utils as kfmri

DIR = '/home/genr/data/rsfmri'

mDIR = os.path.join(DIR, 'melodic_component_matching_d16')

subj_list = os.path.join(mDIR, 'subj_list.txt')

gbs = kfmri.gen_bootstrap_samples()

gbs.read_subj_list(subj_list)

gbs.gen_samples(10, 40)

gbs.gen_melodic_lisa(DIR, '_27July2013.feat', mDIR, 'melodic_component_matching_d16')

