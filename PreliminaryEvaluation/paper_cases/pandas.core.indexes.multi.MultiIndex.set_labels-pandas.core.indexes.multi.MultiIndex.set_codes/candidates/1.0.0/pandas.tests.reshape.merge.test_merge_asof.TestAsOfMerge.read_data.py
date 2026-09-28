def read_data(self, datapath, name, dedupe=False):
    path = datapath('reshape', 'merge', 'data', name)
    x = read_csv(path)
    if dedupe:
        x = x.drop_duplicates(['time', 'ticker'], keep='last').reset_index(drop=True)
    x.time = to_datetime(x.time)
    return x