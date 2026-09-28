def test_to_timestamp_freq(self):
    idx = pd.period_range('2017', periods=12, freq='A-DEC')
    result = idx.to_timestamp()
    expected = pd.date_range('2017', periods=12, freq='AS-JAN')
    tm.assert_index_equal(result, expected)