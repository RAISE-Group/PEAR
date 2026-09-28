def test_loc_len1(self, data):
    df = pd.DataFrame({'A': data})
    res = df.loc[[0], 'A']
    assert res._data._block.ndim == 1