def test_constructor_categorical_with_coercion(self):
    factor = Categorical(['a', 'b', 'b', 'a', 'a', 'c', 'c', 'c'])
    s = Series(factor, name='A')
    assert s.dtype == 'category'
    assert len(s) == len(factor)
    str(s.values)
    str(s)
    df = DataFrame({'A': factor})
    result = df['A']
    tm.assert_series_equal(result, s)
    result = df.iloc[:, 0]
    tm.assert_series_equal(result, s)
    assert len(df) == len(factor)
    str(df.values)
    str(df)
    df = DataFrame({'A': s})
    result = df['A']
    tm.assert_series_equal(result, s)
    assert len(df) == len(factor)
    str(df.values)
    str(df)
    df = DataFrame({'A': s, 'B': s, 'C': 1})
    result1 = df['A']
    result2 = df['B']
    tm.assert_series_equal(result1, s)
    tm.assert_series_equal(result2, s, check_names=False)
    assert result2.name == 'B'
    assert len(df) == len(factor)
    str(df.values)
    str(df)
    x = DataFrame([[1, 'John P. Doe'], [2, 'Jane Dove'], [1, 'John P. Doe']], columns=['person_id', 'person_name'])
    x['person_name'] = Categorical(x.person_name)
    expected = x.iloc[0].person_name
    result = x.person_name.iloc[0]
    assert result == expected
    result = x.person_name[0]
    assert result == expected
    result = x.person_name.loc[0]
    assert result == expected