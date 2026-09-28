def test_astype_category(self):
    obj = pd.timedelta_range('1H', periods=2, freq='H')
    result = obj.astype('category')
    expected = pd.CategoricalIndex([pd.Timedelta('1H'), pd.Timedelta('2H')])
    tm.assert_index_equal(result, expected)
    result = obj._data.astype('category')
    expected = expected.values
    tm.assert_categorical_equal(result, expected)