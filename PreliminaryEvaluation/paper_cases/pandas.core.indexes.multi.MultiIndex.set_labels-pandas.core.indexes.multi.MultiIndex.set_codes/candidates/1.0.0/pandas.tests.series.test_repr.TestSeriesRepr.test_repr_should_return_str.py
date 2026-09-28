def test_repr_should_return_str(self):
    data = [8, 5, 3, 5]
    index1 = ['σ', 'τ', 'υ', 'φ']
    df = Series(data, index=index1)
    assert type(df.__repr__() == str)