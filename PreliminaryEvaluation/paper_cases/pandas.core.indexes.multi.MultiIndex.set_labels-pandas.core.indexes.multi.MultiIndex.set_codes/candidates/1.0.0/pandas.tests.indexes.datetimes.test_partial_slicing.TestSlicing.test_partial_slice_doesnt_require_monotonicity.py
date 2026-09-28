def test_partial_slice_doesnt_require_monotonicity(self):
    s = pd.Series(np.arange(10), pd.date_range('2014-01-01', periods=10))
    nonmonotonic = s[[3, 5, 4]]
    expected = nonmonotonic.iloc[:0]
    timestamp = pd.Timestamp('2014-01-10')
    tm.assert_series_equal(nonmonotonic['2014-01-10':], expected)
    with pytest.raises(KeyError, match="Timestamp\\('2014-01-10 00:00:00'\\)"):
        nonmonotonic[timestamp:]
    tm.assert_series_equal(nonmonotonic.loc['2014-01-10':], expected)
    with pytest.raises(KeyError, match="Timestamp\\('2014-01-10 00:00:00'\\)"):
        nonmonotonic.loc[timestamp:]