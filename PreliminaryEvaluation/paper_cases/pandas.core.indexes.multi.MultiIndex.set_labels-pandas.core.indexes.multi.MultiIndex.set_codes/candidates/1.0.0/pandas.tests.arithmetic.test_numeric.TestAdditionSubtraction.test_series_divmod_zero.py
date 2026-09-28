def test_series_divmod_zero(self):
    tser = tm.makeTimeSeries().rename('ts')
    other = tser * 0
    result = divmod(tser, other)
    exp1 = pd.Series([np.inf] * len(tser), index=tser.index, name='ts')
    exp2 = pd.Series([np.nan] * len(tser), index=tser.index, name='ts')
    tm.assert_series_equal(result[0], exp1)
    tm.assert_series_equal(result[1], exp2)