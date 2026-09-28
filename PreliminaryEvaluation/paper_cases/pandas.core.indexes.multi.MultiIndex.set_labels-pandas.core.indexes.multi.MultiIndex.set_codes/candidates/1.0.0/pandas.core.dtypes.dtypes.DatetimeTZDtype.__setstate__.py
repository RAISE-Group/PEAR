def __setstate__(self, state):
    self._tz = state['tz']
    self._unit = state['unit']