import pyNN.nest as sim
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

logger.info('Starting script.')

sim.setup(timestep=0.1, min_delay=0.1, max_delay=1.0)

cell_params = {}
pop1 = sim.Population(10, sim.IF_cond_alpha, cell_params)
pop2 = sim.Population(20, sim.IF_cond_alpha, cell_params)

pop1.record_v(to_file=False)

sim.run(1000)

spikes = pop1.getSpikes()

print(spikes.)
