"""
motors
"""

__all__ = """
    m1 m2 m3 m4 m5 m6 m7 m8
    m9 m10 m11 m12 m13 m14 m15 m16
""".split()
    # m1 m2 m3 m4
    # tth th chi phi

from ..session_logs import logger

logger.info(__file__)

from ophyd import EpicsMotor
from ophyd.sim import SynAxis

m1 = EpicsMotor("100idWYM:m1", name="m1", labels=("motor",))
m2 = EpicsMotor("100idWYM:m2", name="m2", labels=("motor",))
m3 = EpicsMotor("100idWYM:m3", name="m3", labels=("motor",))
m4 = EpicsMotor("100idWYM:m4", name="m4", labels=("motor",))
m5 = EpicsMotor("100idWYM:m5", name="m5", labels=("motor",))
m6 = EpicsMotor("100idWYM:m6", name="m6", labels=("motor",))
m7 = EpicsMotor("100idWYM:m7", name="m7", labels=("motor",))
m8 = EpicsMotor("100idWYM:m8", name="m8", labels=("motor",))
m9 = EpicsMotor("100idWYM:m9", name="m9", labels=("motor",))
m10 = EpicsMotor("100idWYM:m10", name="m10", labels=("motor",))
m11 = EpicsMotor("100idWYM:m11", name="m11", labels=("motor",))
m12 = EpicsMotor("100idWYM:m12", name="m12", labels=("motor",))
m13 = EpicsMotor("100idWYM:m13", name="m13", labels=("motor",))
m14 = EpicsMotor("100idWYM:m14", name="m14", labels=("motor",))
m15 = EpicsMotor("100idWYM:m15", name="m15", labels=("motor",))
m16 = EpicsMotor("100idWYM:m16", name="m16", labels=("motor",))

# can limits be set through kwargs?
# sm1 = SynAxis('sm1', readback_func=None, value=0, delay=0, precision=3, parent=None, labels=("motor",), kind=None)
# sm2 = SynAxis('sm2', readback_func=None, value=0, delay=0, precision=3, parent=None, labels=("motor",), kind=None)
# sm3 = SynAxis('sm3', readback_func=None, value=0, delay=0, precision=3, parent=None, labels=("motor",), kind=None)
# sm4 = SynAxis('sm4', readback_func=None, value=0, delay=0, precision=3, parent=None, labels=("motor",), kind=None)
# sm5 = SynAxis('sm5', readback_func=None, value=0, delay=0, precision=3, parent=None, labels=("motor",), kind=None)
# sm6 = SynAxis('sm6', readback_func=None, value=0, delay=0, precision=3, parent=None, labels=("motor",), kind=None)
# sm7 = SynAxis('sm7', readback_func=None, value=0, delay=0, precision=3, parent=None, labels=("motor",), kind=None)
# sm8 = SynAxis('sm8', readback_func=None, value=0, delay=0, precision=3, parent=None, labels=("motor",), kind=None)
# sm9 = SynAxis('sm9', readback_func=None, value=0, delay=0, precision=3, parent=None, labels=("motor",), kind=None)
# sm10 = SynAxis('sm10', readback_func=None, value=0, delay=0, precision=3, parent=None, labels=("motor",), kind=None)
# sm11 = SynAxis('sm11', readback_func=None, value=0, delay=0, precision=3, parent=None, labels=("motor",), kind=None)
# sm12 = SynAxis('sm12', readback_func=None, value=0, delay=0, precision=3, parent=None, labels=("motor",), kind=None)
