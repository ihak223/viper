import abc

class Cipher(abc.ABC):
    @abc.abstractmethod
    def decipher(self, data, index):
        pass

class CaesarShift(Cipher):
    def decipher(self, data, index):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

