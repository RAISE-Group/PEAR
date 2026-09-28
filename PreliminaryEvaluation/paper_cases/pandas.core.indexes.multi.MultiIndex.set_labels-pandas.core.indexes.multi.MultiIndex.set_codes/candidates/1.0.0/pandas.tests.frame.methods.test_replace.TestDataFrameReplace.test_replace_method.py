@pytest.mark.parametrize('to_replace, method, expected', [(0, 'bfill', {'A': [1, 1, 2], 'B': [5, np.nan, 7], 'C': ['a', 'b', 'c']}), (np.nan, 'bfill', {'A': [0, 1, 2], 'B': [5.0, 7.0, 7.0], 'C': ['a', 'b', 'c']}), ('d', 'ffill', {'A': [0, 1, 2], 'B': [5, np.nan, 7], 'C': ['a', 'b', 'c']}), ([0, 2], 'bfill', {'A': [1, 1, 2], 'B': [5, np.nan, 7], 'C': ['a', 'b', 'c']}), ([1, 2], 'pad', {'A': [0, 0, 0], 'B': [5, np.nan, 7], 'C': ['a', 'b', 'c']}), ((1, 2), 'bfill', {'A': [0, 2, 2], 'B': [5, np.nan, 7], 'C': ['a', 'b', 'c']}), (['b', 'c'], 'ffill', {'A': [0, 1, 2], 'B': [5, np.nan, 7], 'C': ['a', 'a', 'a']})])
def test_replace_method(self, to_replace, method, expected):
    df = DataFrame({'A': [0, 1, 2], 'B': [5, np.nan, 7], 'C': ['a', 'b', 'c']})
    result = df.replace(to_replace=to_replace, value=None, method=method)
    expected = DataFrame(expected)
    tm.assert_frame_equal(result, expected)