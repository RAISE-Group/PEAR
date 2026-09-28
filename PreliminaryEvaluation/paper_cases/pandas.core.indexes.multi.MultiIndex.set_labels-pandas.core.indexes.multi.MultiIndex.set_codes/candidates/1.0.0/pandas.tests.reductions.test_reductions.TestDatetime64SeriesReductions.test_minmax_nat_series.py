@pytest.mark.parametrize('nat_ser', [Series([pd.NaT, pd.NaT]), Series([pd.NaT, pd.Timedelta('nat')]), Series([pd.Timedelta('nat'), pd.Timedelta('nat')])])
def test_minmax_nat_series(self, nat_ser):
    assert nat_ser.min() is pd.NaT
    assert nat_ser.max() is pd.NaT
    assert nat_ser.min(skipna=False) is pd.NaT
    assert nat_ser.max(skipna=False) is pd.NaT