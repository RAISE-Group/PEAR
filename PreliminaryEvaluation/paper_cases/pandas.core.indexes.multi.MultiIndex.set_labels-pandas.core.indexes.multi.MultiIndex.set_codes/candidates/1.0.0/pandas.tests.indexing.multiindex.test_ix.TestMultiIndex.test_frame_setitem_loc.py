def test_frame_setitem_loc(self, multiindex_dataframe_random_data):
    frame = multiindex_dataframe_random_data
    frame.loc[('bar', 'two'), 'B'] = 5
    assert frame.loc[('bar', 'two'), 'B'] == 5
    df = frame.copy()
    df.columns = list(range(3))
    df.loc[('bar', 'two'), 1] = 7
    assert df.loc[('bar', 'two'), 1] == 7