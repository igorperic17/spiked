
import nest
import pdb

class MemoryBuilder:

	# defaults
	syn_local_inh = {
		#'model' : 'tsodyks_synapse',
		#'tau_rec' : 1000.0, # recovery time
		#'tau_psc' : 100.0, # ?
		'delay' : 1.0,
		'weight': -1000.0
	}
	syn_prox_in = {
		'delay' : 1.0,
		'weight' : 100.0
	}
	syn_basal_in = {
		'model' : 'stdp_synapse',
		'delay' : 1.0,
		'weight' : 10.0
	}
	column_neuron_params = { 
		'V_th' : -61.0, 
		't_ref' : 1.0,
		'tau_m' : 10.0
	}
	
	I_e_OFF = 0.0
	I_e_ON = 1e4
	def __init__(self):
		pass

	@classmethod
	def InitMemoryUnit(self):
		nest.ResetKernel()

	@classmethod
	def CreateColumn(self, numOfCells, localInhibitionRadius=0):

		column = nest.Create('iaf_neuron', numOfCells, params = self.column_neuron_params)

		for neuron in column:
			nest.Connect([neuron], column, syn_spec = self.syn_local_inh)
		return column

	@classmethod
	def ConnectProximalDendrite(self, column, in_neuron=None):

		if in_neuron is None:
			in_neuron = nest.Create('iaf_neuron', params = {'I_e' : self.I_e_OFF})
		nest.Connect(in_neuron, column, 'all_to_all', syn_spec = self.syn_prox_in)
		return in_neuron

	@classmethod
	def ConnectBasalDendrite(self, neuron, in_neuron=None):
		if in_neuron is None:
			in_neuron = nest.Create('iaf_neuron', params = {'I_e' : self.I_e_OFF})
		
		#pdb.set_trace()
		nest.Connect(in_neuron, [neuron], 'all_to_all', self.syn_basal_in)
		return in_neuron

	@classmethod
	def SetProximalInput(self, neuron, val):
		v = self.I_e_OFF
		if val is True:
			v = self.I_e_ON
		nest.SetStatus(neuron, params = {'I_e' : v})

	############## RECORDING #################

	@classmethod
	def RecordColumnVoltages(self, column):
		vd = nest.Create('multimeter', len(column), params={'record_from': ['V_m'], 'interval' :0.1})

		# pdb.set_trace()
		nest.Connect(vd, column, 'one_to_one')
		return vd

	@classmethod
	def RecordColumnSpikes(self, column):
		sd = nest.Create('spike_detector', len(column))
		nest.Connect(column, sd, 'one_to_one')
		return sd

	@classmethod
	def FetchColumnEvents(self, sd):
		spikes = nest.GetStatus(sd, 'events')
		return spikes

	############## LAYERS (UNITS) #################

	@classmethod
	def CreateUnit(self, 
		numOfColumns,
		cellsPerColumn, 
		localInhibitionRadius=0,
		localConnectivityRadius=0):
		
		unit = []
		# create columns
		for i in range(numOfColumns):
			c = self.CreateColumn(cellsPerColumn)
			unit.append(c)
			# connect neighboring columns
			for k in range(-localConnectivityRadius, 1, 1):
				idx = i + k # index of column to connect to
				print(idx)
				if idx < 0:
					continue 
				# connect every cell to every other cell
				for p in range(cellsPerColumn):
					for q in range(cellsPerColumn):
						print(p)
						print(q)
						self.ConnectBasalDendrite(unit[i][p], unit[idx][q])

		return unit


###################### ENCODERS ###################

class ScalarEncoder:

	@classmethod
	def CreateEncoderDefinition(self, size = 10, width = 1, minVal = 0, maxVal = 10):
		encoder_def = {
			'size' : size,
			'width' : width,
			'minVal' : minVal,
			'maxVal' : maxVal 
		}
		return encoder_def

	@classmethod
	def CreateEncoderPopulation(self, encoder_def):
		encoder_pop = nest.Create('iaf_neuron', encoder_def['size'])
		return encoder_pop

	@classmethod
	def CreateEncoder(self, size = 10, width = 1, minVal = 0, maxVal = 10):
		enc_def = CreateEncoderDefinition(size, width, minVal, maxVal)
		enc_pop = CreateEncoderPopulation(enc_def)
		return enc_pop

	@classmethod
	def Encode(self, encoder_def, val_to_encode):
		pass