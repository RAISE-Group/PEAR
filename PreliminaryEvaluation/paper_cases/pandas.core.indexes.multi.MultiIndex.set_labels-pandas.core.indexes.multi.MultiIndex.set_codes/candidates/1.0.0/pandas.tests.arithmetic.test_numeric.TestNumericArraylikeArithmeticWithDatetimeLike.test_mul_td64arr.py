@pytest.mark.parametrize('box_cls', [np.array, pd.Index, pd.Series])
@pytest.mark.parametrize('left', lefts, ids=lambda x: type(x).__name__ + str(x.dtype))
def test_mul_td64arr(self, left, box_cls):
    right = np.array([1, 2, 3], dtype='m8[s]')
    right = box_cls(right)
    expected = pd.TimedeltaIndex(['10s', '40s', '90s'])
    if isinstance(left, pd.Series) or box_cls is pd.Series:
        expected = pd.Series(expected)
    result = left * right
    tm.assert_equal(result, expected)
    result = right * left
    tm.assert_equal(result, expected)