def test_loc_getitem_frame(self):
    df = DataFrame({'A': range(10)})
    s = pd.cut(df.A, 5)
    df['B'] = s
    df = df.set_index('B')
    result = df.loc[4]
    expected = df.iloc[4:6]
    tm.assert_frame_equal(result, expected)
    with pytest.raises(KeyError, match='10'):
        df.loc[10]
    result = df.loc[[4]]
    expected = df.iloc[4:6]
    tm.assert_frame_equal(result, expected)
    result = df.loc[[4, 5]]
    expected = df.take([4, 5, 4, 5])
    tm.assert_frame_equal(result, expected)
    with pytest.raises(KeyError, match='^$'):
        df.loc[[10]]
    with pytest.raises(KeyError, match='^$'):
        df.loc[[10, 4]]