@pytest.mark.parametrize('empty', [[], Series(dtype=object), np.array([])])
def test_isin_empty(self, empty):
    df = DataFrame({'A': ['a', 'b', 'c'], 'B': ['a', 'e', 'f']})
    expected = DataFrame(False, df.index, df.columns)
    result = df.isin(empty)
    tm.assert_frame_equal(result, expected)