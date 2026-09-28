def test_date_range_with_fixedoffset_noname(self):
    off = fixed_off_no_name
    start = datetime(2012, 3, 11, 5, 0, 0, tzinfo=off)
    end = datetime(2012, 6, 11, 5, 0, 0, tzinfo=off)
    rng = date_range(start=start, end=end)
    assert off == rng.tz
    idx = Index([start, end])
    assert off == idx.tz