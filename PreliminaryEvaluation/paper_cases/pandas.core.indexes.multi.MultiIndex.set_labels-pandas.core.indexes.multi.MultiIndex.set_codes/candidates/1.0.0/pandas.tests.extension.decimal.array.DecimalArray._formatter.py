def _formatter(self, boxed=False):
    if boxed:
        return 'Decimal: {0}'.format
    return repr