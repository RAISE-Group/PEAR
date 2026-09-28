@classmethod
def _concat_same_type(cls, to_concat):
    data = list(itertools.chain.from_iterable([x.data for x in to_concat]))
    return cls(data)