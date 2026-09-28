def read_csv(self, path, **kwargs):
    params = dict(squeeze=True, index_col=0, header=None, parse_dates=True)
    params.update(**kwargs)
    header = params.get('header')
    out = pd.read_csv(path, **params)
    if header is None:
        out.name = out.index.name = None
    return out