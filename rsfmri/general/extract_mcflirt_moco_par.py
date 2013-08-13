import os as os
import csv as csv
import numpy as np
import math as math
import argparse as argparse

#First parse the command-line arguments that we need.
#set up the parser
parser = argparse.ArgumentParser(description='Parse MCFLIRT moco files to extract information')
#add the args you want parsed
parser.add_argument("-f", "--feat_dir", help="Location of subject's feat folders", required=True, nargs=1)
parser.add_argument("--maxtra", help="maximum amount of translations (in mm)",  required=False, nargs=1)
parser.add_argument("--maxrot", help="maximum amount of rotation (in degrees)",  required=False, nargs=1)
#parser.add_argument("--genr", help="assume the outdir, nifti pfix and sfix are ordered in a certain way", required=False, action="store_true")
#parse the args
args = parser.parse_args()

if args.maxtra:
	maxtra = args.maxtra[0]
else:
	maxtra = 3
if args.maxrot:
	maxrot = args.maxrot[0]
else:
	maxrot = 3
feat_dir = args.feat_dir[0]

print "Maximum translation: ", maxtra
print "Maximum rotation: ", maxrot

par = 6

excl_dict = {}

mcDir = os.path.join(feat_dir, 'mc')
if not os.path.isdir(mcDir):
	print 'No_Feat_DIR'
	sys.exit(0)
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
parFile.close()
trs = len(data_list)
#if len(data_list) == trs:
mc_pars = np.zeros(shape=(trs, par))
for i in range(0, len(data_list)):
	for j in range(0, 6):
		mc_pars[i] = data_list[i]
if math.degrees(np.max(mc_pars[:,0])) > maxrot:
	if not excl_dict.has_key(feat_dir):
		excl_dict[feat_dir] = [math.degrees(np.max(mc_pars[:,0])), 'xrot']
if math.degrees(np.max(mc_pars[:,1])) > maxrot:
	if not excl_dict.has_key(feat_dir):
		excl_dict[feat_dir] = [math.degrees(np.max(mc_pars[:,1])), 'yrot']
if math.degrees(np.max(mc_pars[:,2])) > maxrot:
	if not excl_dict.has_key(feat_dir):
		excl_dict[feat_dir] = [math.degrees(np.max(mc_pars[:,2])), 'zrot']
if np.max(mc_pars[:,3]) > maxtra:
	if not excl_dict.has_key(feat_dir):
		excl_dict[feat_dir] = [np.max(mc_pars[:,3]), 'xtrans']
if np.max(mc_pars[:,4]) > maxtra:
	if not excl_dict.has_key(feat_dir):
		excl_dict[feat_dir] = [np.max(mc_pars[:,4]), 'ytrans']
if np.max(mc_pars[:,5]) > maxtra:
	if not excl_dict.has_key(feat_dir):
		excl_dict[feat_dir] = [np.max(mc_pars[:,5]), 'ytrans']		

if excl_dict.has_key(feat_dir):
	print True
			
#print 'Max X rotation (rad, deg): ', np.max(mc_pars[:,0]), math.degrees(np.max(mc_pars[:,0]))
#print 'Max Y rotation (rad, deg): ', np.max(mc_pars[:,1]), math.degrees(np.max(mc_pars[:,1]))
#print 'Max Z rotation (rad, deg): ', np.max(mc_pars[:,2]), math.degrees(np.max(mc_pars[:,2]))
#print 'Max X translation (mm): ', np.max(mc_pars[:,3])
#print 'Max Y translation (mm): ', np.max(mc_pars[:,4])
#print 'Max Z translation (mm): ', np.max(mc_pars[:,5])