def test_dt64ser_sub_datetime_dtype(self):
    ts = Timestamp(datetime(1993, 1, 7, 13, 30, 0))
    dt = datetime(1993, 6, 22, 13, 30)
    ser = Series([ts])
    result = pd.to_timedelta(np.abs(ser - dt))
    assert result.dtype == 'timedelta64[ns]'