from spiked.encoders import ScalarEncoder
import logging
import numpy as np

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.StreamHandler())
LOG.setLevel(logging.INFO)

def test_default_params():
    """
    Checking if creating encoder with defualt values works.
    """
    encoder = ScalarEncoder.ScalarEncoder()
    LOG.info('Encoder created: {}'.format(encoder))

def test_encoder_rate_1():
    """
    Checks if encoder is properly encoding provided values.
    """

    encoder = ScalarEncoder.ScalarEncoder(
        size=10, width=1, min_val=0, max_val=10)
    encoder.encode(5.0)

    rate = encoder.population.get('rate', gather=False)
    # get index of maximum rate neuron
    idx_max = np.argmax(rate)
    LOG.info(rate)
    LOG.info('Max firing rate: {}'.format(idx_max))

    assert idx_max == 4  # indexing starts from zero

if __name__ == '__main__':

    # run tests

    test_default_params()
    test_encoder_rate_1()
    