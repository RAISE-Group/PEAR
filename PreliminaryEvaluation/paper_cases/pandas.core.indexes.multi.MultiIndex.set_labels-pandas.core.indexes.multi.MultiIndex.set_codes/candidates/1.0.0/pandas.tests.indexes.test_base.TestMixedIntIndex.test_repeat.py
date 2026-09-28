def test_repeat(self):
    repeats = 2
    index = pd.Index([1, 2, 3])
    expected = pd.Index([1, 1, 2, 2, 3, 3])
    result = index.repeat(repeats)
    tm.assert_index_equal(result, expected)