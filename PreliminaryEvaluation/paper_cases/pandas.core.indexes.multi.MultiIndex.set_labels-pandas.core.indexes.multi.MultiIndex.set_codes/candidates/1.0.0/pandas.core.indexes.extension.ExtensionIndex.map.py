@Appender(Index.map.__doc__)
def map(self, mapper, na_action=None):
    try:
        result = mapper(self)
        if isinstance(result, np.ndarray):
            result = Index(result)
        if not isinstance(result, Index):
            raise TypeError('The map function must return an Index object')
        return result
    except Exception:
        return self.astype(object).map(mapper)