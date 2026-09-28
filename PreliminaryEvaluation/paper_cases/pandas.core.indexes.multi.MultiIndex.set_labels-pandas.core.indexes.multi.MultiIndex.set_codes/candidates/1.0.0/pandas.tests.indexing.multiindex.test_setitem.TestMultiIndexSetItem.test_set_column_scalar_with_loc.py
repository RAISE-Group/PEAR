def test_set_column_scalar_with_loc(self, multiindex_dataframe_random_data):
    frame = multiindex_dataframe_random_data
    subset = frame.index[[1, 4, 5]]
    frame.loc[subset] = 99
    assert (frame.loc[subset].values == 99).all()
    col = frame['B']
    col[subset] = 97
    assert (frame.loc[subset, 'B'] == 97).all()