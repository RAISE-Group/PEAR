@pytest.mark.parametrize('level', [0, -1])
@pytest.mark.parametrize('index', [Index(['qux', 'baz', 'foo', 'bar']), Float64Index([1.0, 2.0, 3.0, 4.0])])
def test_isin_level_kwarg(self, level, index):
    values = index.tolist()[-2:] + ['nonexisting']
    expected = np.array([False, False, True, True])
    tm.assert_numpy_array_equal(expected, index.isin(values, level=level))
    index.name = 'foobar'
    tm.assert_numpy_array_equal(expected, index.isin(values, level='foobar'))