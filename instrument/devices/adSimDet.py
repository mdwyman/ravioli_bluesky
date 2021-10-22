"""
Simulated detector
"""

from ophyd.areadetector import SimDetector, SimDetectorCam, SingleTrigger
from ophyd.areadetector.plugins import (
	StatsPlugin,
	ImagePlugin,
	ROIPlugin,
	HDF5Plugin,
	ProcessPlugin,
)
from ophyd.areadetector.filestore_mixins import FileStoreHDF5IterativeWrite
from ophyd import Component


from ..session_logs import logger

logger.info(__file__)

class HDF5PluginWithFileStore(HDF5Plugin, FileStoreHDF5IterativeWrite):
	pass

class LocalSimDetector(SingleTrigger, SimDetector):
	
	_default_configuration_attrs = ('roi1', 'roi2', 'roi3', 'roi4')
	_default_read_attrs = ('cam', 'file', 'stats1', 'stats2', 'stats3', 'stats4')
	
	image = Component(ImagePlugin, 'image1:')
	cam = Component(SimDetectorCam, 'cam1:')
	transform_type = 0
	hdf5 = Component(HDF5PluginWithFileStore, 'HDF1:',
			 write_path_template='/home/beams/MWYMAN/data',
			 read_path_template='/home/beams/MWYMAN/images',
			 read_attrs=[],
			 root='/')
	stats1 = Component(StatsPlugin, 'Stats1:')
	stats2 = Component(StatsPlugin, 'Stats2:')
	stats3 = Component(StatsPlugin, 'Stats3:')
	stats4 = Component(StatsPlugin, 'Stats4:')
	stats5 = Component(StatsPlugin, 'Stats5:')
	roi1 = Component(ROIPlugin, 'ROI1:')
	roi2 = Component(ROIPlugin, 'ROI2:')
	roi3 = Component(ROIPlugin, 'ROI3:')
	roi4 = Component(ROIPlugin, 'ROI4:')
	proc1 = Component(ProcessPlugin, 'Proc1:')
