@cache_readonly
def freqstr(self):
    try:
        code = self.rule_code
    except NotImplementedError:
        return repr(self)
    if self.n != 1:
        fstr = f'{self.n}{code}'
    else:
        fstr = code
    try:
        if self._offset:
            fstr += self._offset_str()
    except AttributeError:
        pass
    return fstr