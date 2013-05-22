#!/bin/bash

idc=${1}

if [ ! -d $TMPDIR/rmuetzel/rsfmri ] ; then
	mkdir -p $TMPDIR/rmuetzel/rsfmri
fi

rsync -rtvzL /home/genr/data/rsfmri/${idc} $TMPDIR/rmuetzel/rsfmri/

python /home/genr/software/bitbucket/lisa/rsfmri/bootstrap/mk_fsf_files.py -f $TMPDIR/rmuetzel/rsfmri -m /home/genr/software/fsl/data/standard/MNI152_T1_2mm_brain.nii.gz -s ${idc}

export FSLDIR=/home/muetzel/software/fsl-4.1.9
source $FSLDIR/etc/fslconf/fsl.sh

featdir_sfix=22May2013.feat

${FSLDIR}/bin/feat $TMPDIR/rmuetzel/rsfmri/${idc}/idc_${idc}_${featdir_sfix}.fsf

$FSLDIR/bin/flirt -in $TMPDIR/$idc/${idc}_${featdir_sfix}/filtered_func_data -ref $TMPDIR/$idc/${idc}_${featdir_sfix}/reg/standard -out $TMPDIR/$idc/${idc}_${featdir_sfix}/filtered_func_data_2_standard -dof 12 -applyxfm -init $TMPDIR/$idc/${idc}_${featdir_sfix}/reg/example_func2standard.mat

rsync -rtvz $TMPDIR/rmuetzel/rsfmri/${idc}/ /home/genr/data/rsfmri/${idc}/
