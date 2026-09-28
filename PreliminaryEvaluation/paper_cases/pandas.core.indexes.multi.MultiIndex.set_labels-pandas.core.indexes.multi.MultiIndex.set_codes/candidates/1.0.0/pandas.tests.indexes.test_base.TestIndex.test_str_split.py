@pytest.mark.parametrize('expand,expected', [(None, Index([['a', 'b', 'c'], ['d', 'e'], ['f']])), (False, Index([['a', 'b', 'c'], ['d', 'e'], ['f']])), (True, MultiIndex.from_tuples([('a', 'b', 'c'), ('d', 'e', np.nan), ('f', np.nan, np.nan)]))])
def test_str_split(self, expand, expected):
    index = Index(['a b c', 'd e', 'f'])
    if expand is not None:
        result = index.str.split(expand=expand)
    else:
        result = index.str.split()
    tm.assert_index_equal(result, expected)