@pytest.mark.parametrize('tz1', [None, 'UTC'])
@pytest.mark.parametrize('tz2', [None, 'UTC'])
@pytest.mark.parametrize('s', [pd.NaT, pd.Timestamp('20150101')])
def test_concat_NaT_dataframes_all_NaT_axis_0(self, tz1, tz2, s):
    first = pd.DataFrame([[pd.NaT], [pd.NaT]]).apply(lambda x: x.dt.tz_localize(tz1))
    second = pd.DataFrame([s]).apply(lambda x: x.dt.tz_localize(tz2))
    result = pd.concat([first, second], axis=0)
    expected = pd.DataFrame(pd.Series([pd.NaT, pd.NaT, s], index=[0, 1, 0]))
    expected = expected.apply(lambda x: x.dt.tz_localize(tz2))
    if tz1 != tz2:
        expected = expected.astype(object)
    tm.assert_frame_equal(result, expected)