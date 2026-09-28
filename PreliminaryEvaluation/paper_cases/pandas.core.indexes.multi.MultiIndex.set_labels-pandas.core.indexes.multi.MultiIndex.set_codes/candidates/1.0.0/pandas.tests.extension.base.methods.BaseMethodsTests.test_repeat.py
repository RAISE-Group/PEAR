@pytest.mark.parametrize('repeats', [0, 1, 2, [1, 2, 3]])
def test_repeat(self, data, repeats, as_series, use_numpy):
    arr = type(data)._from_sequence(data[:3], dtype=data.dtype)
    if as_series:
        arr = pd.Series(arr)
    result = np.repeat(arr, repeats) if use_numpy else arr.repeat(repeats)
    repeats = [repeats] * 3 if isinstance(repeats, int) else repeats
    expected = [x for x, n in zip(arr, repeats) for _ in range(n)]
    expected = type(data)._from_sequence(expected, dtype=data.dtype)
    if as_series:
        expected = pd.Series(expected, index=arr.index.repeat(repeats))
    self.assert_equal(result, expected)