@pytest.mark.parametrize('dtype', [np.float64, np.int])
@pytest.mark.parametrize('numpy', [True, False])
def test_series_roundtrip_numeric(self, orient, numpy, dtype):
    s = Series(range(6), index=['a', 'b', 'c', 'd', 'e', 'f'])
    data = s.to_json(orient=orient)
    result = pd.read_json(data, typ='series', orient=orient, numpy=numpy)
    expected = s.copy()
    if orient in ('values', 'records'):
        expected = expected.reset_index(drop=True)
    tm.assert_series_equal(result, expected)