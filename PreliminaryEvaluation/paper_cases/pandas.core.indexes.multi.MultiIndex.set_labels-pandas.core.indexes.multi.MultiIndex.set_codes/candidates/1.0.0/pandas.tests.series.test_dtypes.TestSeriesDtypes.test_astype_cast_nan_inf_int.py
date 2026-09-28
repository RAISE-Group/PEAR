@pytest.mark.parametrize('value', [np.nan, np.inf])
@pytest.mark.parametrize('dtype', [np.int32, np.int64])
def test_astype_cast_nan_inf_int(self, dtype, value):
    msg = 'Cannot convert non-finite values \\(NA or inf\\) to integer'
    s = Series([value])
    with pytest.raises(ValueError, match=msg):
        s.astype(dtype)