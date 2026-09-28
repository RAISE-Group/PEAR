def test_setitem_iloc_scalar_multiple_homogoneous(self, data):
    df = pd.DataFrame({'A': data, 'B': data})
    df.iloc[10, 1] = data[1]
    assert df.loc[10, 'B'] == data[1]