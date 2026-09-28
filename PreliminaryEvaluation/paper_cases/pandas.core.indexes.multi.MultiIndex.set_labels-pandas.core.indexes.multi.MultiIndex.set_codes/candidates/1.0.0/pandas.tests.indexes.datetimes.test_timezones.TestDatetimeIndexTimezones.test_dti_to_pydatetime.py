def test_dti_to_pydatetime(self):
    dt = dateutil.parser.parse('2012-06-13T01:39:00Z')
    dt = dt.replace(tzinfo=tzlocal())
    arr = np.array([dt], dtype=object)
    result = to_datetime(arr, utc=True)
    assert result.tz is pytz.utc
    rng = date_range('2012-11-03 03:00', '2012-11-05 03:00', tz=tzlocal())
    arr = rng.to_pydatetime()
    result = to_datetime(arr, utc=True)
    assert result.tz is pytz.utc