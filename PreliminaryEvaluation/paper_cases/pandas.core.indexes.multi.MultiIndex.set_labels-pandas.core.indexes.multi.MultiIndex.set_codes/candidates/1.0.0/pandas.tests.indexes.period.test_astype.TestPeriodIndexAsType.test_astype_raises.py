@pytest.mark.parametrize('dtype', [float, 'timedelta64', 'timedelta64[ns]'])
def test_astype_raises(self, dtype):
    idx = PeriodIndex(['2016-05-16', 'NaT', NaT, np.NaN], freq='D')
    msg = 'Cannot cast PeriodArray to dtype'
    with pytest.raises(TypeError, match=msg):
        idx.astype(dtype)