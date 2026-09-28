def test_2(self):
    rng = list(generate_range(start=datetime(2008, 1, 1), end=datetime(2008, 1, 3)))
    expected = [datetime(2008, 1, 1), datetime(2008, 1, 2), datetime(2008, 1, 3)]
    assert rng == expected