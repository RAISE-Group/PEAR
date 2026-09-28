@pytest.mark.parametrize('how', ['any', 'all'])
@pytest.mark.parametrize('dtype', [None, object, 'category'])
@pytest.mark.parametrize('vals,expected', [([1, 2, 3], [1, 2, 3]), ([1.0, 2.0, 3.0], [1.0, 2.0, 3.0]), ([1.0, 2.0, np.nan, 3.0], [1.0, 2.0, 3.0]), (['A', 'B', 'C'], ['A', 'B', 'C']), (['A', np.nan, 'B', 'C'], ['A', 'B', 'C'])])
def test_dropna(self, how, dtype, vals, expected):
    index = pd.Index(vals, dtype=dtype)
    result = index.dropna(how=how)
    expected = pd.Index(expected, dtype=dtype)
    tm.assert_index_equal(result, expected)