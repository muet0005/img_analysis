import os as os
import shutil as shutil

DIR = '/home/genr/tracula'
dtroot = os.path.join(DIR, 'dti')
subjects_dir = os.path.join(DIR, 'freesurfer')

scratch = 'rmuetzel/tracula/'
scratchdt = scratch + 'dti'
scratchfs = scratch + 'freesurfer'



idc_list = []
idcs = os.listdir(dtroot)
for idc in idcs:
	if os.path.exists(os.path.join(dtroot, str(idc), 'dti_idc_' + str(idc) + '.bvec')) and not os.path.exists(os.path.join(dtroot, idc, 'dpath')):
		idc_list.append(idc)


iters = int(len(idc_list)/6.0)
indv_subs = len(idc_list)-int(len(idc_list)/6.0)*6
print 'Found: ', len(idc_list), ' IDCs for processing'
print 'Need: ', iters, ' iterations for processing'
print 'Need to process the last: ', indv_subs, ' subjects individually'


tractypes = ['prep', 'bedp', 'path']
for tractype in tractypes:
	queue = os.path.join(DIR, 'queue_' + tractype)
	if os.path.exists(queue):
		shutil.rmtree(queue)
	os.makedirs(queue)
	
	f = os.path.join(queue, 'run_iters_' + str(iters) + '_indivsub_' + str(indv_subs) + '.pbs')
	run_pbs = open(f, 'w')
	os.chmod(f, 0750)
	run_pbs.write('#PBS -lwalltime=24:00:00' + '\n')
	run_pbs.write('#PBS -lnodes=1:cores8:ppn=6' + '\n' + '\n')
	run_pbs.write('dtroot=' + dtroot + '\n')
	run_pbs.write('queue=' + queue + '\n')
	run_pbs.write('idcs=(')
	for idc in idc_list:
		run_pbs.write(idc + ' ')
	run_pbs.write(')' + '\n')
	run_pbs.write('num_cores=6' + '\n')
	run_pbs.write('num_sub=0' + '\n')
	#run_pbs.write('n=$[($RANDOM % 5) + 1]' + '\n')
	#run_pbs.write('sleep ${n}' + '\n')
	run_pbs.write('sleep ${PBS_ARRAYID}' + '\n')
	run_pbs.write('echo PBSARRAYID ${PBS_ARRAYID}' + '\n')
	run_pbs.write('if [ ! -d ${dtroot}/' + tractype + '_queue_control ] ; then' + '\n')
	run_pbs.write('\t' + 'mkdir ${dtroot}/' + tractype + '_queue_control' + '\n')
	run_pbs.write('fi' + '\n')
	run_pbs.write('for idc in ${idcs[*]} ; do' + '\n')
	run_pbs.write('\t' + 'if [ ! -e ${dtroot}/' + tractype + '_queue_control/${idc}.isrunning -a ${num_sub} -lt ${num_cores} ] ; then' + '\n')
	run_pbs.write('\t' + '\t' + 'let num_sub=\"${num_sub}+1\"' + '\n')
	run_pbs.write('\t' + '\t' + 'touch ${dtroot}/' + tractype + '_queue_control/${idc}.isrunning' + '\n')
	run_pbs.write('\t' + '\t' + 'echo ${dtroot}/' + tractype + '_queue_control/${idc}.isrunning' + '\n')
	run_pbs.write('\t' + '\t' + '${queue}/run ${idc} &' '\n')
	#run_pbs.write('\t' + '\t' + 'sleep ${n}' + '\n')
	run_pbs.write('\t' + 'else' + '\n')
	run_pbs.write('\t' + '\t' + 'continue' + '\n')
	run_pbs.write('\t' + 'fi' + '\n')
	run_pbs.write('done' + '\n')
	run_pbs.write('wait')
	run_pbs.close()




for tractype in tractypes:
	queue = os.path.join(DIR, 'queue_' + tractype)
	f = os.path.join(queue, 'run')
	run = open(f, 'w')
	os.chmod(f, 0750)
	run.write('#!/bin/bash' +'\n')
	run.write('idc=${1}' + '\n')
	run.write('if [ ! -d $TMPDIR/' + scratchdt + ' ] ; then' + '\n')
	run.write('\t' + 'mkdir -p $TMPDIR/' + scratchdt + '\n')
	run.write('fi' + '\n')
	run.write('if [ ! -d $TMPDIR/' + scratchfs + ' ] ; then' + '\n')
	run.write('\t' + 'mkdir -p $TMPDIR/' + scratchfs + '\n')
	run.write('fi' + '\n' + '\n')
	run.write('rsync -rtvzL ' + dtroot + '/${idc} $TMPDIR/' + scratchdt + '/'+ '\n')
	run.write('rsync -rtvzL ' + subjects_dir + '/${idc} $TMPDIR/' + scratchfs + '/' + '\n')
	if tractype == 'prep':
		run.write('/home/muetzel/scripts/tracula/prep_raw_dti_4_tracula.sh $TMPDIR/' + scratchdt + ' ${idc}' + '\n')
	run.write('python /home/muetzel/scripts/tracula/mk_tracula_cfg.py $TMPDIR/' + scratchfs + ' $TMPDIR/' + scratchdt + ' ' + '${idc}' + ' $TMPDIR/' + scratchdt + '/${idc}/${idc}.trc.cfg' + '\n')
	run.write('export FSLDIR=/home/muetzel/software/fsl-4.1.9' + '\n')
	run.write('source $FSLDIR/etc/fslconf/fsl.sh' + '\n')
	run.write('export SUBJECTS_DIR=$TMPDIR/' + scratchfs + '\n')
	run.write('module load freesurfer/5.1.0' + '\n')
	run.write('/home/muetzel/scripts/tracula/trac-all-rlm.new -c $TMPDIR/' + scratchdt + '/${idc}/${idc}.trc.cfg -' + tractype + '\n')
	run.write('rsync -rtvz $TMPDIR/' + scratchdt + '/${idc}/ ' + dtroot + '/${idc}/' + '\n')
	
