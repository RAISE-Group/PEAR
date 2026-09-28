def test_replace_for_new_dtypes(self, datetime_frame):
    tsframe = datetime_frame.copy().astype(np.float32)
    tsframe['A'][:5] = np.nan
    tsframe['A'][-5:] = np.nan
    zero_filled = tsframe.replace(np.nan, -100000000.0)
    tm.assert_frame_equal(zero_filled, tsframe.fillna(-100000000.0))
    tm.assert_frame_equal(zero_filled.replace(-100000000.0, np.nan), tsframe)
    tsframe['A'][:5] = np.nan
    tsframe['A'][-5:] = np.nan
    tsframe['B'][:5] = -100000000.0
    b = tsframe['B']
    b[b == -100000000.0] = np.nan
    tsframe['B'] = b
    result = tsframe.fillna(method='bfill')
    tm.assert_frame_equal(result, tsframe.fillna(method='bfill'))