def test_between_time_types(self):
    rng = date_range('1/1/2000', '1/5/2000', freq='5min')
    msg = 'Cannot convert arg \\[datetime\\.datetime\\(2010, 1, 2, 1, 0\\)\\] to a time'
    with pytest.raises(ValueError, match=msg):
        rng.indexer_between_time(datetime(2010, 1, 2, 1), datetime(2010, 1, 2, 5))
    frame = DataFrame({'A': 0}, index=rng)
    with pytest.raises(ValueError, match=msg):
        frame.between_time(datetime(2010, 1, 2, 1), datetime(2010, 1, 2, 5))
    series = Series(0, index=rng)
    with pytest.raises(ValueError, match=msg):
        series.between_time(datetime(2010, 1, 2, 1), datetime(2010, 1, 2, 5))