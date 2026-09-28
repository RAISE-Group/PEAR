def test_assignment(self):
    df = DataFrame({'value': np.array(np.random.randint(0, 10000, 100), dtype='int32')})
    labels = Categorical(['{0} - {1}'.format(i, i + 499) for i in range(0, 10000, 500)])
    df = df.sort_values(by=['value'], ascending=True)
    s = pd.cut(df.value, range(0, 10500, 500), right=False, labels=labels)
    d = s.values
    df['D'] = d
    str(df)
    result = df.dtypes
    expected = Series([np.dtype('int32'), CategoricalDtype(categories=labels, ordered=False)], index=['value', 'D'])
    tm.assert_series_equal(result, expected)
    df['E'] = s
    str(df)
    result = df.dtypes
    expected = Series([np.dtype('int32'), CategoricalDtype(categories=labels, ordered=False), CategoricalDtype(categories=labels, ordered=False)], index=['value', 'D', 'E'])
    tm.assert_series_equal(result, expected)
    result1 = df['D']
    result2 = df['E']
    tm.assert_categorical_equal(result1._data._block.values, d)
    s.name = 'E'
    tm.assert_series_equal(result2.sort_index(), s.sort_index())
    cat = Categorical([1, 2, 3, 10], categories=[1, 2, 3, 4, 10])
    df = DataFrame(Series(cat))