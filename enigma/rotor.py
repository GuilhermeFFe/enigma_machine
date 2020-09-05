from random import randint

end_rotor_wiring = (25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
rotor_wiring = (
    (15, 4, 25, 20, 14, 7, 23, 18, 2, 21, 5, 12, 19, 1, 6, 11, 17, 8, 13, 16, 9, 22, 0, 24, 3, 10),
    (25, 14, 20, 4, 18, 24, 3, 10, 5, 22, 15, 2, 8, 16, 23, 7, 12, 21, 1, 11, 6, 13, 9, 17, 0, 19),
    (4, 7, 17, 21, 23, 6, 0, 14, 1, 16, 20, 18, 8, 12, 25, 5, 11, 24, 13, 22, 10, 19, 15, 3, 9, 2),
    (8, 12, 4, 19, 2, 6, 5, 17, 0, 24, 18, 16, 1, 25, 23, 22, 11, 7, 10, 3, 21, 20, 15, 14, 9, 13),
    (16, 22, 4, 17, 19, 25, 20, 8, 14, 0, 18, 3, 5, 6, 7, 9, 10, 15, 24, 23, 2, 21, 1, 13, 12, 11),
)

class Rotors:
    class Rotor:
        def __init__(self, index: int, start: int):
            self._next = None
            self._prev = None
            self._val = start
            self._idx = index
            self._wiring = rotor_wiring[index]
            self._is_end = None
        
        def set_end_wiring(self):
            self._is_end = True
            self._wiring = end_rotor_wiring
        
        def next(self, next: 'Rotor') -> None:
            self._next = next
        
        def prev(self, prev: 'Rotor') -> None:
            self._prev = prev
        
        def pass_through(self, c: int) -> int:
            if self._is_end:
                c_in = c
            else:
                c_in = (c + self._val) % 26
            new_c = self._wiring[c_in]

            if self._next:
                return self._next.pass_through(new_c)
            else:
                return self._prev.pass_through_rev(new_c)
        
        def pass_through_rev(self, c: int) -> int:
            new_c = (self._wiring.index(c) - self._val + 26) % 26

            if self._prev:
                return self._prev.pass_through_rev(new_c)
            else:
                return new_c
        
        def increment(self) -> None:
            self._val += 1
            if self._val >= 26:
                self._val = 0
                if self._next:
                    self._next.increment()

    def __init__(self, size):
        self._rotors = [self.Rotor(0, 0), ]
        self._first = self._rotors[0]
        for _ in range(1, size):
            self._append_rotor()
        self._rotors[-1].set_end_wiring( )
    
    def _append_rotor(self) -> None:
        new_rotor = self.Rotor(len(self._rotors), 0)
        new_rotor.prev(self._rotors[-1])
        self._rotors[-1].next( new_rotor )
        self._rotors.append(new_rotor)
    
    def increment_rotor(self, by: int) -> None:
        for _ in range (by):
            self._first.increment()
    
    def pass_through(self, c: int) -> int:
        new_c = self._first.pass_through(c)
        self._first.increment()
        return new_c
