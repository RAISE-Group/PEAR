@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_infer_datetime_format_inconsistent_format(self, cache):
    s = pd.Series(np.array(['01/01/2011 00:00:00', '01-02-2011 00:00:00', '2011-01-03T00:00:00']))
    tm.assert_series_equal(pd.to_datetime(s, infer_datetime_format=False, cache=cache), pd.to_datetime(s, infer_datetime_format=True, cache=cache))
    s = pd.Series(np.array(['Jan/01/2011', 'Feb/01/2011', 'Mar/01/2011']))
    tm.assert_series_equal(pd.to_datetime(s, infer_datetime_format=False, cache=cache), pd.to_datetime(s, infer_datetime_format=True, cache=cache))