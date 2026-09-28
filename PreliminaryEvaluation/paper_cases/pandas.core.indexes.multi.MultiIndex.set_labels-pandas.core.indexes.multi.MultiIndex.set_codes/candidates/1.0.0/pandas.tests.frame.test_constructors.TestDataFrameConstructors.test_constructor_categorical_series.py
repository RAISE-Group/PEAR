def test_constructor_categorical_series(self):
    items = [1, 2, 3, 1]
    exp = Series(items).astype('category')
    res = Series(items, dtype='category')
    tm.assert_series_equal(res, exp)
    items = ['a', 'b', 'c', 'a']
    exp = Series(items).astype('category')
    res = Series(items, dtype='category')
    tm.assert_series_equal(res, exp)
    index = date_range('20000101', periods=3)
    expected = Series(Categorical(values=[np.nan, np.nan, np.nan], categories=['a', 'b', 'c']))
    expected.index = index
    expected = DataFrame({'x': expected})
    df = DataFrame({'x': Series(['a', 'b', 'c'], dtype='category')}, index=index)
    tm.assert_frame_equal(df, expected)