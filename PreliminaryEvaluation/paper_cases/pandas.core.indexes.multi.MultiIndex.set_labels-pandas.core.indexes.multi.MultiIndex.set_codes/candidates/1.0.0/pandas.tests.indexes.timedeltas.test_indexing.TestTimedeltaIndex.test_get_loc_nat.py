def test_get_loc_nat(self):
    tidx = TimedeltaIndex(['1 days 01:00:00', 'NaT', '2 days 01:00:00'])
    assert tidx.get_loc(pd.NaT) == 1
    assert tidx.get_loc(None) == 1
    assert tidx.get_loc(float('nan')) == 1
    assert tidx.get_loc(np.nan) == 1