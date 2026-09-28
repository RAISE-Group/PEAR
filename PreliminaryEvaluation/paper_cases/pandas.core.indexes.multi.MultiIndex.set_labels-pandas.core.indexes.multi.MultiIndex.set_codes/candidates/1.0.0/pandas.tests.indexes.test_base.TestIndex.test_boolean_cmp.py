@pytest.mark.parametrize('values', [[1, 2, 3, 4], [1.0, 2.0, 3.0, 4.0], [True, True, True, True], ['foo', 'bar', 'baz', 'qux'], pd.date_range('2018-01-01', freq='D', periods=4)])
def test_boolean_cmp(self, values):
    index = Index(values)
    result = index == values
    expected = np.array([True, True, True, True], dtype=bool)
    tm.assert_numpy_array_equal(result, expected)