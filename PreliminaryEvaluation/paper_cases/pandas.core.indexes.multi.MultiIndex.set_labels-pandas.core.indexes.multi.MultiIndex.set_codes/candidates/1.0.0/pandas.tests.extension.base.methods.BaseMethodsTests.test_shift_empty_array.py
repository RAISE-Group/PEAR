@pytest.mark.parametrize('periods', [-4, -1, 0, 1, 4])
def test_shift_empty_array(self, data, periods):
    empty = data[:0]
    result = empty.shift(periods)
    expected = empty
    self.assert_extension_array_equal(result, expected)