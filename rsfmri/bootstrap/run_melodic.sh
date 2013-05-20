#!/bin/bash

sample=${1}

sample_sfix=melodic_test
ndims=16
tr=2.0

src=${HOME}/data/rsfmri/melodic_bootstrap_test/sample.${sample}.${sample_sfix}
trg=${TMPDIR}/rmuetzel/rsfmri/melodic_bootstrap_test/sample.${sample}.${sample_sfix}

if [ ! -d $trg ] ; then
	mkdir -p $trg
fi

rsync -rtvz ${src}/ ${trg}/

export FSLDIR=/home/muetzel/software/fsl-4.1.9
source $FSLDIR/etc/fslconf/fsl.sh

${FSLDIR}/bin/melodic --in=${trg}/sample.${sample} --outdir=${trg} --dim=${ndims} --tr=${tr} --approach=concat --nobet --bgthreshold=10

rsync -rtvz ${trg}/ ${src}/

