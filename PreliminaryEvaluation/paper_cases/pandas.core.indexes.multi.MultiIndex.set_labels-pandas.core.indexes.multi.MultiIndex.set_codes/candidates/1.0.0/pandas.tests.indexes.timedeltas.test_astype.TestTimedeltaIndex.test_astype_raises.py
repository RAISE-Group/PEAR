@pytest.mark.parametrize('dtype', [float, 'datetime64', 'datetime64[ns]'])
def test_astype_raises(self, dtype):
    idx = TimedeltaIndex([100000000000000.0, 'NaT', NaT, np.NaN])
    msg = 'Cannot cast TimedeltaArray to dtype'
    with pytest.raises(TypeError, match=msg):
        idx.astype(dtype)