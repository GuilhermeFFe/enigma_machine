from .rotor import Rotors

class Machine:
    def __init__(self):
        self._rotors = Rotors( )

    def type(self, c: str) -> str:
        if len(c) != 1:
            raise Exception('Enigma can receive single-characters only.')
        if not c.isalpha():
            raise Exception('Enigma can receive alphabetic characters only.')

        return self._rotors.pass_through( c )
        
    