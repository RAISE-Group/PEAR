def test_categorical_repr_unicode(self):

    class County:
        name = 'San Sebastián'
        state = 'PR'

        def __repr__(self) -> str:
            return self.name + ', ' + self.state
    cat = pd.Categorical([County() for _ in range(61)])
    idx = pd.Index(cat)
    ser = idx.to_series()
    repr(ser)
    str(ser)