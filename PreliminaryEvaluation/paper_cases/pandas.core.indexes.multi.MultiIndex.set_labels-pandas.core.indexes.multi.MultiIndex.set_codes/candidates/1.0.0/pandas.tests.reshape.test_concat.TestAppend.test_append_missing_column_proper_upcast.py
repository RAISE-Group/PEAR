def test_append_missing_column_proper_upcast(self, sort):
    df1 = DataFrame({'A': np.array([1, 2, 3, 4], dtype='i8')})
    df2 = DataFrame({'B': np.array([True, False, True, False], dtype=bool)})
    appended = df1.append(df2, ignore_index=True, sort=sort)
    assert appended['A'].dtype == 'f8'
    assert appended['B'].dtype == 'O'