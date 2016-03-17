from spiked.memory import Ensemble
from spiked.encoders import ScalarEncoder
import logging
import numpy as np
import pyNN.nest as sim
import nest

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.StreamHandler())
LOG.setLevel(logging.INFO)

def test_default_params():
    """
    Checking if creating encoder with defualt values works.
    """
    
    # reset the simulator
    nest.reset()
    
    ensemble = Ensemble.Ensemble()
    LOG.info('Ensemble created: {}'.format(ensemble))


def test_squaring():
    """
    Test adding two values using neural substrate works.
    """
    
    LOG.info('Running squaring test...')
    
    # reset the simulator
    sim.reset()
    
    # create input Encoder
    input = ScalarEncoder.ScalarEncoder()
    input.encode(5)
    
    # create decoder
    output = ScalarEncoder.ScalarEncoder()
    output.encode(7)
    
    # creating ensemble
    ensemble = Ensemble.Ensemble(input, output, ensemble_size=200)
    ensemble.Train()
    
    LOG.info('Test complete.')


if __name__ == '__main__':
    
    # setup the simulator
    sim.setup()

    # run tests
    test_squaring()