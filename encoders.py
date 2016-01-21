
import pyNN.nest as sim
import pdb

class ScalarEncoder:
	@classmethod
	def CreateEncoderDefinition(self, size = 10, width = 1, minVal = 0, maxVal = 10):
		"
		Docstring for create encoder definition.
		"

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
