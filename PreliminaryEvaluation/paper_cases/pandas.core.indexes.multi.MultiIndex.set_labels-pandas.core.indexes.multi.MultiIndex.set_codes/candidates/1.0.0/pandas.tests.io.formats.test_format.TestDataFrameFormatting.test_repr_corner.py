def test_repr_corner(self):
    df = DataFrame({'foo': [-np.inf, np.inf]})
    repr(df)