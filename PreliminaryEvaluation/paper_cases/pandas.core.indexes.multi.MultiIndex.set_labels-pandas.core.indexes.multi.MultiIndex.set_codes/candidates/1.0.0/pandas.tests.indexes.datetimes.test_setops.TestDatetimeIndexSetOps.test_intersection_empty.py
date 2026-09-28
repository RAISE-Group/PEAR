def test_intersection_empty(self):
    rng = date_range('6/1/2000', '6/15/2000', freq='T')
    result = rng[0:0].intersection(rng)
    assert len(result) == 0
    result = rng.intersection(rng[0:0])
    assert len(result) == 0