"""
Simulated detector
"""

from ..session_logs import logger

logger.info(__file__)

class LocalSimDetector():
	"""
	stuff
	"""
	_default_configuration_attrs = ('roi1', 'roi2', 'roi3', 'roi4')
	_default_read_attrs = ('cam', 'file', 'stats1', 'stats2', 'stats3',
						   'stats4')
