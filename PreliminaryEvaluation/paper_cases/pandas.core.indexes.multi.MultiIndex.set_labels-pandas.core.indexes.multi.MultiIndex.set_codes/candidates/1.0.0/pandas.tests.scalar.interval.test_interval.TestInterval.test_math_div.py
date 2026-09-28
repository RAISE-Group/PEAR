def test_math_div(self, closed):
    interval = Interval(0, 1, closed=closed)
    expected = Interval(0, 0.5, closed=closed)
    result = interval / 2.0
    assert result == expected
    result = interval
    result /= 2.0
    assert result == expected
    msg = 'unsupported operand type\\(s\\) for /'
    with pytest.raises(TypeError, match=msg):
        interval / interval
    with pytest.raises(TypeError, match=msg):
        interval / 'foo'