@pytest.mark.parametrize('dtype', [float, 'timedelta64', 'timedelta64[ns]', 'datetime64', 'datetime64[D]'])
def test_astype_raises(self, dtype):
    idx = DatetimeIndex(['2016-05-16', 'NaT', NaT, np.NaN])
    msg = 'Cannot cast DatetimeArray to dtype'
    with pytest.raises(TypeError, match=msg):
        idx.astype(dtype)