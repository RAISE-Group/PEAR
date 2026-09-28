@pytest.mark.parametrize('tz', [None, 'US/Central'])
def test_astype_category(self, tz):
    obj = pd.date_range('2000', periods=2, tz=tz)
    result = obj.astype('category')
    expected = pd.CategoricalIndex([pd.Timestamp('2000-01-01', tz=tz), pd.Timestamp('2000-01-02', tz=tz)])
    tm.assert_index_equal(result, expected)
    result = obj._data.astype('category')
    expected = expected.values
    tm.assert_categorical_equal(result, expected)