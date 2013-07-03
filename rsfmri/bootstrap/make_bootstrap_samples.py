import os as os
import knicr.fmri.fmri_utils as kfmri

DIR = '/home/genr/data/rsfmri'

mDIR = os.path.join(DIR, 'melodic_bootstrap_test')

subj_list = os.path.join(DIR, 'bootstrap_samples', 'subj_list.txt')

gbs = kfmri.gen_bootstrap_samples()

gbs.read_subj_list(subj_list)

gbs.gen_samples(10, 35)

gbs.gen_melodic_lisa(DIR, '_22May2013.feat', mDIR, 'melodic_test_dim20')

