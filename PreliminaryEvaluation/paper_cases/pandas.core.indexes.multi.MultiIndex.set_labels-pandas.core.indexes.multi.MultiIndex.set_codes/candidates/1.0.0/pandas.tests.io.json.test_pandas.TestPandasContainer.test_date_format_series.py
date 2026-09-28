@pytest.mark.parametrize('date,date_unit', [('20130101 20:43:42.123', None), ('20130101 20:43:42', 's'), ('20130101 20:43:42.123', 'ms'), ('20130101 20:43:42.123456', 'us'), ('20130101 20:43:42.123456789', 'ns')])
def test_date_format_series(self, date, date_unit):
    ts = Series(Timestamp(date), index=self.ts.index)
    ts.iloc[1] = pd.NaT
    ts.iloc[5] = pd.NaT
    if date_unit:
        json = ts.to_json(date_format='iso', date_unit=date_unit)
    else:
        json = ts.to_json(date_format='iso')
    result = read_json(json, typ='series')
    expected = ts.copy()
    expected.index = expected.index.tz_localize('UTC')
    expected = expected.dt.tz_localize('UTC')
    tm.assert_series_equal(result, expected)