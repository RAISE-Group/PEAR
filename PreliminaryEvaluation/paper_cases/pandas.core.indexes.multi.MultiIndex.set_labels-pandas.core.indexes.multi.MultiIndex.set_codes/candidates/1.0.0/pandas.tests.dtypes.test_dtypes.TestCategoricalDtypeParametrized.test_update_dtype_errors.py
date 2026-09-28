@pytest.mark.parametrize('bad_dtype', ['foo', object, np.int64, PeriodDtype('Q')])
def test_update_dtype_errors(self, bad_dtype):
    dtype = CategoricalDtype(list('abc'), False)
    msg = 'a CategoricalDtype must be passed to perform an update, '
    with pytest.raises(ValueError, match=msg):
        dtype.update_dtype(bad_dtype)