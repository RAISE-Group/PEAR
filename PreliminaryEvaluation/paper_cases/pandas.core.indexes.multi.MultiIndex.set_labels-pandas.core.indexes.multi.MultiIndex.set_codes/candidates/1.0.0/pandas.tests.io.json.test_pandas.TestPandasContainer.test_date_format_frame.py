@pytest.mark.parametrize('date,date_unit', [('20130101 20:43:42.123', None), ('20130101 20:43:42', 's'), ('20130101 20:43:42.123', 'ms'), ('20130101 20:43:42.123456', 'us'), ('20130101 20:43:42.123456789', 'ns')])
def test_date_format_frame(self, date, date_unit):
    df = self.tsframe.copy()
    df['date'] = Timestamp(date)
    df.iloc[1, df.columns.get_loc('date')] = pd.NaT
    df.iloc[5, df.columns.get_loc('date')] = pd.NaT
    if date_unit:
        json = df.to_json(date_format='iso', date_unit=date_unit)
    else:
        json = df.to_json(date_format='iso')
    result = read_json(json)
    expected = df.copy()
    expected.index = expected.index.tz_localize('UTC')
    expected['date'] = expected['date'].dt.tz_localize('UTC')
    tm.assert_frame_equal(result, expected)