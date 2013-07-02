import os as os
import csv as csv
import numpy as np
import math as math

DIR = '/Volumes/mr_data_idc/feb2013_datalock/rfmri'
DIR = '/home/genr/data/rsfmri'
subjs = os.listdir(DIR)

sfix = '_22May2013.feat'

trs = 157
par = 6

excl_dict = {}

for subj in subjs:
	mcDir = os.path.join(DIR, subj, subj + sfix, 'mc')
	if not os.path.isdir(mcDir):
		continue
	print subj
	parFile = open(os.path.join(mcDir, 'prefiltered_func_data_mcf.par'), 'r')
	csv_parFile = csv.reader(parFile, delimiter=' ')
	data_list = []
	for line in csv_parFile:
		rmWS = True
		while rmWS:
			try:
				line.remove('')
			except:
				rmWS = False
		data_list.append(line)
	if len(data_list) == trs:
		mc_pars = np.zeros(shape=(trs, par))
		for i in range(0, len(data_list)):
			for j in range(0, 6):
				mc_pars[i] = data_list[i]
		if math.degrees(np.max(mc_pars[:,0])) > 3:
			if not excl_dict.has_key(subj):
				excl_dict[subj] = [math.degrees(np.max(mc_pars[:,0])), 'xrot']
		if math.degrees(np.max(mc_pars[:,1])) > 3:
			if not excl_dict.has_key(subj):
				excl_dict[subj] = [math.degrees(np.max(mc_pars[:,1])), 'yrot']
		if math.degrees(np.max(mc_pars[:,2])) > 3:
			if not excl_dict.has_key(subj):
				excl_dict[subj] = [math.degrees(np.max(mc_pars[:,2])), 'zrot']
		if np.max(mc_pars[:,3]) > 3:
			if not excl_dict.has_key(subj):
				excl_dict[subj] = [np.max(mc_pars[:,3]), 'xtrans']
		if np.max(mc_pars[:,4]) > 3:
			if not excl_dict.has_key(subj):
				excl_dict[subj] = [np.max(mc_pars[:,4]), 'ytrans']
		if np.max(mc_pars[:,5]) > 3:
			if not excl_dict.has_key(subj):
				excl_dict[subj] = [np.max(mc_pars[:,5]), 'ytrans']		
	#print excl_dict
print 'Found: ', len(excl_dict), ' cases that exceeded the motion criteria'
			
#print 'Max X rotation (rad, deg): ', np.max(mc_pars[:,0]), math.degrees(np.max(mc_pars[:,0]))
#print 'Max Y rotation (rad, deg): ', np.max(mc_pars[:,1]), math.degrees(np.max(mc_pars[:,1]))
#print 'Max Z rotation (rad, deg): ', np.max(mc_pars[:,2]), math.degrees(np.max(mc_pars[:,2]))
#print 'Max X translation (mm): ', np.max(mc_pars[:,3])
#print 'Max Y translation (mm): ', np.max(mc_pars[:,4])
#print 'Max Z translation (mm): ', np.max(mc_pars[:,5])