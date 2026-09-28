@pytest.mark.parametrize('numpy', [True, False])
def test_series_roundtrip_simple(self, orient, numpy):
    data = self.series.to_json(orient=orient)
    result = pd.read_json(data, typ='series', orient=orient, numpy=numpy)
    expected = self.series.copy()
    if orient in ('values', 'records'):
        expected = expected.reset_index(drop=True)
    if orient != 'split':
        expected.name = None
    tm.assert_series_equal(result, expected)