from abc import ABCMeta, abstractmethod

class IEncoder(object):
    """
    Abstract class defning encoder interface.
    """
    
    @abstractmethod
    def encode(self, value): pass
    
    @abstractmethod
    def decode(self): pass