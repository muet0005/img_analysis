#!/bin/bash

DIR=/home/genr/data/randomise_tests
ic=dr_stage2_merged_pe_ic0003
statroot=design_mainfx
oDIR=/global/rmuetzel/randomise/${ic}_${statroot}

seed=${1}
nperms=${2}

#make sure a seed is passed
#make sure number of permutations is passed
if [ $# != 2 ] ; then
    echo "Must supply the seed number and number of permutations for randomise..."
    exit
fi
#make they are integers
if [[ $seed != *[!0-9]* ]]; then
    echo "seed is: " ${seed}
else
    echo "Seed is not an integer...please enter a valid seed."
    exit
fi
if [[ $nperms != *[!0-9]* ]]; then
    echo "number of permutations is: " ${nperms}
else
    echo "number of permutations is not an integer...please enter a valid seed."
    exit
fi

#set up fsl
export FSLDIR=/home/genr/software/fsl/5.0.5
source $FSLDIR/etc/fslconf/fsl.sh
export PATH=${PATH}:${FSLDIR}/bin

if [ ! -d $oDIR ] ; then
	mkdir -p $oDIR/parallel
fi

echo "**************COPYING TO SCRATCH SPACE***************"
echo "cp -r ${DIR}/${icroot}${ic}.nii.gz ${oDIR}/"
echo "cp -r ${DIR}/mask.nii.gz ${oDIR}/"
echo "cp -r ${DIR}/${statroot}.* ${oDIR}/"
cp -r ${DIR}/${icroot}${ic}.nii.gz ${oDIR}/
cp -r ${DIR}/mask.nii.gz ${oDIR}/
cp -r ${DIR}/${statroot}.* ${oDIR}/
echo "**************FINISHED COPYING TO SCRATCH SPACE***************"

python $DIR/randomise_parallel.py -i ${oDIR}/${ic}.nii.gz --dir ${oDIR} -d ${oDIR}/${statroot}.mat -t ${oDIR}/${statroot}.con -o ${ic}_${statroot} --T --glm --nperm ${nperm}

echo "**************COPYING TO HOME DIRECTORY***************"
echo "cp -r ${oDIR} ${DIR}/"
cp -r ${oDIR} ${DIR}/