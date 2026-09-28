def __setattr__(self, key, val):
    prefix = object.__getattribute__(self, 'prefix')
    if prefix:
        prefix += '.'
    prefix += key
    if key in self.d and (not isinstance(self.d[key], dict)):
        _set_option(prefix, val)
    else:
        raise OptionError('You can only set the value of existing options')