def test_assigning_ops(self):
    cats = Categorical(['a', 'a', 'a', 'a', 'a', 'a', 'a'], categories=['a', 'b'])
    idx = Index(['h', 'i', 'j', 'k', 'l', 'm', 'n'])
    values = [1, 1, 1, 1, 1, 1, 1]
    orig = DataFrame({'cats': cats, 'values': values}, index=idx)
    cats1 = Categorical(['a', 'a', 'b', 'a', 'a', 'a', 'a'], categories=['a', 'b'])
    idx1 = Index(['h', 'i', 'j', 'k', 'l', 'm', 'n'])
    values1 = [1, 1, 2, 1, 1, 1, 1]
    exp_single_row = DataFrame({'cats': cats1, 'values': values1}, index=idx1)
    cats2 = Categorical(['a', 'a', 'b', 'b', 'a', 'a', 'a'], categories=['a', 'b'])
    idx2 = Index(['h', 'i', 'j', 'k', 'l', 'm', 'n'])
    values2 = [1, 1, 2, 2, 1, 1, 1]
    exp_multi_row = DataFrame({'cats': cats2, 'values': values2}, index=idx2)
    cats3 = Categorical(['a', 'a', 'b', 'b', 'a', 'a', 'a'], categories=['a', 'b'])
    idx3 = Index(['h', 'i', 'j', 'k', 'l', 'm', 'n'])
    values3 = [1, 1, 1, 1, 1, 1, 1]
    exp_parts_cats_col = DataFrame({'cats': cats3, 'values': values3}, index=idx3)
    cats4 = Categorical(['a', 'a', 'b', 'a', 'a', 'a', 'a'], categories=['a', 'b'])
    idx4 = Index(['h', 'i', 'j', 'k', 'l', 'm', 'n'])
    values4 = [1, 1, 1, 1, 1, 1, 1]
    exp_single_cats_value = DataFrame({'cats': cats4, 'values': values4}, index=idx4)
    df = orig.copy()
    df.iloc[2, 0] = 'b'
    tm.assert_frame_equal(df, exp_single_cats_value)
    df = orig.copy()
    df.iloc[df.index == 'j', 0] = 'b'
    tm.assert_frame_equal(df, exp_single_cats_value)
    with pytest.raises(ValueError):
        df = orig.copy()
        df.iloc[2, 0] = 'c'
    df = orig.copy()
    df.iloc[2, :] = ['b', 2]
    tm.assert_frame_equal(df, exp_single_row)
    with pytest.raises(ValueError):
        df = orig.copy()
        df.iloc[2, :] = ['c', 2]
    df = orig.copy()
    df.iloc[2:4, :] = [['b', 2], ['b', 2]]
    tm.assert_frame_equal(df, exp_multi_row)
    with pytest.raises(ValueError):
        df = orig.copy()
        df.iloc[2:4, :] = [['c', 2], ['c', 2]]
    df = orig.copy()
    df.iloc[2:4, 0] = Categorical(['b', 'b'], categories=['a', 'b'])
    tm.assert_frame_equal(df, exp_parts_cats_col)
    with pytest.raises(ValueError):
        df = orig.copy()
        df.iloc[2:4, 0] = Categorical(list('bb'), categories=list('abc'))
    with pytest.raises(ValueError):
        df = orig.copy()
        df.iloc[2:4, 0] = Categorical(list('cc'), categories=list('abc'))
    df = orig.copy()
    df.iloc[2:4, 0] = ['b', 'b']
    tm.assert_frame_equal(df, exp_parts_cats_col)
    with pytest.raises(ValueError):
        df.iloc[2:4, 0] = ['c', 'c']
    df = orig.copy()
    df.loc['j', 'cats'] = 'b'
    tm.assert_frame_equal(df, exp_single_cats_value)
    df = orig.copy()
    df.loc[df.index == 'j', 'cats'] = 'b'
    tm.assert_frame_equal(df, exp_single_cats_value)
    with pytest.raises(ValueError):
        df = orig.copy()
        df.loc['j', 'cats'] = 'c'
    df = orig.copy()
    df.loc['j', :] = ['b', 2]
    tm.assert_frame_equal(df, exp_single_row)
    with pytest.raises(ValueError):
        df = orig.copy()
        df.loc['j', :] = ['c', 2]
    df = orig.copy()
    df.loc['j':'k', :] = [['b', 2], ['b', 2]]
    tm.assert_frame_equal(df, exp_multi_row)
    with pytest.raises(ValueError):
        df = orig.copy()
        df.loc['j':'k', :] = [['c', 2], ['c', 2]]
    df = orig.copy()
    df.loc['j':'k', 'cats'] = Categorical(['b', 'b'], categories=['a', 'b'])
    tm.assert_frame_equal(df, exp_parts_cats_col)
    with pytest.raises(ValueError):
        df = orig.copy()
        df.loc['j':'k', 'cats'] = Categorical(['b', 'b'], categories=['a', 'b', 'c'])
    with pytest.raises(ValueError):
        df = orig.copy()
        df.loc['j':'k', 'cats'] = Categorical(['c', 'c'], categories=['a', 'b', 'c'])
    df = orig.copy()
    df.loc['j':'k', 'cats'] = ['b', 'b']
    tm.assert_frame_equal(df, exp_parts_cats_col)
    with pytest.raises(ValueError):
        df.loc['j':'k', 'cats'] = ['c', 'c']
    df = orig.copy()
    df.loc['j', df.columns[0]] = 'b'
    tm.assert_frame_equal(df, exp_single_cats_value)
    df = orig.copy()
    df.loc[df.index == 'j', df.columns[0]] = 'b'
    tm.assert_frame_equal(df, exp_single_cats_value)
    with pytest.raises(ValueError):
        df = orig.copy()
        df.loc['j', df.columns[0]] = 'c'
    df = orig.copy()
    df.loc['j', :] = ['b', 2]
    tm.assert_frame_equal(df, exp_single_row)
    with pytest.raises(ValueError):
        df = orig.copy()
        df.loc['j', :] = ['c', 2]
    df = orig.copy()
    df.loc['j':'k', :] = [['b', 2], ['b', 2]]
    tm.assert_frame_equal(df, exp_multi_row)
    with pytest.raises(ValueError):
        df = orig.copy()
        df.loc['j':'k', :] = [['c', 2], ['c', 2]]
    df = orig.copy()
    df.loc['j':'k', df.columns[0]] = Categorical(['b', 'b'], categories=['a', 'b'])
    tm.assert_frame_equal(df, exp_parts_cats_col)
    with pytest.raises(ValueError):
        df = orig.copy()
        df.loc['j':'k', df.columns[0]] = Categorical(['b', 'b'], categories=['a', 'b', 'c'])
    with pytest.raises(ValueError):
        df = orig.copy()
        df.loc['j':'k', df.columns[0]] = Categorical(['c', 'c'], categories=['a', 'b', 'c'])
    df = orig.copy()
    df.loc['j':'k', df.columns[0]] = ['b', 'b']
    tm.assert_frame_equal(df, exp_parts_cats_col)
    with pytest.raises(ValueError):
        df.loc['j':'k', df.columns[0]] = ['c', 'c']
    df = orig.copy()
    df.iat[2, 0] = 'b'
    tm.assert_frame_equal(df, exp_single_cats_value)
    with pytest.raises(ValueError):
        df = orig.copy()
        df.iat[2, 0] = 'c'
    df = orig.copy()
    df.at['j', 'cats'] = 'b'
    tm.assert_frame_equal(df, exp_single_cats_value)
    with pytest.raises(ValueError):
        df = orig.copy()
        df.at['j', 'cats'] = 'c'
    catsf = Categorical(['a', 'a', 'c', 'c', 'a', 'a', 'a'], categories=['a', 'b', 'c'])
    idxf = Index(['h', 'i', 'j', 'k', 'l', 'm', 'n'])
    valuesf = [1, 1, 3, 3, 1, 1, 1]
    df = DataFrame({'cats': catsf, 'values': valuesf}, index=idxf)
    exp_fancy = exp_multi_row.copy()
    exp_fancy['cats'].cat.set_categories(['a', 'b', 'c'], inplace=True)
    df[df['cats'] == 'c'] = ['b', 2]
    tm.assert_frame_equal(df, exp_fancy)
    df = orig.copy()
    df.at['j', 'cats'] = 'b'
    tm.assert_frame_equal(df, exp_single_cats_value)
    with pytest.raises(ValueError):
        df = orig.copy()
        df.at['j', 'cats'] = 'c'
    df = DataFrame({'a': [1, 1, 1, 1, 1], 'b': list('aaaaa')})
    exp = DataFrame({'a': [1, 'b', 'b', 1, 1], 'b': list('aabba')})
    df.loc[1:2, 'a'] = Categorical(['b', 'b'], categories=['a', 'b'])
    df.loc[2:3, 'b'] = Categorical(['b', 'b'], categories=['a', 'b'])
    tm.assert_frame_equal(df, exp)