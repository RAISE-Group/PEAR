@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_infer_datetime_format_consistent_format(self, cache):
    s = pd.Series(pd.date_range('20000101', periods=50, freq='H'))
    test_formats = ['%m-%d-%Y', '%m/%d/%Y %H:%M:%S.%f', '%Y-%m-%dT%H:%M:%S.%f']
    for test_format in test_formats:
        s_as_dt_strings = s.apply(lambda x: x.strftime(test_format))
        with_format = pd.to_datetime(s_as_dt_strings, format=test_format, cache=cache)
        no_infer = pd.to_datetime(s_as_dt_strings, infer_datetime_format=False, cache=cache)
        yes_infer = pd.to_datetime(s_as_dt_strings, infer_datetime_format=True, cache=cache)
        tm.assert_series_equal(with_format, no_infer)
        tm.assert_series_equal(no_infer, yes_infer)