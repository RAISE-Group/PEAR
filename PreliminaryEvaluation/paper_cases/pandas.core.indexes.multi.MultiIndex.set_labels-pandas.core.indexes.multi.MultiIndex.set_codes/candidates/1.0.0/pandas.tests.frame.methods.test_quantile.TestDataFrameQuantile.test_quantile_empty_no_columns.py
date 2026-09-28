def test_quantile_empty_no_columns(self):
    df = pd.DataFrame(pd.date_range('1/1/18', periods=5))
    df.columns.name = 'captain tightpants'
    result = df.quantile(0.5)
    expected = pd.Series([], index=[], name=0.5, dtype=np.float64)
    expected.index.name = 'captain tightpants'
    tm.assert_series_equal(result, expected)
    result = df.quantile([0.5])
    expected = pd.DataFrame([], index=[0.5], columns=[])
    expected.columns.name = 'captain tightpants'
    tm.assert_frame_equal(result, expected)