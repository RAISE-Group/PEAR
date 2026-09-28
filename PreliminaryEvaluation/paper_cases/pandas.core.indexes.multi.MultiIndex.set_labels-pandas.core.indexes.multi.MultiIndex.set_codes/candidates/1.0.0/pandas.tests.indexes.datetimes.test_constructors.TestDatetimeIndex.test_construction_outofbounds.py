def test_construction_outofbounds(self):
    dates = [datetime(3000, 1, 1), datetime(4000, 1, 1), datetime(5000, 1, 1), datetime(6000, 1, 1)]
    exp = Index(dates, dtype=object)
    tm.assert_index_equal(Index(dates), exp)
    with pytest.raises(OutOfBoundsDatetime):
        DatetimeIndex(dates)