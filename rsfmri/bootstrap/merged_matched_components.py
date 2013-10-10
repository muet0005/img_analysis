import os as os
import nipype.interfaces.fsl as fsl

#specify the inputs
DIR = '/Volumes/rbraid/mr_data_idc/aug2013_final/rsfmri/melodic_samples_d16_initial/matched'
oDIR = os.path.join(DIR, 'merged')

templates = ['cerebellum', 'DMN', 'inferior_mid_frontal', 'insula_subcortical', 'left_pf', 'mid_frontal', 'noise_ant_frontal', 'noise_lower_brainstem', 'noise_pons_vessel', 'noise_sinus', 'noise_sup_frontal', 'noise_susceptibility', 'noise_upper_brainstem', 'noise_vent_wm', 'parietal', 'right_pf', 'sensory_motor', 'superior_mid_frontal', 'visual']
nsamples = 100

for template in templates:
	fList = []
	for s in range(0, nsamples):
		if s < 10:
			s_str = '000' + str(s)
		elif s < 100:
			s_str = '00' + str(s)
		elif s < 1000:
			s_str = '0' + str(s)
		else:
			s_str = str(s)
		f = os.path.join(DIR, template + '_' + s_str + '.nii.gz')
		print f
		if os.path.exists(f):
			fList.append(f)
	oFile = os.path.join(DIR, 'merged', template + '_merged.nii.gz')
	print fList
	fslmerge = fsl.Merge(dimension='t', terminal_output='stream',in_files=fList, merged_file=oFile, output_type='NIFTI_GZ')
	fslmerge.run()
