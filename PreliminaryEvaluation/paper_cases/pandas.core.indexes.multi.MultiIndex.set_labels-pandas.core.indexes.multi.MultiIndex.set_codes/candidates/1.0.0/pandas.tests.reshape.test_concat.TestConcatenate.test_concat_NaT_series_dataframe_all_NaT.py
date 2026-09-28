@pytest.mark.parametrize('tz1', [None, 'UTC'])
@pytest.mark.parametrize('tz2', [None, 'UTC'])
def test_concat_NaT_series_dataframe_all_NaT(self, tz1, tz2):
    first = pd.Series([pd.NaT, pd.NaT]).dt.tz_localize(tz1)
    second = pd.DataFrame([[pd.Timestamp('2015/01/01', tz=tz2)], [pd.Timestamp('2016/01/01', tz=tz2)]], index=[2, 3])
    expected = pd.DataFrame([pd.NaT, pd.NaT, pd.Timestamp('2015/01/01', tz=tz2), pd.Timestamp('2016/01/01', tz=tz2)])
    if tz1 != tz2:
        expected = expected.astype(object)
    result = pd.concat([first, second])
    tm.assert_frame_equal(result, expected)