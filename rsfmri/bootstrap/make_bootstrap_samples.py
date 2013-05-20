import os as os
import gen_bs_samples as gbs

DIR = '/Volumes/mdraid1/mr_data_idc/feb2012_datalock/rfmri'

mDIR = os.path.join(DIR, 'melodic_bootstrap_test')

subj_list = os.path.join(DIR, 'bootstrap_samples', 'test_subj_list.txt')


gbsc = gbs.gen_bootstrap_samples()

gbsc.read_subj_list(subj_list)

gbsc.gen_samples(1, 10)

gbsc.gen_melodic_lisa(DIR, '_Apr2013.feat', mDIR, 'melodic_test')

