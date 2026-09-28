@pytest.mark.parametrize('box_cls', [np.array, pd.Index, pd.Series])
@pytest.mark.parametrize('left', lefts, ids=lambda x: type(x).__name__ + str(x.dtype))
def test_div_td64arr(self, left, box_cls):
    right = np.array([10, 40, 90], dtype='m8[s]')
    right = box_cls(right)
    expected = pd.TimedeltaIndex(['1s', '2s', '3s'])
    if isinstance(left, pd.Series) or box_cls is pd.Series:
        expected = pd.Series(expected)
    result = right / left
    tm.assert_equal(result, expected)
    result = right // left
    tm.assert_equal(result, expected)
    with pytest.raises(TypeError):
        left / right
    with pytest.raises(TypeError):
        left // right