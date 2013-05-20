import os as os
import knicr.fmri.fmri_utils.gen_bootstrap_samples as gbs

DIR = '/home/genr/data/rsfmri'

mDIR = os.path.join(DIR, 'melodic_bootstrap_test')

subj_list = os.path.join(DIR, 'bootstrap_samples', 'subj_list.txt')

gbsc = gbs.gen_bootstrap_samples()

gbsc.read_subj_list(subj_list)

gbsc.gen_samples(10, 35)

gbsc.gen_melodic_lisa(DIR, '_Apr2013.feat', mDIR, 'melodic_test')

