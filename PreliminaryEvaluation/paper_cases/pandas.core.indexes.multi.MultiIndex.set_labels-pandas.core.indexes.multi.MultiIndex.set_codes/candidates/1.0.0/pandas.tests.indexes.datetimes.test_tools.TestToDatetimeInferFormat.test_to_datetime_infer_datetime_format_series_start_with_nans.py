@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_infer_datetime_format_series_start_with_nans(self, cache):
    s = pd.Series(np.array([np.nan, np.nan, '01/01/2011 00:00:00', '01/02/2011 00:00:00', '01/03/2011 00:00:00']))
    tm.assert_series_equal(pd.to_datetime(s, infer_datetime_format=False, cache=cache), pd.to_datetime(s, infer_datetime_format=True, cache=cache))