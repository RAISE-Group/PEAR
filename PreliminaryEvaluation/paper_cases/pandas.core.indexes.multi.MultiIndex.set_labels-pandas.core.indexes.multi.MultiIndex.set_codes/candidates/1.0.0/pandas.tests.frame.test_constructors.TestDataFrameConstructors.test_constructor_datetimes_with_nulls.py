@pytest.mark.parametrize('arr', [np.array([None, None, None, None, datetime.now(), None]), np.array([None, None, datetime.now(), None]), [[np.datetime64('NaT')], [None]], [[np.datetime64('NaT')], [pd.NaT]], [[None], [np.datetime64('NaT')]], [[None], [pd.NaT]], [[pd.NaT], [np.datetime64('NaT')]], [[pd.NaT], [None]]])
def test_constructor_datetimes_with_nulls(self, arr):
    result = DataFrame(arr).dtypes
    expected = Series([np.dtype('datetime64[ns]')])
    tm.assert_series_equal(result, expected)