def test_3(self):
    rng = list(generate_range(start=datetime(2008, 1, 5), end=datetime(2008, 1, 6)))
    expected = []
    assert rng == expected