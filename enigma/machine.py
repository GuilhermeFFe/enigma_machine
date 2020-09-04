from .rotor import Rotors

class Machine:
    def __init__(self):
        self._rotors = Rotors( )

    def type(self, text: str):
        new_msg = ''
        for c in text:
            new_msg +=  self._type(c)
        return new_msg
    
    def _type(self, c: str):
        if len(c) > 1:
            return self.type(c)
        
        return self._rotors.pass_through( c )