def test_sum_mixed_datetime(self):
    df = pd.DataFrame({'A': pd.date_range('2000', periods=4), 'B': [1, 2, 3, 4]}).reindex([2, 3, 4])
    result = df.sum()
    expected = pd.Series({'B': 7.0})
    tm.assert_series_equal(result, expected)