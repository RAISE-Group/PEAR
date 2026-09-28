@pytest.mark.parametrize('numpy', [True, False])
def test_series_roundtrip_timeseries(self, orient, numpy):
    data = self.ts.to_json(orient=orient)
    result = pd.read_json(data, typ='series', orient=orient, numpy=numpy)
    expected = self.ts.copy()
    if orient in ('values', 'records'):
        expected = expected.reset_index(drop=True)
    if orient != 'split':
        expected.name = None
    tm.assert_series_equal(result, expected)