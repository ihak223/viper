import abc


class Cipher(abc.ABC):
    @abc.abstractmethod
    def decrypt(self, index, data):
        pass


class CeasarShift(Cipher):
    def decrypt(self, index, data):
        key = index + 1
        message = data.upper()
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""

        for letter in message:
            if letter in alpha:  # if the letter is actually a letter
                # find the corresponding ciphertext letter in the alphabet
                letter_index = (alpha.find(letter) - key) % len(alpha)

                result = result + alpha[letter_index]
            else:
                result = result + letter

        return result
