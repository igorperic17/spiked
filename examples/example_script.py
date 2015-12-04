import nest
import matplotlib.pyplot as plt

from psmu.core import MemoryBuilder

import pdb

# create a column
unit = MemoryBuilder.CreateUnit(2, 6, localConnectivityRadius=1)
col1 = unit[0]
print(col1)

# create a common proximal dendrite and dedicated input neuron
input_neuron = MemoryBuilder.ConnectProximalDendrite(col1)
basal_neuron = MemoryBuilder.ConnectBasalDendrite(col1[2])
basal_neuron2 = MemoryBuilder.ConnectBasalDendrite(col1[0])

# turn on recording of spikes for this column
sd = MemoryBuilder.RecordColumnSpikes(col1)
vd = MemoryBuilder.RecordColumnVoltages(col1)

# prepare plotting
#plt.ion()
plt.figure()
plt.ioff()

# run loop
for i in range(100):
	plt.clf()

	if i > 10:
		MemoryBuilder.SetProximalInput(basal_neuron, True)

	if i > 15:
		MemoryBuilder.SetProximalInput(input_neuron, True)

	if i > 30:
		MemoryBuilder.SetProximalInput(basal_neuron, False)
		MemoryBuilder.SetProximalInput(basal_neuron2, True)

	if i > 40:
		MemoryBuilder.SetProximalInput(basal_neuron2, False)

	column_spikes = MemoryBuilder.FetchColumnEvents(sd)
	column_v = MemoryBuilder.FetchColumnEvents(vd)
		
	nest.Simulate(10)


plt1 = plt.subplot(1, 2, 1)
for i in range(len(column_v)):
	pass
	plt1.plot(column_v[i]['times'], column_v[i]['V_m'])

plt2 = plt.subplot(1, 2, 2)
for i in range(len(sd)):
	for spike in column_spikes[i]['times']: 
		plt2.scatter(spike, sd[i]) 
plt.show()
