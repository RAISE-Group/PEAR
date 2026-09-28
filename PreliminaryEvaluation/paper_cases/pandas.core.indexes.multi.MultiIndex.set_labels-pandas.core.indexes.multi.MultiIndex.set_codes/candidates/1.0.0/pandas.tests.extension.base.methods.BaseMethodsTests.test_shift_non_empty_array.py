@pytest.mark.parametrize('periods, indices', [[-4, [-1, -1]], [-1, [1, -1]], [0, [0, 1]], [1, [-1, 0]], [4, [-1, -1]]])
def test_shift_non_empty_array(self, data, periods, indices):
    subset = data[:2]
    result = subset.shift(periods)
    expected = subset.take(indices, allow_fill=True)
    self.assert_extension_array_equal(result, expected)