"""
Detector loading functions
"""

__all__ = """
    loadSimDet
    loadShadowDet
""".split()

from ..devices.adSimDet import LocalSimDetector
from ..devices.shadowDet import ShadowDetector

def loadSimDet(prefix="100idWYM:simDet:"):
	print("-- Loading AD simulated Detector")
#	simDet= LocalSimDetector(name="simDet", prefix=prefix, read_attrs=["hdf5", "stats1", "stats5"])
	simDet= LocalSimDetector(name="simDet", prefix=prefix, read_attrs=["stats1"])
	
	simDet.wait_for_connection(timeout=10)
	# This is needed otherwise .get may fail!!!
	
	print("Setting up ROI and STATS defaults ...", end=" ")
	for name in simDet.component_names:
		if "roi" in name:
			roi = getattr(simDet, name)
			roi.wait_for_connection(timeout=10)
			roi.nd_array_port.put("SIM1")
		if "stats" in name:
			stat = getattr(simDet, name)
			stat.wait_for_connection(timeout=10)
			stat.nd_array_port.put(f"ROI{stat.port_name.get()[-1]}")

	print("Done!")
	print("Setting up defaults kinds ...", end=" ")
	simDet.default_kinds()
	print("Done!")
	print("Setting up default settings ...", end=" ")
	simDet.default_settings()
	print("Done!")
	print("All done!")
	
	return simDet


def loadShadowDet():
#	shadowDet = ShadowDetector()
	shadowDet = None
	
	return shadowDet
