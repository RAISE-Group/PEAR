def test_math_sub(self, closed):
    interval = Interval(0, 1, closed=closed)
    expected = Interval(-1, 0, closed=closed)
    result = interval - 1
    assert result == expected
    result = interval
    result -= 1
    assert result == expected
    msg = 'unsupported operand type\\(s\\) for -'
    with pytest.raises(TypeError, match=msg):
        interval - interval
    with pytest.raises(TypeError, match=msg):
        interval - 'foo'