@pytest.mark.parametrize('tz', [None, 'UTC'])
def test_concat_NaT_dataframes(self, tz):
    first = pd.DataFrame([[pd.NaT], [pd.NaT]])
    first = first.apply(lambda x: x.dt.tz_localize(tz))
    second = pd.DataFrame([[pd.Timestamp('2015/01/01', tz=tz)], [pd.Timestamp('2016/01/01', tz=tz)]], index=[2, 3])
    expected = pd.DataFrame([pd.NaT, pd.NaT, pd.Timestamp('2015/01/01', tz=tz), pd.Timestamp('2016/01/01', tz=tz)])
    result = pd.concat([first, second], axis=0)
    tm.assert_frame_equal(result, expected)