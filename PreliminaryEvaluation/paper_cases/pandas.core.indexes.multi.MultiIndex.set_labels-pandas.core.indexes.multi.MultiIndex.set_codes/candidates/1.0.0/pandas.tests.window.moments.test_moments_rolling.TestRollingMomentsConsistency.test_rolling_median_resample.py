def test_rolling_median_resample(self):
    indices = [datetime(1975, 1, i) for i in range(1, 6)]
    indices.append(datetime(1975, 1, 5, 1))
    indices.append(datetime(1975, 1, 5, 2))
    series = Series(list(range(0, 5)) + [10, 20], index=indices)
    series = series.map(lambda x: float(x))
    series = series.sort_index()
    expected = Series([0.0, 1.0, 2.0, 3.0, 10], index=[datetime(1975, 1, i, 0) for i in range(1, 6)])
    x = series.resample('D').median().rolling(window=1).median()
    tm.assert_series_equal(expected, x)