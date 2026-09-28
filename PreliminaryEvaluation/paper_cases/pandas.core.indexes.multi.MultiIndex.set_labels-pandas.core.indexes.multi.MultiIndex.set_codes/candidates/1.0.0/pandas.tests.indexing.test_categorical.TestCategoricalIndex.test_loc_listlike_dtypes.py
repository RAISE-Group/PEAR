def test_loc_listlike_dtypes(self):
    index = CategoricalIndex(['a', 'b', 'c'])
    df = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=index)
    res = df.loc[['a', 'b']]
    exp_index = CategoricalIndex(['a', 'b'], categories=index.categories)
    exp = DataFrame({'A': [1, 2], 'B': [4, 5]}, index=exp_index)
    tm.assert_frame_equal(res, exp, check_index_type=True)
    res = df.loc[['a', 'a', 'b']]
    exp_index = CategoricalIndex(['a', 'a', 'b'], categories=index.categories)
    exp = DataFrame({'A': [1, 1, 2], 'B': [4, 4, 5]}, index=exp_index)
    tm.assert_frame_equal(res, exp, check_index_type=True)
    msg = 'a list-indexer must only include values that are in the categories'
    with pytest.raises(KeyError, match=msg):
        df.loc[['a', 'x']]
    index = CategoricalIndex(['a', 'b', 'a'])
    df = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=index)
    res = df.loc[['a', 'b']]
    exp = DataFrame({'A': [1, 3, 2], 'B': [4, 6, 5]}, index=CategoricalIndex(['a', 'a', 'b']))
    tm.assert_frame_equal(res, exp, check_index_type=True)
    res = df.loc[['a', 'a', 'b']]
    exp = DataFrame({'A': [1, 3, 1, 3, 2], 'B': [4, 6, 4, 6, 5]}, index=CategoricalIndex(['a', 'a', 'a', 'a', 'b']))
    tm.assert_frame_equal(res, exp, check_index_type=True)
    msg = 'a list-indexer must only include values that are in the categories'
    with pytest.raises(KeyError, match=msg):
        df.loc[['a', 'x']]
    index = CategoricalIndex(['a', 'b', 'a', 'c'], categories=list('abcde'))
    df = DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}, index=index)
    res = df.loc[['a', 'b']]
    exp = DataFrame({'A': [1, 3, 2], 'B': [5, 7, 6]}, index=CategoricalIndex(['a', 'a', 'b'], categories=list('abcde')))
    tm.assert_frame_equal(res, exp, check_index_type=True)
    res = df.loc[['a', 'e']]
    exp = DataFrame({'A': [1, 3, np.nan], 'B': [5, 7, np.nan]}, index=CategoricalIndex(['a', 'a', 'e'], categories=list('abcde')))
    tm.assert_frame_equal(res, exp, check_index_type=True)
    res = df.loc[['a', 'a', 'b']]
    exp = DataFrame({'A': [1, 3, 1, 3, 2], 'B': [5, 7, 5, 7, 6]}, index=CategoricalIndex(['a', 'a', 'a', 'a', 'b'], categories=list('abcde')))
    tm.assert_frame_equal(res, exp, check_index_type=True)
    msg = 'a list-indexer must only include values that are in the categories'
    with pytest.raises(KeyError, match=msg):
        df.loc[['a', 'x']]