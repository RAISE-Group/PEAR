def test_get_loc_nat(self):
    index = DatetimeIndex(['1/3/2000', 'NaT'])
    assert index.get_loc(pd.NaT) == 1