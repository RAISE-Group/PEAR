def test_constructor_dict_dont_upcast(self):
    d = {'Col1': {'Row1': 'A String', 'Row2': np.nan}}
    df = DataFrame(d)
    assert isinstance(df['Col1']['Row2'], float)
    dm = DataFrame([[1, 2], ['a', 'b']], index=[1, 2], columns=[1, 2])
    assert isinstance(dm[1][1], int)