def _validate_format(self, format: str) -> str:
    """ validate / deprecate formats """
    try:
        format = _FORMAT_MAP[format.lower()]
    except KeyError:
        raise TypeError(f'invalid HDFStore format specified [{format}]')
    return format