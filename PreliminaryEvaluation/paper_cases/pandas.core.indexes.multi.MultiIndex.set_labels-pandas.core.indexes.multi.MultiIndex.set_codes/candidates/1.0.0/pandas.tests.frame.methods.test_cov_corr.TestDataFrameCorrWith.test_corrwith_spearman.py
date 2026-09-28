@td.skip_if_no_scipy
def test_corrwith_spearman(self):
    df = pd.DataFrame(np.random.random(size=(100, 3)))
    result = df.corrwith(df ** 2, method='spearman')
    expected = Series(np.ones(len(result)))
    tm.assert_series_equal(result, expected)