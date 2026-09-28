@td.skip_if_has_locale
@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_with_apply(self, cache):
    td = Series(['May 04', 'Jun 02', 'Dec 11'], index=[1, 2, 3])
    expected = pd.to_datetime(td, format='%b %y', cache=cache)
    result = td.apply(pd.to_datetime, format='%b %y', cache=cache)
    tm.assert_series_equal(result, expected)
    td = pd.Series(['May 04', 'Jun 02', ''], index=[1, 2, 3])
    msg = "time data '' does not match format '%b %y' \\(match\\)"
    with pytest.raises(ValueError, match=msg):
        pd.to_datetime(td, format='%b %y', errors='raise', cache=cache)
    with pytest.raises(ValueError, match=msg):
        td.apply(pd.to_datetime, format='%b %y', errors='raise', cache=cache)
    expected = pd.to_datetime(td, format='%b %y', errors='coerce', cache=cache)
    result = td.apply(lambda x: pd.to_datetime(x, format='%b %y', errors='coerce', cache=cache))
    tm.assert_series_equal(result, expected)