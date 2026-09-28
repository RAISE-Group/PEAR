@pytest.mark.parametrize('dtype1', [np.int64, np.float64, np.uint64])
def test_ser_div_ser(self, dtype1, any_real_dtype):
    dtype2 = any_real_dtype
    first = Series([3, 4, 5, 8], name='first').astype(dtype1)
    second = Series([0, 0, 0, 3], name='second').astype(dtype2)
    with np.errstate(all='ignore'):
        expected = Series(first.values.astype(np.float64) / second.values, dtype='float64', name=None)
    expected.iloc[0:3] = np.inf
    result = first / second
    tm.assert_series_equal(result, expected)
    assert not result.equals(second / first)