@pytest.mark.parametrize('dtype', [False, None])
@pytest.mark.parametrize('numpy', [True, False])
def test_series_roundtrip_object(self, orient, numpy, dtype):
    data = self.objSeries.to_json(orient=orient)
    result = pd.read_json(data, typ='series', orient=orient, numpy=numpy, dtype=dtype)
    expected = self.objSeries.copy()
    if orient in ('values', 'records'):
        expected = expected.reset_index(drop=True)
    if orient != 'split':
        expected.name = None
    tm.assert_series_equal(result, expected)