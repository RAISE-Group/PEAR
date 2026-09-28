@property
def _box_func(self):
    """Maybe box an ordinal or Period"""

    def func(x):
        if isinstance(x, Period) or x is NaT:
            return x
        else:
            return Period._from_ordinal(ordinal=x, freq=self.freq)
    return func