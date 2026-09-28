def test_union_categorical(self):
    data = [(list('abc'), list('abd'), list('abcabd')), ([0, 1, 2], [2, 3, 4], [0, 1, 2, 2, 3, 4]), ([0, 1.2, 2], [2, 3.4, 4], [0, 1.2, 2, 2, 3.4, 4]), (['b', 'b', np.nan, 'a'], ['a', np.nan, 'c'], ['b', 'b', np.nan, 'a', 'a', np.nan, 'c']), (pd.date_range('2014-01-01', '2014-01-05'), pd.date_range('2014-01-06', '2014-01-07'), pd.date_range('2014-01-01', '2014-01-07')), (pd.date_range('2014-01-01', '2014-01-05', tz='US/Central'), pd.date_range('2014-01-06', '2014-01-07', tz='US/Central'), pd.date_range('2014-01-01', '2014-01-07', tz='US/Central')), (pd.period_range('2014-01-01', '2014-01-05'), pd.period_range('2014-01-06', '2014-01-07'), pd.period_range('2014-01-01', '2014-01-07'))]
    for a, b, combined in data:
        for box in [Categorical, CategoricalIndex, Series]:
            result = union_categoricals([box(Categorical(a)), box(Categorical(b))])
            expected = Categorical(combined)
            tm.assert_categorical_equal(result, expected, check_category_order=True)
    s = Categorical(['x', 'y', 'z'])
    s2 = Categorical(['a', 'b', 'c'])
    result = union_categoricals([s, s2])
    expected = Categorical(['x', 'y', 'z', 'a', 'b', 'c'], categories=['x', 'y', 'z', 'a', 'b', 'c'])
    tm.assert_categorical_equal(result, expected)
    s = Categorical([0, 1.2, 2], ordered=True)
    s2 = Categorical([0, 1.2, 2], ordered=True)
    result = union_categoricals([s, s2])
    expected = Categorical([0, 1.2, 2, 0, 1.2, 2], ordered=True)
    tm.assert_categorical_equal(result, expected)
    s = Categorical([0, 1.2, 2])
    s2 = Categorical([2, 3, 4])
    msg = 'dtype of categories must be the same'
    with pytest.raises(TypeError, match=msg):
        union_categoricals([s, s2])
    msg = 'No Categoricals to union'
    with pytest.raises(ValueError, match=msg):
        union_categoricals([])