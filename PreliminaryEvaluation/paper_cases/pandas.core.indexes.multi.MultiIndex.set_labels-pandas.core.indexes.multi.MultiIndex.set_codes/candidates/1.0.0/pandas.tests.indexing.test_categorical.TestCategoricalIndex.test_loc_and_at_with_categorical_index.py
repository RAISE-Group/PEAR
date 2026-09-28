def test_loc_and_at_with_categorical_index(self):
    s = Series([1, 2, 3], index=pd.CategoricalIndex(['A', 'B', 'C']))
    assert s.loc['A'] == 1
    assert s.at['A'] == 1
    df = DataFrame([[1, 2], [3, 4], [5, 6]], index=pd.CategoricalIndex(['A', 'B', 'C']))
    assert df.loc['B', 1] == 4
    assert df.at['B', 1] == 4