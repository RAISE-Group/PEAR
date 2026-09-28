@property
def levels(self):
    result = [x._shallow_copy(name=name) for x, name in zip(self._levels, self._names)]
    for level in result:
        level._no_setting_name = True
    return FrozenList(result)