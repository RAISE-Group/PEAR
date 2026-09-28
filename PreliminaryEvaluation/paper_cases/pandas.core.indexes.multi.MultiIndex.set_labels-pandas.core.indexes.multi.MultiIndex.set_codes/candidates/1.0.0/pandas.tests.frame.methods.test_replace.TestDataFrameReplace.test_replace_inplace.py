def test_replace_inplace(self, datetime_frame, float_string_frame):
    datetime_frame['A'][:5] = np.nan
    datetime_frame['A'][-5:] = np.nan
    tsframe = datetime_frame.copy()
    tsframe.replace(np.nan, 0, inplace=True)
    tm.assert_frame_equal(tsframe, datetime_frame.fillna(0))
    mf = float_string_frame
    mf.iloc[5:20, mf.columns.get_loc('foo')] = np.nan
    mf.iloc[-10:, mf.columns.get_loc('A')] = np.nan
    result = float_string_frame.replace(np.nan, 0)
    expected = float_string_frame.fillna(value=0)
    tm.assert_frame_equal(result, expected)
    tsframe = datetime_frame.copy()
    tsframe.replace([np.nan], [0], inplace=True)
    tm.assert_frame_equal(tsframe, datetime_frame.fillna(0))