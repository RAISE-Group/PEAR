def test_comparison(self):
    with pytest.raises(TypeError, match='unorderable types'):
        Interval(0, 1) < 2
    assert Interval(0, 1) < Interval(1, 2)
    assert Interval(0, 1) < Interval(0, 2)
    assert Interval(0, 1) < Interval(0.5, 1.5)
    assert Interval(0, 1) <= Interval(0, 1)
    assert Interval(0, 1) > Interval(-1, 2)
    assert Interval(0, 1) >= Interval(0, 1)