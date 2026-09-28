@pytest.mark.parametrize('data', [['1400-01-01'], [datetime(1400, 1, 1)]])
def test_dti_date_out_of_range(self, data):
    msg = 'Out of bounds nanosecond timestamp: 1400-01-01 00:00:00'
    with pytest.raises(OutOfBoundsDatetime, match=msg):
        DatetimeIndex(data)