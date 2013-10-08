import os as os
import nibabel as nb
import numpy as np
from scipy import spatial as sp
from scipy.spatial.distance import rogerstanimoto
from scipy.stats.stats import pearsonr as pr

#specify the inputs
DIR = '/Volumes/rbraid/mr_data_idc/aug2013_final/rsfmri/melodic_samples_d16_initial'
oDIR = os.path.join(DIR, 'matched')

templates = ['cerebellum', 'DMN', 'inferior_mid_frontal', 'insula_subcortical', 'left_pf', 'mid_frontal', 'noise_ant_frontal', 'noise_lower_brainstem', 'noise_pons_vessel', 'noise_sinus', 'noise_sup_frontal', 'noise_susceptibility', 'noise_upper_brainstem', 'noise_vent_wm', 'parietal', 'right_pf', 'sensory_motor', 'superior_mid_frontal', 'visual']
nsamples = 2

#trg map is the IC that we are checking against
trg_map = os.path.join(DIR, 'n200', 'melodic_IC_sm6.nii.gz')
#src map is one of the bootstrap samples we are trying to match with the trg
src_map = os.path.join(DIR, 'sample.1.melodic_test', 'melodic_IC.nii.gz')

#for thresholding the IC maps....they are Z maps
z = 1.96

#make a function -- two args are the trg and src maps
def compute_ui(trg_map, src_map):
	#read in the nifti data for the target (template components) and the source (the experimental set that needs matching)
	#trg_nii = 
	#src_nii = 
	#pull out the data array
	trg_data = nb.load(trg_map).get_data()
	src_data = nb.load(src_map).get_data()
	#make an empty array to store the union over intersection values
	#this is trg# of components x src# of components
	ui = np.zeros([trg_data.shape[3], src_data.shape[3]])
	#scc = np.zeros([trg_data.shape[3], src_data.shape[3]])
	#tdis = np.zeros([trg_data.shape[3], src_data.shape[3]])
	#loop through the trg components, and the src components
	for c_trg in range(0, trg_data.shape[3]):
		#print 'checking component: ', c_trg
		for c_src in range(0, src_data.shape[3]):
			#first threshold to get the positive values in both maps
			trg_mask_pos = trg_data[:,:,:,c_trg] >= z
			src_mask_pos = src_data[:,:,:,c_src] >= z
			#next identify the negative values
			#trg_mask_neg = trg_data[:,:,:,c_trg] <= -(z)
			#src_mask_neg = src_data[:,:,:,c_src] <= -(z)
			#find the intersection of the positive map
			intersect_pos = np.sum((trg_mask_pos.astype(int) + src_mask_pos.astype(int)) >=2)
			#find the union of the positive map
			union_pos = np.sum(trg_mask_pos.astype(int)) + np.sum(src_mask_pos.astype(int)) - intersect_pos
			#same for the negative maps
			#intersect_neg = np.sum((trg_mask_neg.astype(int) + src_mask_neg.astype(int)) >=2)
			#union_neg = np.sum(trg_mask_neg.astype(int)) + np.sum(src_mask_neg.astype(int)) - intersect_neg
			#now, sum the pos/neg union/intersects
			#intersect = intersect_pos + intersect_neg
			#union = union_pos + union_neg
			intersect = intersect_pos
			union = union_pos
			#dump the union over intersection into the array with the coordinates that correspond to which component matches
			ui[c_trg, c_src] = float(intersect)/float(union)
			#scc[c_trg, c_src] = pr(trg_data[:,:,:,c_trg].ravel(), src_data[:,:,:,c_src].ravel())[0]
			#tdis[c_trg, c_src] = rogerstanimoto(trg_mask_pos.ravel(), src_mask_pos.ravel())
	#make an empty matrix to store the matches
	matched_components = np.zeros([16,16])
	#now iterate through each target component, and find the max U/I...this is your match
	for i in range(0, trg_data.shape[3]):
		#print 'Target component: ',  i, ' Source Component: ', np.argmax(ui[i]), np.argmax(scc[i]), np.argmin(tdis[i]), np.max(ui[i]), np.max(scc[i]), np.min(tdis[i])
		print 'Target component: ',  i, ' Source Component: ', np.argmax(ui[i]), np.max(ui[i])
        matched_components[i][np.argmax(ui[i])] += 1
		#matched_components[i][np.argmax(scc[i])] += 1
		#matched_components[i][np.argmax(tdis[i])] += 1
	return matched_components






for sample in range(0, nsamples):
	src_map = os.path.join(DIR, 'sample.' + str(sample) + '.melodic_samples_d16_initial', 'melodic_IC.nii.gz')
	for template in templates:
		print template
		trg_map = os.path.join(DIR, 'templates', template + '_merged.nii.gz')
		matched_components = compute_ui(trg_map, src_map)

#run the function on the sample target and source maps defined above
















###in case the masking is needed, this preserves the values within the images...doesn't switch to bools
#set the z threshold for the positive and negative ranges
#trg_mask_pos = np.invert(trg_data[:,:,:,0] >= z)
#src_mask_pos = np.invert(src_data[:,:,:,0] >= z)
#trg_mask_neg = np.invert(trg_data[:,:,:,0] <= -(z))
#mask the arrays
#trg_data_masked_pos = np.ma.masked_array(trg_data[:,:,:,0], trg_mask_pos)
#src_data_masked_pos = np.ma.masked_array(src_data[:,:,:,0], src_mask_pos)
#trg_data_masked_neg = np.ma.masked_array(trg_data[:,:,:,0], trg_mask_neg)
