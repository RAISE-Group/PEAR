@pytest.mark.parametrize('data', [pd.period_range('2000', periods=4), pd.IntervalIndex.from_breaks([1, 2, 3, 4])])
def test_values_compatibility(self, data):
    result = pd.Series(data).values
    expected = np.array(data.astype(object))
    tm.assert_numpy_array_equal(result, expected)