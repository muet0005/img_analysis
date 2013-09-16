#!/bin/bash

sample=${1}

sample_sfix=d16
ndims=16
tr=2.0

src=${HOME}/data/rsfmri/melodic_melodic_component_matching_d16/sample.${sample}.${sample_sfix}
trg=${TMPDIR}/rmuetzel/rsfmri/melodic_melodic_component_matching_d16/sample.${sample}.${sample_sfix}

if [ ! -d $trg ] ; then
	mkdir -p $trg
fi

rsync -rtvz ${src}/ ${trg}/

export FSLDIR=/home/genr/software/fsl/5.0.4
source $FSLDIR/etc/fslconf/fsl.sh

${FSLDIR}/bin/melodic --in=${trg}/sample.${sample} --outdir=${trg} --dim=${ndims} --tr=${tr} --approach=concat --nobet --bgthreshold=10 --mask=$FSLDIR/data/custom/knicr130_t1_2mm_brain_mask.nii.gz

rsync -rtvz ${trg}/ ${src}/

