"""
Implements helper functions for visualizing neuron rates of populations.
"""

from abc import ABCMeta, abstractmethod
import spiked.encoders.ScalarEncoder

class PopulationPlotter {
    """
    Abstract class for defining interface for plotter object.
    """
    __metaclass__ == ABCMeta
    
    @abstractmethod
    def plot_encoder(self, figure): pass
}

class ScalarEncoderPlotter(PopulationPlotter) {
    
    def __init__(self, population, figure):
        self.population = population
    
    def plot_encoder(self):
        """
        Plot scalar encoder output on given figure.
        """
        
        figure.plot()
}
