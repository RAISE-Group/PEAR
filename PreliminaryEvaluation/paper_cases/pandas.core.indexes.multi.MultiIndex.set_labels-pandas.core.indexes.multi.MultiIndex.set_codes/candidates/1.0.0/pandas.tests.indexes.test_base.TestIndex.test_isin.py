@pytest.mark.parametrize('values', [['foo', 'bar', 'quux'], {'foo', 'bar', 'quux'}])
@pytest.mark.parametrize('index,expected', [(Index(['qux', 'baz', 'foo', 'bar']), np.array([False, False, True, True])), (Index([]), np.array([], dtype=bool))])
def test_isin(self, values, index, expected):
    result = index.isin(values)
    tm.assert_numpy_array_equal(result, expected)