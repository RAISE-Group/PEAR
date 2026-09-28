def _pickle_roundtrip(self, obj):
    with tm.ensure_clean() as path:
        obj.to_pickle(path)
        unpickled = pd.read_pickle(path)
        return unpickled