__all__ = """
    create_start_population
    ga_scan
""".split()

import inspect
from itertools import chain, zip_longest
from functools import partial
import collections
from collections import defaultdict
import time

import numpy as np
try:
    # cytools is a drop-in replacement for toolz, implemented in Cython
    from cytools import partition
except ImportError:
    from toolz import partition

from bluesky import utils, plan_patterns
from bluesky.utils import Msg

from bluesky import preprocessors as bpp
from bluesky import plan_stubs as bps



def create_start_population(population_size, motor_info, mode = 'gaussian', previous_best = None):
    """
    Create starting population
    
    Parameters
    ----------
    population_size :
    motor_info : list
        list of dictionaries of 'settable' objects (motor, temp controller, etc.) containing 
        range of possible values, mean, standard deviation
    mode : method of creating population
    previous_best : used for mode = informed_gaussian

    Returns
    -------
    population : list
        list of lists of motor positions

    """


    #check that mode is valid

    

    if mode is 'gaussian':
        pass
    elif mode is 'uniform':
        pass
    elif mode is 'informed_gaussian':
        pass

    return






def ga_scan(detectors, fitness_func, ga_parameters, motors, starting_population,
            max_n_generations, fitness_minimum = None, md=None):

    """
    Scan and evolve population of positions with goal of maximizing a fitness
    function.

    Parameters
    ----------
    detectors : list
        list of 'readable' objects
    fitness_func : function
        function for determining fitness for each member of population
    ga_parameters : dictionary
        dictionary of parameters for genetic algorithm
    motors : list
        list of any 'settable' objects (motor, temp controller, etc.) whose position
        in the list corresponds to a trial setting in each population member
    starting_population : list
        list of list of trial settings
    max_n_generations : integer
        number of generations to evolve through if fitness_minimum is None
    fitness_minimum : float
        early stopping criteria for genetic algorithm
    md : dict, optional
        metadata

    See Also
    --------
    :func:`bluesky.plans.adaptive_scan`
    :func:`bluesky.plans.rel_adaptive_scan`
    """

    # Any checks?

    _md = {'detectors': [det.name for det in detectors],
           'motors': [motor.name],
           'plan_args': {'detectors': list(map(repr, detectors)),
                         'motors': repr(motors),
                         'start_population': starting_population,
                         'ga_parameters': ga_parameters,
                         'fitness_func': fitness_func.__name__,
                         'max_n_generations': max_n_generations,
                         'fitness_minimum': fitness_minimum},
           'plan_name': 'ga_scan',
           'hints': {},
           }
    _md.update(md or {})

    try:
        dimensions = [(motor.hints['fields'], 'primary')]
    except (AttributeError, KeyError):
        pass
    else:
        _md['hints'].setdefault('dimensions', dimensions)

    @bpp.stage_decorator(list(detectors) + [motor])
    @bpp.run_decorator(md=_md)
    def ga_core():
        next_pos = start
        step = (max_step - min_step) / 2
        past_I = None
        cur_I = None
        cur_det = {}
        if stop >= start:
            direction_sign = 1
        else:
            direction_sign = -1
        while next_pos * direction_sign < stop * direction_sign:
            yield Msg('checkpoint')
            yield from bps.mv(motor, next_pos)
            yield Msg('create', None, name='primary')
            for det in detectors:
                yield Msg('trigger', det, group='B')
            yield Msg('wait', None, 'B')
            for det in utils.separate_devices(detectors + [motor]):
                cur_det = yield Msg('read', det)
                if target_field in cur_det:
                    cur_I = cur_det[target_field]['value']
            yield Msg('save')

            # special case first first loop
            if past_I is None:
                past_I = cur_I
                next_pos += step * direction_sign
                continue

            dI = np.abs(cur_I - past_I)

            slope = dI / step
            if slope:
                new_step = np.clip(target_delta / slope, min_step, max_step)
            else:
                new_step = np.min([step * 1.1, max_step])

            # if we over stepped, go back and try again
            if backstep and (new_step < step * threshold):
                next_pos -= step
                step = new_step
            else:
                past_I = cur_I
                step = 0.2 * new_step + 0.8 * step
            next_pos += step * direction_sign

    return (yield from ga_core())

