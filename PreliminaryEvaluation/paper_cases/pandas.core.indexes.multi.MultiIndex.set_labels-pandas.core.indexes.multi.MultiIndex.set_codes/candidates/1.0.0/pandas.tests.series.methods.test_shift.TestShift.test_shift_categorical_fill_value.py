def test_shift_categorical_fill_value(self):
    ts = pd.Series(['a', 'b', 'c', 'd'], dtype='category')
    res = ts.shift(1, fill_value='a')
    expected = pd.Series(pd.Categorical(['a', 'a', 'b', 'c'], categories=['a', 'b', 'c', 'd'], ordered=False))
    tm.assert_equal(res, expected)
    msg = "'fill_value=f' is not present in this Categorical's categories"
    with pytest.raises(ValueError, match=msg):
        ts.shift(1, fill_value='f')