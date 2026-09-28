def test_frame_apply_dont_convert_datetime64(self):
    from pandas.tseries.offsets import BDay
    df = DataFrame({'x1': [datetime(1996, 1, 1)]})
    df = df.applymap(lambda x: x + BDay())
    df = df.applymap(lambda x: x + BDay())
    assert df.x1.dtype == 'M8[ns]'