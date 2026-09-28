@pytest.mark.parametrize('in_series', [True, False])
@pytest.mark.parametrize('dtype', ['int32', 'int64', 'bool'])
def test_to_numpy_dtype(self, dtype, in_series):
    a = pd.array([0, 1], dtype='Int64')
    if in_series:
        a = pd.Series(a)
    result = a.to_numpy(dtype=dtype)
    expected = np.array([0, 1], dtype=dtype)
    tm.assert_numpy_array_equal(result, expected)