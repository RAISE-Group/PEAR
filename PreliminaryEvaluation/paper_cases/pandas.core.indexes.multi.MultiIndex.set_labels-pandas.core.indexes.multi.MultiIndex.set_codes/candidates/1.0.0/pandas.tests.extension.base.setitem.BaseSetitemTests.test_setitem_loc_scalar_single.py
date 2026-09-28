def test_setitem_loc_scalar_single(self, data):
    df = pd.DataFrame({'B': data})
    df.loc[10, 'B'] = data[1]
    assert df.loc[10, 'B'] == data[1]