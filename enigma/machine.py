from .rotor import Rotors
from .plug_board import PlugBoard

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Machine:
    def __init__(self):
        self._rotors = Rotors()
        self._plug_board = PlugBoard()

    def type(self, c: str) -> str:
        if len(c) != 1:
            raise Exception('Enigma can receive single-characters only.')
        if not c.isalpha():
            raise Exception('Enigma can receive alphabetic characters only.')

        return self._run_char(self.char_to_number(c.upper()))
    
    def _run_char(self, c: int) -> str:
        char = self._plug_board.pass_through(c)
        char = self._rotors.pass_through(char)
        char = self._plug_board.pass_through(char)
        return self.number_to_char(char)
    
    def char_to_number(self, c: str) -> int:
        return alphabet.index(c)
    
    def number_to_char(self, c: int) -> str:
        return alphabet[c]
    