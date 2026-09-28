def test_scalar_assignment(self):
    df = pd.DataFrame(index=(0, 1, 2))
    df['now'] = pd.Timestamp('20130101', tz='UTC')
    expected = pd.DataFrame({'now': pd.Timestamp('20130101', tz='UTC')}, index=[0, 1, 2])
    tm.assert_frame_equal(df, expected)