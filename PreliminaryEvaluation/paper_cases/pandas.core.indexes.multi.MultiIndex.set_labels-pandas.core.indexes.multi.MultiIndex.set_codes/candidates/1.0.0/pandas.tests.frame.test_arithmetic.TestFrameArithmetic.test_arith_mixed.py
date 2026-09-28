def test_arith_mixed(self):
    left = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [1, 2, 3]})
    result = left + left
    expected = pd.DataFrame({'A': ['aa', 'bb', 'cc'], 'B': [2, 4, 6]})
    tm.assert_frame_equal(result, expected)