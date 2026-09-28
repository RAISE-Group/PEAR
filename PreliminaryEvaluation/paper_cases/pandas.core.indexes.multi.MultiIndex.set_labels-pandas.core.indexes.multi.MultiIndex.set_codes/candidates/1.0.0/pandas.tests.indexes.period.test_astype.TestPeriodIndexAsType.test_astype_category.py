def test_astype_category(self):
    obj = pd.period_range('2000', periods=2)
    result = obj.astype('category')
    expected = pd.CategoricalIndex([pd.Period('2000-01-01', freq='D'), pd.Period('2000-01-02', freq='D')])
    tm.assert_index_equal(result, expected)
    result = obj._data.astype('category')
    expected = expected.values
    tm.assert_categorical_equal(result, expected)