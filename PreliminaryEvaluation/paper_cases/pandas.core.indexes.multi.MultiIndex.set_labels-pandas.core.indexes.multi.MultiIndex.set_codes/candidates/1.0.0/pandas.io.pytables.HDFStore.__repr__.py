def __repr__(self) -> str:
    pstr = pprint_thing(self._path)
    return f'{type(self)}\nFile path: {pstr}\n'