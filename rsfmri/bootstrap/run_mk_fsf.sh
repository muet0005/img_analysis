#!/bin/bash

idc=${1}

if [ ! -d $TMPDIR/rmuetzel/rsfmri ] ; then
	mkdir -p $TMPDIR/rmuetzel/rsfmri
fi

rsync -rtvzL /home/genr/data/rsfmri/${idc} $TMPDIR/rmuetzel/rsfmri/

python /home/genr/software/rsfmri/bootstrap/mk_fsf_files.py -f $TMPDIR/rmuetzel/rsfmri -m /home/genr/software/fsl/data/standard/MNI152_T1_2mm_brain.nii.gz -s ${idc}

export FSLDIR=/home/muetzel/software/fsl-4.1.9
source $FSLDIR/etc/fslconf/fsl.sh

featdir_sfix=22May2013.feat

${FSLDIR}/bin/feat $TMPDIR/rmuetzel/rsfmri/${idc}/idc_${idc}_${featdir_sfix}.fsf

rsync -rtvz $TMPDIR/rmuetzel/rsfmri/${idc}/ /home/genr/data/rsfmri/${idc}/
