def test_value_counts_preserves_tz(self):
    dti = pd.date_range('2000', periods=2, freq='D', tz='US/Central')
    arr = DatetimeArray(dti).repeat([4, 3])
    result = arr.value_counts()
    assert result.index.equals(dti)
    arr[-2] = pd.NaT
    result = arr.value_counts()
    expected = pd.Series([1, 4, 2], index=[pd.NaT, dti[0], dti[1]])
    tm.assert_series_equal(result, expected)