@pytest.mark.parametrize('tz', [None, 'UTC'])
def test_mean_mixed_datetime_numeric(self, tz):
    df = pd.DataFrame({'A': [1, 1], 'B': [pd.Timestamp('2000', tz=tz)] * 2})
    result = df.mean()
    expected = pd.Series([1.0], index=['A'])
    tm.assert_series_equal(result, expected)