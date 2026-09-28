def test_frame_setitem_timestamp(self):
    columns = date_range(start='1/1/2012', end='2/1/2012', freq=BDay())
    data = DataFrame(columns=columns, index=range(10))
    t = datetime(2012, 11, 1)
    ts = Timestamp(t)
    data[ts] = np.nan
    assert np.isnan(data[ts]).all()