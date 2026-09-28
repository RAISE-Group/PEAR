@pytest.mark.parametrize('method', ['ceil', 'round', 'floor'])
def test_dt_round_tz_ambiguous(self, method):
    df1 = pd.DataFrame([pd.to_datetime('2017-10-29 02:00:00+02:00', utc=True), pd.to_datetime('2017-10-29 02:00:00+01:00', utc=True), pd.to_datetime('2017-10-29 03:00:00+01:00', utc=True)], columns=['date'])
    df1['date'] = df1['date'].dt.tz_convert('Europe/Madrid')
    result = getattr(df1.date.dt, method)('H', ambiguous='infer')
    expected = df1['date']
    tm.assert_series_equal(result, expected)
    result = getattr(df1.date.dt, method)('H', ambiguous=[True, False, False])
    tm.assert_series_equal(result, expected)
    result = getattr(df1.date.dt, method)('H', ambiguous='NaT')
    expected = df1['date'].copy()
    expected.iloc[0:2] = pd.NaT
    tm.assert_series_equal(result, expected)
    with pytest.raises(pytz.AmbiguousTimeError):
        getattr(df1.date.dt, method)('H', ambiguous='raise')