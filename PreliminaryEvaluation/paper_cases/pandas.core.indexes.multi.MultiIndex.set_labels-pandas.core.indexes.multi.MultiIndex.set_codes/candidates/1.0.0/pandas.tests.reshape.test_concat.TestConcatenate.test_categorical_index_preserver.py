def test_categorical_index_preserver(self):
    a = Series(np.arange(6, dtype='int64'))
    b = Series(list('aabbca'))
    df2 = DataFrame({'A': a, 'B': b.astype(CategoricalDtype(list('cab')))}).set_index('B')
    result = pd.concat([df2, df2])
    expected = DataFrame({'A': pd.concat([a, a]), 'B': pd.concat([b, b]).astype(CategoricalDtype(list('cab')))}).set_index('B')
    tm.assert_frame_equal(result, expected)
    df3 = DataFrame({'A': a, 'B': Categorical(b, categories=list('abe'))}).set_index('B')
    msg = 'categories must match existing categories when appending'
    with pytest.raises(TypeError, match=msg):
        pd.concat([df2, df3])