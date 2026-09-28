def test_apply_categorical(self):
    values = pd.Categorical(list('ABBABCD'), categories=list('DCBA'), ordered=True)
    ser = pd.Series(values, name='XX', index=list('abcdefg'))
    result = ser.apply(lambda x: x.lower())
    values = pd.Categorical(list('abbabcd'), categories=list('dcba'), ordered=True)
    exp = pd.Series(values, name='XX', index=list('abcdefg'))
    tm.assert_series_equal(result, exp)
    tm.assert_categorical_equal(result.values, exp.values)
    result = ser.apply(lambda x: 'A')
    exp = pd.Series(['A'] * 7, name='XX', index=list('abcdefg'))
    tm.assert_series_equal(result, exp)
    assert result.dtype == np.object