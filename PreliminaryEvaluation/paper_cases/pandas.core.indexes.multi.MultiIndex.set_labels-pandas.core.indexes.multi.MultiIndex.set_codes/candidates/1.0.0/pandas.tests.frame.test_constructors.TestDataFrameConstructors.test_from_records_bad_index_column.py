def test_from_records_bad_index_column(self):
    df = DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'])
    df1 = DataFrame.from_records(df, index=['C'])
    tm.assert_index_equal(df1.index, Index(df.C))
    df1 = DataFrame.from_records(df, index='C')
    tm.assert_index_equal(df1.index, Index(df.C))
    msg = 'Shape of passed values is \\(10, 3\\), indices imply \\(1, 3\\)'
    with pytest.raises(ValueError, match=msg):
        DataFrame.from_records(df, index=[2])
    with pytest.raises(KeyError, match='^2$'):
        DataFrame.from_records(df, index=2)