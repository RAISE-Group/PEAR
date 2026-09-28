@pytest.mark.parametrize('input_s', [['19801222', '20010112', None], ['19801222', '20010112', np.nan], ['19801222', '20010112', pd.NaT], ['19801222', '20010112', 'NaT'], [19801222, 20010112, None], [19801222, 20010112, np.nan], [19801222, 20010112, pd.NaT], [19801222, 20010112, 'NaT']])
def test_to_datetime_format_YYYYMMDD_with_none(self, input_s):
    expected = Series([Timestamp('19801222'), Timestamp('20010112'), pd.NaT])
    result = Series(pd.to_datetime(input_s, format='%Y%m%d'))
    tm.assert_series_equal(result, expected)