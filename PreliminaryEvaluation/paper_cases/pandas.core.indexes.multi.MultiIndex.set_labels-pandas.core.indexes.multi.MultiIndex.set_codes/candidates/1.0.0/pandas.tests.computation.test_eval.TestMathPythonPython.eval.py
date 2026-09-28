def eval(self, *args, **kwargs):
    kwargs['engine'] = self.engine
    kwargs['parser'] = self.parser
    kwargs['level'] = kwargs.pop('level', 0) + 1
    return pd.eval(*args, **kwargs)