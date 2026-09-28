@pytest.mark.parametrize('tz1', [None, 'UTC'])
@pytest.mark.parametrize('tz2', [None, 'UTC'])
def test_concat_NaT_dataframes_all_NaT_axis_1(self, tz1, tz2):
    first = pd.DataFrame(pd.Series([pd.NaT, pd.NaT]).dt.tz_localize(tz1))
    second = pd.DataFrame(pd.Series([pd.NaT]).dt.tz_localize(tz2), columns=[1])
    expected = pd.DataFrame({0: pd.Series([pd.NaT, pd.NaT]).dt.tz_localize(tz1), 1: pd.Series([pd.NaT, pd.NaT]).dt.tz_localize(tz2)})
    result = pd.concat([first, second], axis=1)
    tm.assert_frame_equal(result, expected)