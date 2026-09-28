def test_at_time_tz(self):
    dti = pd.date_range('2018', periods=3, freq='H', tz='US/Pacific')
    df = pd.DataFrame(list(range(len(dti))), index=dti)
    result = df.at_time(time(4, tzinfo=pytz.timezone('US/Eastern')))
    expected = df.iloc[1:2]
    tm.assert_frame_equal(result, expected)