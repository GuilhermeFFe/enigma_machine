class PlugBoard:
    class Plug:
        def __init__(self, a: int, b: int):
            if a == b:
                raise Exception('Plug cant connect to itself')
            self._connection = {a: b, b: a}
        def __getitem__(self, idx: int) -> int:
            return self._connection.get(c, c)

    def __init__(self):
        self._plugs = []
    
    def add_plug(self, a: int, b: int) -> None:
        _a = self.pass_through(a)
        _b = self.pass_through(b)
        if _a == b or _a == a or _b == b or _b == _a:
            raise Exception('Cant connect plug on char that is already connected')
        self._plugs.append(self.Plug(a, b))

    def pass_through(self, c: int) -> str:
        for plug in self._plugs:
            c = plug[c]
        return c