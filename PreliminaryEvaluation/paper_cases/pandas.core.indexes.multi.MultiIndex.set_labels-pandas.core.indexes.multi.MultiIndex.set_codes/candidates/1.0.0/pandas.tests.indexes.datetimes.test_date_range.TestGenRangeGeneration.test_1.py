def test_1(self):
    rng = list(generate_range(start=datetime(2009, 3, 25), periods=2))
    expected = [datetime(2009, 3, 25), datetime(2009, 3, 26)]
    assert rng == expected