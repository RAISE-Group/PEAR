def _get_options_with_defaults(self, engine):
    kwds = self.orig_options
    options = {}
    for argname, default in _parser_defaults.items():
        value = kwds.get(argname, default)
        if argname == 'mangle_dupe_cols' and (not value):
            raise ValueError('Setting mangle_dupe_cols=False is not supported yet')
        else:
            options[argname] = value
    for argname, default in _c_parser_defaults.items():
        if argname in kwds:
            value = kwds[argname]
            if engine != 'c' and value != default:
                if 'python' in engine and argname not in _python_unsupported:
                    pass
                elif value == _deprecated_defaults.get(argname, default):
                    pass
                else:
                    raise ValueError(f'The {repr(argname)} option is not supported with the {repr(engine)} engine')
        else:
            value = _deprecated_defaults.get(argname, default)
        options[argname] = value
    if engine == 'python-fwf':
        for argname, default in _fwf_defaults.items():
            options[argname] = kwds.get(argname, default)
    return options