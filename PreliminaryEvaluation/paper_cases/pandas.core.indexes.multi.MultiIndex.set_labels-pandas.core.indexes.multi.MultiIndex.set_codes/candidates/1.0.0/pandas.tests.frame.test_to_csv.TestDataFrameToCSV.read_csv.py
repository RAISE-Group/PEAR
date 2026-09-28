def read_csv(self, path, **kwargs):
    params = dict(index_col=0, parse_dates=True)
    params.update(**kwargs)
    return pd.read_csv(path, **params)