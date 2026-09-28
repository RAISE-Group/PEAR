def test_nat(self):
    assert DatetimeIndex([np.nan])[0] is pd.NaT