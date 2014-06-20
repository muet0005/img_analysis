# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.slicer.filtering.morphology import GrayscaleFillHoleImageFilter

def test_GrayscaleFillHoleImageFilter_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputVolume=dict(argstr='%s',
    position=-2,
    ),
    outputVolume=dict(argstr='%s',
    hash_files=False,
    position=-1,
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    )
    inputs = GrayscaleFillHoleImageFilter.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_GrayscaleFillHoleImageFilter_outputs():
    output_map = dict(outputVolume=dict(position=-1,
    ),
    )
    outputs = GrayscaleFillHoleImageFilter.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
