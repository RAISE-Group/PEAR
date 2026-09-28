@pytest.mark.parametrize('tz', [None, 'UTC'])
def test_mean_excludes_datetimes(self, tz):
    df = pd.DataFrame({'A': [pd.Timestamp('2000', tz=tz)] * 2})
    result = df.mean()
    expected = pd.Series(dtype=np.float64)
    tm.assert_series_equal(result, expected)