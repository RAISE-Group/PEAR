@pytest.mark.parametrize('window', range(7))
def test_rolling_corr_with_zero_variance(self, window):
    s = pd.Series(np.zeros(20))
    other = pd.Series(np.arange(20))
    assert s.rolling(window=window).corr(other=other).isna().all()