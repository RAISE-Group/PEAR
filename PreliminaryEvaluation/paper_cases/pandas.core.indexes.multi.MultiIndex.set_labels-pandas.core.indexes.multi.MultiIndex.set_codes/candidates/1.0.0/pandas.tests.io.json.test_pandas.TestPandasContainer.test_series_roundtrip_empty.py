@pytest.mark.parametrize('numpy', [True, False])
def test_series_roundtrip_empty(self, orient, numpy):
    data = self.empty_series.to_json(orient=orient)
    result = pd.read_json(data, typ='series', orient=orient, numpy=numpy)
    expected = self.empty_series.copy()
    if orient in ('values', 'records'):
        expected = expected.reset_index(drop=True)
    else:
        expected.index = expected.index.astype(float)
    tm.assert_series_equal(result, expected)