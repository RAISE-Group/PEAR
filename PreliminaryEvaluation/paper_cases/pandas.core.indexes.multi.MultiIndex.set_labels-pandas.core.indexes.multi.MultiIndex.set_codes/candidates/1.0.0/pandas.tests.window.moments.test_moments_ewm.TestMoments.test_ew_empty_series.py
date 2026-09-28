@pytest.mark.parametrize('method', ['mean', 'vol', 'var'])
def test_ew_empty_series(self, method):
    vals = pd.Series([], dtype=np.float64)
    ewm = vals.ewm(3)
    result = getattr(ewm, method)()
    tm.assert_almost_equal(result, vals)